"""Local browser editor for generated PyTeXmd Sphinx projects."""

from __future__ import annotations

import argparse
import io
import json
import mimetypes
import posixpath
import re
import shutil
import threading
import webbrowser
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import dataclass
from datetime import UTC, datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from urllib.parse import parse_qs, unquote, urlparse

from pytexmd.sphinx_doc import make_html

_DIRECTIVE_RE = re.compile(
    r"^(?P<fence>:{3,}|`{3,})\{(?P<name>[^}]+)\}(?:\s+(?P<title>.*))?$"
)
_HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<text>.*)$")
_PLAIN_FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?!\{)")
_NON_PARAGRAPH_RE = re.compile(r"^(?:[-*+]\s|\d+[.)]\s|>|\||<|\s{4})")
_LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)")
_ADMONITION_DIRECTIVES = {
    "admonition",
    "attention",
    "caution",
    "danger",
    "error",
    "hint",
    "important",
    "note",
    "seealso",
    "tip",
    "warning",
}
_ADMONITION_COLORS = {"note", "tip", "warning", "danger", "important"}


@dataclass
class EditableBlock:
    kind: str
    start: int
    end: int
    value: str
    prefix: str = ""
    index: int = 0
    metadata: dict | None = None


@dataclass
class ToctreeEntry:
    line: int
    document: str
    group: int


def _directive_ranges(lines: list[str]) -> tuple[list[dict], set[int]]:
    stack: list[dict] = []
    ranges: list[dict] = []
    structural_lines: set[int] = set()
    for index, line in enumerate(lines):
        match = _DIRECTIVE_RE.match(line)
        if match:
            frame = {
                "start": index,
                "fence": match.group("fence"),
                "name": match.group("name"),
                "title": match.group("title") or "",
                "opener": line,
            }
            stack.append(frame)
            structural_lines.add(index)
            continue
        if stack and line.strip() == stack[-1]["fence"]:
            frame = stack.pop()
            frame["end"] = index
            ranges.append(frame)
            structural_lines.add(index)
    return ranges, structural_lines


def _list_metadata(value: str) -> dict:
    """Describe a MyST list for the editor's dedicated item controls."""
    lines = value.splitlines()
    bullet_items = []
    ordered_items = []
    for line in lines:
        bullet = re.match(r"^\s*[-+*]\s+(.*)$", line)
        ordered = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if bullet:
            bullet_items.append({"label": "", "content": bullet.group(1)})
        elif ordered:
            ordered_items.append({"label": "", "content": ordered.group(1)})
    if bullet_items and len(bullet_items) == len(lines):
        return {"style": "bullet", "items": bullet_items}
    if ordered_items and len(ordered_items) == len(lines):
        return {"style": "ordered", "items": ordered_items}

    definition_items = []
    index = 0
    while index + 1 < len(lines):
        if lines[index + 1].startswith(": "):
            definition_items.append(
                {"label": lines[index].strip(), "content": lines[index + 1][2:].strip()}
            )
            index += 2
        else:
            index += 1
    if definition_items:
        numeric = all(
            re.fullmatch(r"\d+[.)]?", item["label"]) for item in definition_items
        )
        return {
            "style": "enumeration" if numeric else "custom_enumeration",
            "items": definition_items,
        }
    return {"style": "raw", "items": []}


def _admonition_metadata(lines: list[str], item: dict) -> dict:
    classes = []
    for line in lines[item["start"] + 1 : item["end"]]:
        if line.startswith(":class:"):
            classes = line.partition(":class:")[2].strip().split()
            break
        if line.strip() and not line.startswith(":"):
            break
    return {
        "directive": item["name"],
        "title": item["title"],
        "color": next((name for name in classes if name in _ADMONITION_COLORS), ""),
    }


