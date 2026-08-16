"""Structured preview of the files detected by PyTeXmd's LaTeX loader."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

from pytexmd.file_loader import (
    BIB_EXTENSIONS,
    IMAGE_EXTENSIONS,
    INPUT_PATTERN,
    TEX_EXTENSIONS,
)


@dataclass(frozen=True)
class DetectedFile:
    path: Path
    category: str
    mechanisms: tuple[str, ...]


@dataclass(frozen=True)
class DetectionReport:
    root: Path
    files: tuple[DetectedFile, ...]
    missing_inputs: tuple[str, ...]
    collisions: tuple[str, ...]
    warnings: tuple[str, ...]


def detect_project_files(input_file: str | Path) -> DetectionReport:
    r"""Mirror the loader's filesystem scan and exact ``\input{}`` resolution."""
    entry = Path(input_file).expanduser().resolve()
    if not entry.is_file():
        raise FileNotFoundError(f"LaTeX input file not found: {entry}")
    root = entry.parent
    categories = {
        **{extension: "LaTeX inventory" for extension in TEX_EXTENSIONS},
        **{extension: "Bibliography" for extension in BIB_EXTENSIONS},
        **{extension: "Image inventory" for extension in IMAGE_EXTENSIONS},
    }
    mechanisms: dict[Path, list[str]] = {}
    file_categories: dict[Path, str] = {}
    scanned: list[Path] = []
    warnings: list[str] = []

    def record_walk_error(error: OSError) -> None:
        warnings.append(f"Could not scan {error.filename}: {error}")

    for directory, directories, filenames in os.walk(root, onerror=record_walk_error):
        directories.sort(key=str.casefold)
        filenames.sort(key=str.casefold)
        for filename in filenames:
            path = Path(directory, filename).resolve()
            category = categories.get(path.suffix.lower())
            if category is None:
                continue
            scanned.append(path)
            file_categories[path] = category
            mechanisms.setdefault(path, []).append("recursive extension scan")

    file_categories[entry] = "Entry source"
    mechanisms.setdefault(entry, []).insert(0, "selected entry file")

    known_extensions = TEX_EXTENSIONS + IMAGE_EXTENSIONS + BIB_EXTENSIONS

    def key(path: Path) -> str:
        return path.stem if path.suffix.lower() in known_extensions else path.name

    tex = {key(path): path for path in scanned if path.suffix.lower() in TEX_EXTENSIONS}
    bib = {key(path): path for path in scanned if path.suffix.lower() in BIB_EXTENSIONS}
    images = {
        key(path): path for path in scanned if path.suffix.lower() in IMAGE_EXTENSIONS
    }
    all_files = {**tex, **bib, **images}

    collision_groups: dict[str, list[Path]] = {}
    for path in scanned:
        collision_groups.setdefault(key(path), []).append(path)
    collisions = tuple(
        f"{name}: " + ", ".join(str(path) for path in paths)
        for name, paths in collision_groups.items()
        if len(paths) > 1
    )

    def resolve_input(argument: str) -> Path:
        normalized = argument.replace("\\", "/")
        candidate = Path(os.path.normpath(os.path.join(root, normalized)))
        if candidate.is_file():
            return candidate.resolve()
        for extension in TEX_EXTENSIONS:
            extended = Path(str(candidate) + extension)
            if extended.is_file():
                return extended.resolve()
        bare = Path(normalized).name
        suffix = Path(bare).suffix.lower()
        if suffix in known_extensions:
            bare = Path(bare).stem
        if bare in all_files:
            return all_files[bare]
        raise FileNotFoundError(argument)

    pending = [entry]
    seen_arguments: set[str] = set()
    external_input_directories: set[Path] = set()
    missing_inputs: list[str] = []
    while pending:
        source = pending.pop(0)
        try:
            content = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            warnings.append(f"Could not read input candidate {source}: {exc}")
            continue
        for argument in re.findall(INPUT_PATTERN, content):
            if argument in seen_arguments:
                continue
            seen_arguments.add(argument)
            try:
                resolved = resolve_input(argument)
            except FileNotFoundError:
                missing_inputs.append(argument)
                continue
            mechanism = f"resolved from \\input{{{argument}}}"
            mechanisms.setdefault(resolved, []).append(mechanism)
            file_categories.setdefault(resolved, "Expanded input")
            pending.append(resolved)
            try:
                resolved.parent.relative_to(root)
            except ValueError:
                external_input_directories.add(resolved.parent)

    for external_directory in external_input_directories:
        for directory, directories, filenames in os.walk(
            external_directory, onerror=record_walk_error
        ):
            directories.sort(key=str.casefold)
            filenames.sort(key=str.casefold)
            for filename in filenames:
                path = Path(directory, filename).resolve()
                if path.suffix.lower() not in BIB_EXTENSIONS:
                    continue
                file_categories[path] = "Bibliography"
                mechanisms.setdefault(path, []).append(
                    "bibliography scan beside external input"
                )

    files = tuple(
        DetectedFile(path, file_categories[path], tuple(dict.fromkeys(reasons)))
        for path, reasons in sorted(
            mechanisms.items(),
            key=lambda item: (file_categories[item[0]], str(item[0])),
        )
    )
    return DetectionReport(
        root,
        files,
        tuple(missing_inputs),
        collisions,
        tuple(warnings),
    )