def _update_admonition(value: str, title: str, color: str) -> str:
    """Apply structured title and color fields to an admonition source block."""
    lines = value.splitlines()
    if not lines:
        raise ValueError("Admonition source cannot be empty.")
    opener = _DIRECTIVE_RE.match(lines[0])
    if not opener or opener.group("name") not in _ADMONITION_DIRECTIVES:
        raise ValueError("The edited source is not a supported MyST admonition.")
    title = title.strip()
    directive_name = opener.group("name")
    if not title and directive_name == "admonition":
        raise ValueError("Admonition title cannot be empty.")
    if color not in _ADMONITION_COLORS | {""}:
        raise ValueError("Unknown admonition color.")

    lines[0] = f'{opener.group("fence")}{{{directive_name}}}' + (
        f" {title}" if title else ""
    )
    class_index = None
    for index, line in enumerate(lines[1:], 1):
        if line.startswith(":class:"):
            class_index = index
            break
        if not line.strip() or not line.startswith(":"):
            break
    classes = []
    if class_index is not None:
        classes = lines[class_index].partition(":class:")[2].strip().split()
    classes = [name for name in classes if name not in _ADMONITION_COLORS]
    if color:
        classes.append(color)
    if classes:
        class_line = ":class: " + " ".join(classes)
        if class_index is None:
            lines.insert(1, class_line)
        else:
            lines[class_index] = class_line
    elif class_index is not None:
        del lines[class_index]
    return "\n".join(lines)


def parse_editable_blocks(markdown: str) -> list[EditableBlock]:
    """Return source spans that can safely round-trip from the visual editor."""
    lines = markdown.splitlines()
    ranges, structural = _directive_ranges(lines)
    protected: set[int] = set()
    blocks: list[EditableBlock] = []

    plain_fence = None
    for index, line in enumerate(lines):
        if index in structural:
            continue
        match = _PLAIN_FENCE_RE.match(line)
        if plain_fence is None and match:
            plain_fence = (match.group("fence"), index)
        elif plain_fence is not None and line.startswith(plain_fence[0]):
            protected.update(range(plain_fence[1], index + 1))
            plain_fence = None
    if plain_fence is not None:
        protected.update(range(plain_fence[1], len(lines)))

    blocks.append(EditableBlock("page", 0, len(lines), markdown))

    for item in ranges:
        name = item["name"]
        start = item["start"]
        end = item["end"]
        if name not in _ADMONITION_DIRECTIVES:
            protected.update(range(start + 1, end))
        if name in _ADMONITION_DIRECTIVES:
            blocks.append(
                EditableBlock(
                    "admonition",
                    start,
                    end + 1,
                    "\n".join(lines[start : end + 1]),
                    metadata=_admonition_metadata(lines, item),
                )
            )
        if name == "admonition":
            prefix = (
                item["opener"][: len(item["opener"]) - len(item["title"])]
                if item["title"]
                else item["opener"] + " "
            )
            blocks.append(
                EditableBlock(
                    "directive_title", start, start + 1, item["title"], prefix
                )
            )
        if name in {"math", "tikz"}:
            content_start = start + 1
            while content_start < end and lines[content_start].startswith(":"):
                content_start += 1
            if content_start < end and not lines[content_start].strip():
                content_start += 1
            protected.update(range(start + 1, end))
            if name == "math":
                blocks.append(
                    EditableBlock(
                        "equation",
                        content_start,
                        end,
                        "\n".join(lines[content_start:end]).strip(),
                    )
                )
            else:
                scale_line = next(
                    (
                        i
                        for i in range(start + 1, end)
                        if lines[i].startswith(":xscale:")
                    ),
                    None,
                )
                value = (
                    lines[scale_line].partition(":xscale:")[2].strip()
                    if scale_line is not None
                    else "1"
                )
                insertion = scale_line if scale_line is not None else start + 1
                blocks.append(
                    EditableBlock(
                        "tikz_scale",
                        insertion,
                        insertion + (scale_line is not None),
                        value,
                    )
                )

    index = 0
    while index < len(lines):
        if index in structural or index in protected or not lines[index].strip():
            index += 1
            continue
        heading = _HEADING_RE.match(lines[index])
        if heading:
            blocks.append(
                EditableBlock(
                    "heading",
                    index,
                    index + 1,
                    heading.group("text"),
                    heading.group("marks") + " ",
                )
            )
            index += 1
            continue
        if lines[index].startswith(":"):
            index += 1
            continue
        is_definition_list = (
            index + 1 < len(lines)
            and bool(lines[index].strip())
            and lines[index + 1].startswith(": ")
        )
        if _LIST_ITEM_RE.match(lines[index]) or is_definition_list:
            start = index
            while index < len(lines):
                if (
                    not lines[index].strip()
                    or index in structural
                    or index in protected
                    or _HEADING_RE.match(lines[index])
                ):
                    break
                index += 1
            blocks.append(
                EditableBlock(
                    "list",
                    start,
                    index,
                    "\n".join(lines[start:index]),
                    metadata=_list_metadata("\n".join(lines[start:index])),
                )
            )
            continue
        if _NON_PARAGRAPH_RE.match(lines[index]):
            while index < len(lines) and lines[index].strip():
                index += 1
            continue
        start = index
        while index < len(lines):
            if (
                not lines[index].strip()
                or index in structural
                or index in protected
                or _HEADING_RE.match(lines[index])
                or lines[index].startswith(":")
            ):
                break
            index += 1
        if index > start:
            blocks.append(
                EditableBlock("paragraph", start, index, "\n".join(lines[start:index]))
            )
        else:
            index += 1

    blocks.sort(key=lambda block: (block.start, block.kind))
    counters: dict[str, int] = {}
    for block in blocks:
        block.index = counters.get(block.kind, 0)
        counters[block.kind] = block.index + 1

    admonitions = [block for block in blocks if block.kind == "admonition"]
    sibling_counts: dict[tuple[str, int | None], int] = {}
    for block in blocks:
        parents = [
            parent
            for parent in admonitions
            if parent is not block
            and parent.start <= block.start
            and block.end <= parent.end
        ]
        parent = min(parents, key=lambda item: item.end - item.start, default=None)
        metadata = dict(block.metadata or {})
        parent_index = parent.index if parent is not None else None
        sibling_key = (block.kind, parent_index)
        sibling_index = sibling_counts.get(sibling_key, 0)
        sibling_counts[sibling_key] = sibling_index + 1
        metadata["nesting"] = {
            "depth": len(parents),
            "parent": parent_index,
            "sibling": sibling_index,
        }
        block.metadata = metadata
    return blocks


def apply_visual_changes(markdown: str, changes: list[dict]) -> str:
    """Apply structured visual changes to MyST without disturbing directives."""
    blocks = parse_editable_blocks(markdown)
    lookup = {(block.kind, block.index): block for block in blocks}
    replacements: list[tuple[int, int, list[str]]] = []
    seen: set[tuple[str, int]] = set()
    selected_blocks: list[EditableBlock] = []

    for change in changes:
        key = (str(change.get("kind", "")), int(change.get("index", -1)))
        if key in seen:
            raise ValueError(
                f"Duplicate editable element in one save request: {key[0]} {key[1]}"
            )
        if key not in lookup:
            raise ValueError(
                f"The selected {key[0]} is no longer mapped to the current Markdown "
                "source. Reload the page and try again."
            )
        seen.add(key)
        block = lookup[key]
        if any(
            block.start < selected.end and selected.start < block.end
            for selected in selected_blocks
        ):
            raise ValueError(
                "Overlapping visual edits were selected. Save either the whole "
                "admonition/list or its individual child edits, not both."
            )
        selected_blocks.append(block)
        value = str(change.get("value", "")).strip()
        if block.kind == "admonition" and (
            "admonition_title" in change or "admonition_color" in change
        ):
            value = _update_admonition(
                value,
                str(change.get("admonition_title", "")),
                str(change.get("admonition_color", "")),
            )
            new_lines = value.splitlines()
        elif block.kind == "tikz_scale":
            try:
                numeric_scale = float(value)
            except ValueError as exc:
                raise ValueError("TikZ scale must be a number.") from exc
            if not 0.1 <= numeric_scale <= 4:
                raise ValueError("TikZ scale must be between 0.1 and 4.")
            value = f"{numeric_scale:g}"
            new_lines = [f":xscale: {value}"]
        elif block.kind in {"heading", "directive_title"}:
            if not value:
                raise ValueError(
                    f"{block.kind.replace('_', ' ').title()} cannot be empty."
                )
            new_lines = [(block.prefix + value).rstrip()]
        else:
            new_lines = value.splitlines()
        replacements.append((block.start, block.end, new_lines))

    lines = markdown.splitlines()
    for start, end, replacement in sorted(replacements, reverse=True):
        lines[start:end] = replacement
    result = "\n".join(lines)
    return result + ("\n" if markdown.endswith("\n") else "")


def _toctree_entries(markdown: str, owner: str) -> list[ToctreeEntry]:
    """Return resolved document entries from each MyST toctree."""
    lines = markdown.splitlines()
    ranges, _ = _directive_ranges(lines)
    entries = []
    owner_parent = PurePosixPath(owner).parent
    group = 0
    for item in ranges:
        if item["name"] != "toctree":
            continue
        for line_number in range(item["start"] + 1, item["end"]):
            value = lines[line_number].strip()
            if not value or value.startswith((":", "http")):
                continue
            titled = re.match(r".*<([^>]+)>$", value)
            document = titled.group(1).strip() if titled else value
            document = document.removeprefix("/")
            path = owner_parent / document.replace("\\", "/")
            if path.suffix:
                path = path.with_suffix("")
            resolved = posixpath.normpath(path.as_posix()) + ".md"
            entries.append(ToctreeEntry(line_number, resolved, group))
        group += 1
    return entries


def _page_slug(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return slug or "page"


class SphinxProject:
    def __init__(self, path: str | Path):
        selected = Path(path).expanduser().absolute()
        if (selected / "source" / "conf.py").is_file():
            root = selected
        elif (selected / "conf.py").is_file():
            root = selected.parent
        elif (
            selected.name == "html"
            and selected.parent.name == "build"
            and (selected.parent.parent / "source" / "conf.py").is_file()
        ):
            root = selected.parent.parent
        else:
            root = selected
        self.root = root.resolve()
        self.source = (root / "source").resolve()
        self.html = (root / "build" / "html").resolve()
        self._lock = threading.RLock()
        if not (self.source / "conf.py").is_file():
            raise ValueError(f"Not a Sphinx project: {self.root}")

    def _source_path(self, relative: str) -> Path:
        path = (self.source / unquote(relative)).resolve()
        if self.source not in path.parents or path.suffix != ".md":
            raise ValueError("Invalid Markdown path.")
        return path

    def pages(self) -> list[dict]:
        paths = {
            path.relative_to(self.source).as_posix(): path
            for path in self.source.rglob("*.md")
        }
        ordered: list[str] = []
        parents: dict[str, str] = {}

        def visit(relative: str) -> None:
            if relative in ordered or relative not in paths:
                return
            ordered.append(relative)
            markdown = paths[relative].read_text(encoding="utf-8")
            for entry in _toctree_entries(markdown, relative):
                if entry.document in paths:
                    parents.setdefault(entry.document, relative)
                    visit(entry.document)

        visit("index.md")
        ordered.extend(sorted(set(paths) - set(ordered)))
        pages = []
        for relative in ordered:
            path = paths[relative]
            markdown = path.read_text(encoding="utf-8")
            heading = next(
                (
                    match.group("text")
                    for line in markdown.splitlines()
                    if (match := _HEADING_RE.match(line))
                ),
                path.stem,
            )
            html_relative = PurePosixPath(relative).with_suffix(".html").as_posix()
            pages.append(
                {
                    "path": relative,
                    "title": heading,
                    "preview": f"/preview/{html_relative}",
                    "built": (self.html / html_relative).is_file(),
                    "parent": parents.get(relative),
                    "protected": relative in {"index.md", "references.md"},
                }
            )
        return pages

    def create_page(self, title: str, slug: str = "") -> tuple[str, str]:
        title = title.strip()
        if not title:
            raise ValueError("Page title cannot be empty.")
        if len(title) > 200:
            raise ValueError("Page title is too long.")
        slug = (slug.strip() or _page_slug(title)).removesuffix(".md")
        if not re.fullmatch(r"[A-Za-z0-9_-]+", slug):
            raise ValueError(
                "Page filename may contain letters, numbers, hyphens, and underscores."
            )
        relative = slug + ".md"
        path = self._source_path(relative)
        if path.exists():
            raise ValueError(f"A page named {relative} already exists.")

        with self._lock:
            path.write_text(f"# {title}\n\n", encoding="utf-8")
            index_path = self._source_path("index.md")
            index = index_path.read_text(encoding="utf-8")
            lines = index.splitlines()
            ranges, _ = _directive_ranges(lines)
            root_toctree = next(
                (item for item in ranges if item["name"] == "toctree"), None
            )
            if root_toctree is None:
                updated = (
                    index.rstrip()
                    + f"\n\n```{{toctree}}\n:maxdepth: 2\n\n{slug}\n```\n"
                )
            else:
                insertion = root_toctree["end"]
                existing = _toctree_entries(index, "index.md")
                references = next(
                    (entry for entry in existing if entry.document == "references.md"),
                    None,
                )
                if references is not None:
                    insertion = references.line
                lines.insert(insertion, slug)
                updated = "\n".join(lines) + ("\n" if index.endswith("\n") else "")
            self._write("index.md", updated)
            return relative, self.build()

    def delete_page(self, relative: str) -> str:
        if relative in {"index.md", "references.md"}:
            raise ValueError(
                f"{relative} is required by the Sphinx project and cannot be deleted."
            )
        path = self._source_path(relative)
        if not path.is_file():
            raise ValueError(f"Page does not exist: {relative}")

        with self._lock:
            for owner in self.source.rglob("*.md"):
                owner_relative = owner.relative_to(self.source).as_posix()
                markdown = owner.read_text(encoding="utf-8")
                entries = _toctree_entries(markdown, owner_relative)
                remove_lines = {
                    entry.line for entry in entries if entry.document == relative
                }
                if remove_lines:
                    lines = markdown.splitlines()
                    updated = "\n".join(
                        line
                        for index, line in enumerate(lines)
                        if index not in remove_lines
                    )
                    if markdown.endswith("\n"):
                        updated += "\n"
                    self._write(owner_relative, updated)
            stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S-%f")
            backup = self.root / ".pytexmd-editor" / "backups" / stamp / Path(relative)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, backup)
            path.unlink()
            return self.build()

    def move_page(self, relative: str, direction: str) -> str:
        if relative == "index.md":
            raise ValueError("The index page is always the navigation root.")
        if direction not in {"up", "down"}:
            raise ValueError("Direction must be 'up' or 'down'.")

        with self._lock:
            page = next(
                (item for item in self.pages() if item["path"] == relative), None
            )
            if page is None or page["parent"] is None:
                raise ValueError(
                    "Page is not listed in a toctree and cannot be reordered."
                )
            owner_relative = page["parent"]
            markdown = self._source_path(owner_relative).read_text(encoding="utf-8")
            entries = _toctree_entries(markdown, owner_relative)
            selected = next(
                (entry for entry in entries if entry.document == relative), None
            )
            if selected is None:
                raise ValueError("Page is not listed in its parent toctree.")
            siblings = [entry for entry in entries if entry.group == selected.group]
            position = siblings.index(selected)
            target = position - 1 if direction == "up" else position + 1
            if target < 0 or target >= len(siblings):
                raise ValueError(
                    f"Page is already at the {direction} edge of its section."
                )
            lines = markdown.splitlines()
            first = siblings[position].line
            second = siblings[target].line
            lines[first], lines[second] = lines[second], lines[first]
            updated = "\n".join(lines) + ("\n" if markdown.endswith("\n") else "")
            self._write(owner_relative, updated)
            return self.build()

    def reorder_page(self, relative: str, target_relative: str) -> str:
        """Move a page before another sibling in the same toctree."""
        if relative == target_relative:
            return "Page order unchanged."
        with self._lock:
            pages = {item["path"]: item for item in self.pages()}
            page = pages.get(relative)
            target_page = pages.get(target_relative)
            if not page or not target_page or page["parent"] != target_page["parent"]:
                raise ValueError("Pages can only be reordered among siblings.")
            owner_relative = page["parent"]
            if owner_relative is None:
                raise ValueError("Root pages cannot be reordered.")
            markdown = self._source_path(owner_relative).read_text(encoding="utf-8")
            entries = _toctree_entries(markdown, owner_relative)
            selected = next((item for item in entries if item.document == relative), None)
            target = next(
                (item for item in entries if item.document == target_relative), None
            )
            if selected is None or target is None or selected.group != target.group:
                raise ValueError("Pages must belong to the same navigation group.")
            siblings = [item for item in entries if item.group == selected.group]
            ordered = [item.document for item in siblings]
            ordered.remove(relative)
            ordered.insert(ordered.index(target_relative), relative)
            lines = markdown.splitlines()
            original = {item.document: lines[item.line] for item in siblings}
            for item, document in zip(siblings, ordered):
                lines[item.line] = original[document]
            updated = "\n".join(lines) + ("\n" if markdown.endswith("\n") else "")
            self._write(owner_relative, updated)
            return self.build()

    def paste_page(
        self, source_relative: str, target_relative: str, position: str, mode: str
    ) -> tuple[str, str]:
        """Copy or move a page above or below another navigation entry."""
        if position not in {"above", "below"} or mode not in {"copy", "cut"}:
            raise ValueError("Invalid page paste operation.")
        with self._lock:
            pages = {item["path"]: item for item in self.pages()}
            source_page = pages.get(source_relative)
            target_page = pages.get(target_relative)
            if source_page is None or target_page is None or target_page["parent"] is None:
                raise ValueError("Both clipboard and target pages must be in navigation.")
            if source_page["parent"] is None:
                raise ValueError("The navigation root cannot be copied or moved.")
            if mode == "cut" and source_page["protected"]:
                raise ValueError("This required page cannot be moved.")
            if mode == "cut" and source_relative == target_relative:
                raise ValueError("Choose a different target for the cut page.")

            if mode == "cut":
                ancestor = target_relative
                while ancestor is not None:
                    if ancestor == source_relative:
                        raise ValueError("A page cannot be moved inside its own descendants.")
                    ancestor = pages.get(ancestor, {}).get("parent")
                pasted_relative = source_relative
            else:
                source_path = PurePosixPath(source_relative)
                target_parent = PurePosixPath(target_relative).parent
                stem = source_path.stem + "_copy"
                candidate = target_parent / f"{stem}.md"
                suffix = 2
                while (self.source / candidate).exists():
                    candidate = target_parent / f"{stem}_{suffix}.md"
                    suffix += 1
                pasted_relative = candidate.as_posix()
                destination = self._source_path(pasted_relative)
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(
                    self._source_path(source_relative).read_text(encoding="utf-8"),
                    encoding="utf-8",
                )

            target_owner = target_page["parent"]
            source_owner = source_page["parent"]
            target_markdown = self._source_path(target_owner).read_text(encoding="utf-8")

            if mode == "cut" and source_owner == target_owner:
                lines = target_markdown.splitlines()
                entries = _toctree_entries(target_markdown, target_owner)
                source_entry = next(
                    (item for item in entries if item.document == source_relative), None
                )
                target_entry = next(
                    (item for item in entries if item.document == target_relative), None
                )
                if source_entry is None or target_entry is None:
                    raise ValueError("Could not locate page navigation entries.")
                lines.pop(source_entry.line)
                target_line = target_entry.line - (source_entry.line < target_entry.line)
            else:
                if mode == "cut":
                    old_markdown = self._source_path(source_owner).read_text(encoding="utf-8")
                    old_entries = _toctree_entries(old_markdown, source_owner)
                    source_entry = next(
                        (item for item in old_entries if item.document == source_relative),
                        None,
                    )
                    if source_entry is None:
                        raise ValueError("Could not locate the page being moved.")
                    old_lines = old_markdown.splitlines()
                    old_lines.pop(source_entry.line)
                    self._write(
                        source_owner,
                        "\n".join(old_lines)
                        + ("\n" if old_markdown.endswith("\n") else ""),
                    )
                lines = target_markdown.splitlines()
                target_entries = _toctree_entries(target_markdown, target_owner)
                target_entry = next(
                    (item for item in target_entries if item.document == target_relative),
                    None,
                )
                if target_entry is None:
                    raise ValueError("Could not locate the target navigation entry.")
                target_line = target_entry.line

            owner_parent = PurePosixPath(target_owner).parent.as_posix() or "."
            document = PurePosixPath(pasted_relative).with_suffix("").as_posix()
            reference = posixpath.relpath(document, owner_parent)
            indentation = re.match(r"\s*", lines[target_line]).group()
            insertion = target_line + (1 if position == "below" else 0)
            lines.insert(insertion, indentation + reference)
            updated = "\n".join(lines) + ("\n" if target_markdown.endswith("\n") else "")
            self._write(target_owner, updated)
            return pasted_relative, self.build()

    def read_page(self, relative: str) -> dict:
        path = self._source_path(relative)
        markdown = path.read_text(encoding="utf-8")
        elements = []
        for block in parse_editable_blocks(markdown):
            elements.append(
                {
                    "kind": block.kind,
                    "index": block.index,
                    "value": block.value,
                    "metadata": block.metadata,
                }
            )
        return {"path": relative, "markdown": markdown, "elements": elements}

    def _write(self, relative: str, markdown: str) -> None:
        path = self._source_path(relative)
        stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S-%f")
        backup = self.root / ".pytexmd-editor" / "backups" / stamp / Path(relative)
        backup.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            shutil.copy2(path, backup)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(markdown, encoding="utf-8")
        temporary.replace(path)

    def save_source(self, relative: str, markdown: str, rebuild: bool = True) -> str:
        with self._lock:
            self._write(relative, markdown)
            return self.build() if rebuild else "Source saved without rebuilding."

    def save_visual(self, relative: str, changes: list[dict]) -> str:
        with self._lock:
            path = self._source_path(relative)
            markdown = path.read_text(encoding="utf-8")
            self._write(relative, apply_visual_changes(markdown, changes))
            return self.build()

    def build(self) -> str:
        with self._lock:
            output = io.StringIO()
            with redirect_stdout(output), redirect_stderr(output):
                make_html(str(self.root), raise_on_error=True)
            return output.getvalue()


class EditorServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, project: SphinxProject):
        self.project = project
        super().__init__(address, EditorRequestHandler)
        self.editor_url = f"http://127.0.0.1:{self.server_port}/"


class EditorRequestHandler(BaseHTTPRequestHandler):
    server: EditorServer

    def log_message(self, format, *args):
        pass

    def _json(self, value, status=HTTPStatus.OK):
        payload = json.dumps(value).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _file(self, path: Path, content_type: str | None = None):
        if not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        payload = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header(
            "Content-Type",
            content_type
            or mimetypes.guess_type(path.name)[0]
            or "application/octet-stream",
        )
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        assets = Path(__file__).parent / "editor_assets"
        try:
            if parsed.path == "/":
                self._file(assets / "index.html", "text/html; charset=utf-8")
            elif parsed.path.startswith("/assets/"):
                name = Path(parsed.path).name
                self._file(assets / name)
            elif parsed.path == "/api/project":
                self._json(
                    {
                        "root": str(self.server.project.root),
                        "pages": self.server.project.pages(),
                    }
                )
            elif parsed.path == "/api/page":
                relative = parse_qs(parsed.query).get("path", [""])[0]
                self._json(self.server.project.read_page(relative))
            elif parsed.path.startswith("/preview/"):
                relative = unquote(parsed.path.removeprefix("/preview/"))
                target = (self.server.project.html / relative).resolve()
                if self.server.project.html not in target.parents:
                    raise ValueError("Invalid preview path.")
                if target.suffix == ".html":
                    html = target.read_text(encoding="utf-8")
                    injection = (assets / "frame.js").read_text(encoding="utf-8")
                    html = html.replace(
                        "</body>", f"<script>{injection}</script></body>"
                    )
                    payload = html.encode("utf-8")
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Cache-Control", "no-store")
                    self.send_header("Content-Length", str(len(payload)))
                    self.end_headers()
                    self.wfile.write(payload)
                else:
                    self._file(target)
            else:
                self.send_error(HTTPStatus.NOT_FOUND)
        except (OSError, ValueError) as exc:
            self._json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)

    def do_POST(self):
        try:
            body = self._body()
            page = None
            if self.path == "/api/save":
                log = self.server.project.save_source(
                    body["path"], str(body["markdown"]), bool(body.get("rebuild", True))
                )
            elif self.path == "/api/visual-save":
                log = self.server.project.save_visual(
                    body["path"], list(body["changes"])
                )
            elif self.path == "/api/build":
                log = self.server.project.build()
            elif self.path == "/api/pages/create":
                page, log = self.server.project.create_page(
                    str(body["title"]), str(body.get("slug", ""))
                )
            elif self.path == "/api/pages/delete":
                log = self.server.project.delete_page(str(body["path"]))
            elif self.path == "/api/pages/move":
                log = self.server.project.move_page(
                    str(body["path"]), str(body["direction"])
                )
            elif self.path == "/api/pages/reorder":
                log = self.server.project.reorder_page(
                    str(body["path"]), str(body["target"])
                )
            elif self.path == "/api/pages/paste":
                page, log = self.server.project.paste_page(
                    str(body["source"]),
                    str(body["target"]),
                    str(body["position"]),
                    str(body["mode"]),
                )
            else:
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            self._json(
                {
                    "ok": True,
                    "log": log,
                    "page": page,
                    "pages": self.server.project.pages(),
                }
            )
        except (
            KeyError,
            OSError,
            RuntimeError,
            ValueError,
            json.JSONDecodeError,
        ) as exc:
            self._json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)


def launch_editor(project_path: str | Path, open_browser: bool = True) -> EditorServer:
    """Start the editor server and optionally open its browser interface."""
    project = SphinxProject(project_path)
    server = EditorServer(("127.0.0.1", 0), project)
    if open_browser:
        threading.Timer(0.2, webbrowser.open, args=(server.editor_url,)).start()
    print(f"PyTeXmd Project Editor: {server.editor_url}")
    return server


def choose_project_path() -> str | None:
    """Ask for a Sphinx project when the editor is started without a path."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError as exc:
        raise RuntimeError(
            "A project path is required because Tkinter is unavailable. On "
            "Debian/Ubuntu install it with: sudo apt install python3-tk"
        ) from exc

    root = None
    try:
        root = tk.Tk()
        root.withdraw()
        root.update_idletasks()
        project = filedialog.askdirectory(
            parent=root,
            title="Select a generated PyTeXmd Sphinx project",
            mustexist=True,
        )
    except tk.TclError as exc:
        raise RuntimeError(
            "Could not open the project chooser. Pass the Sphinx project path "
            "to pytexmd-editor explicitly."
        ) from exc
    finally:
        if root is not None:
            root.destroy()
    return project or None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Edit a generated PyTeXmd Sphinx project."
    )
    parser.add_argument(
        "project",
        nargs="?",
        help="Sphinx project folder containing source/ and build/",
    )
    parser.add_argument(
        "--no-browser", action="store_true", help="Do not open a browser"
    )
    args = parser.parse_args()
    project = args.project
    if project is None:
        try:
            project = choose_project_path()
        except RuntimeError as exc:
            parser.exit(1, f"pytexmd-editor: error: {exc}\n")
        if project is None:
            return
    try:
        server = launch_editor(project, not args.no_browser)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"pytexmd-editor: error: {exc}\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
