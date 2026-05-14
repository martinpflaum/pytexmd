r"""File loader utilities for LaTeX projects.

This module provides functions and classes to load LaTeX files and their associated resources
(recursively), such as .tex, .bib, and image files. It also expands \input{} commands in the main
LaTeX file.

Typical usage example:
    latex_file = load_tex_file("main.tex")
"""

__all__ = ["load_tex_file", "LatexFile", "merge_bib_files"]

import os
import re
import regex
from typing import List, Dict, Tuple, Optional, Any, NamedTuple

class LatexFile(NamedTuple):
    r"""Container for loaded LaTeX project files.

    Attributes:
        content (str): The expanded content of the main LaTeX file, with \input{} resolved.
        tex_files (Dict[str, str]): Mapping from base filename (without extension) to absolute path for .tex/.sty/.cls files.
        bib_files (Dict[str, str]): Mapping from base filename (without extension) to absolute path for .bib/.bbl/.bibtex/.biblatex files.
        image_files (Dict[str, str]): Mapping from base filename (without extension) to absolute path for image files.
        all_files (Dict[str, str]): Combined mapping of all supported files.
        merged_bib_content (str): Merged and deduplicated content of all found .bib files.
    """
    content: str
    tex_files: Dict[str, str]
    bib_files: Dict[str, str]
    image_files: Dict[str, str]
    all_files: Dict[str, str]
    merged_bib_content: str = ""


def _split_bib_entries(content: str) -> List[str]:
    """Split .bib file content into individual top-level @-entries."""
    entries = []
    i = 0
    n = len(content)
    while i < n:
        if content[i] != '@':
            i += 1
            continue
        start = i
        while i < n and content[i] != '{':
            i += 1
        if i >= n:
            break
        depth = 1
        i += 1
        while i < n and depth > 0:
            if content[i] == '{':
                depth += 1
            elif content[i] == '}':
                depth -= 1
            i += 1
        entries.append(content[start:i])
    return entries


def _extract_bib_key(entry: str) -> Optional[str]:
    """Return the citation key from a bib entry, or None for @string/@preamble/@comment."""
    m = re.match(r'@(\w+)\s*\{\s*([^,\s}]+)', entry, re.IGNORECASE)
    if not m:
        return None
    if m.group(1).lower() in ('string', 'preamble', 'comment'):
        return None
    return m.group(2)


def merge_bib_files(bib_paths: List[str]) -> str:
    """Read and merge multiple .bib files, deduplicating entries by citation key.

    Args:
        bib_paths: List of absolute paths to .bib/.bbl files.

    Returns:
        str: Merged .bib content with duplicate entries removed (first occurrence wins).
    """
    seen_keys: set = set()
    merged: List[str] = []
    for bib_path in bib_paths:
        try:
            with open(bib_path, 'r', encoding='utf-8', errors='replace') as f:
                raw = f.read()
        except OSError as exc:
            print(f"Warning: could not read {bib_path}: {exc}")
            continue
        for entry in _split_bib_entries(raw):
            key = _extract_bib_key(entry)
            if key is None:
                merged.append(entry.strip())
            elif key not in seen_keys:
                seen_keys.add(key)
                merged.append(entry.strip())
    return "\n\n".join(e for e in merged if e)


def load_tex_file(file_name: str) -> LatexFile:
    r"""Load a LaTeX file and its associated resources recursively.

    Expands all \input{} commands in the main file, and collects all .tex, .bib, and image files
    in the same directory tree.

    Args:
        file_name (str): Path to the main LaTeX file.

    Returns:
        LatexFile: A named tuple containing the expanded content and dictionaries of found files.

    Raises:
        FileNotFoundError: If the main file does not exist.
        OSError: If there is an error reading files from disk.

    Example:
        latex_file = load_tex_file("main.tex")
        print(latex_file.content)
    """
    def load_file(file_name: str) -> str:
        r"""Read the contents of a file.

        Args:
            file_name (str): Path to the file.

        Returns:
            str: Contents of the file.
        """
        data = None
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()
        return data
    
    # Get the folder where file_name resides
    #folder_path = os.path.dirname(file_name)
    absolute_folder = os.path.dirname(os.path.abspath(file_name))

    # Get all image files, .bib files, and .tex files in the folder (recursively)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.pdf', '.eps']
    tex_extensions = [ '.tex', '.sty', '.cls']
    bib_extensions = ['.bib', '.bbl',".bibtex", '.biblatex']
    target_extensions = tex_extensions + image_extensions + bib_extensions

    all_files = []
    tex_files = []
    bib_files = []
    image_files = []

    if os.path.exists(absolute_folder):
        # Walk through all subdirectories recursively
        for root, dirs, files in os.walk(absolute_folder):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.abspath(file_path)
                file_ext = os.path.splitext(file)[1].lower()
                
                if file_ext in tex_extensions:
                    tex_files.append(relative_path)
                elif file_ext in bib_extensions:
                    bib_files.append(relative_path)
                elif file_ext in image_extensions:
                    image_files.append(relative_path)

    print(f"Folder (recursive): {absolute_folder}")
    print(f"TEX files: {tex_files}")
    print(f"BIB files: {bib_files}")
    print(f"Image files: {image_files}")

    content = load_file(file_name)

    def remove_extensions(file_name: str) -> str:
        """Strip a single trailing known extension from a basename."""
        root, ext = os.path.splitext(file_name)
        if ext.lower() in target_extensions:
            return root
        return file_name

    def _basename_key(abs_path: str) -> str:
        """Return the bare basename (no extension) used as dict key."""
        return remove_extensions(os.path.basename(abs_path))

    _tex_files = {_basename_key(f): f for f in tex_files}
    _bib_files = {_basename_key(f): f for f in bib_files}
    _image_files = {_basename_key(f): f for f in image_files}
    all_files = {**_tex_files, **_bib_files, **_image_files}

    def input_to_filename(input_name: str) -> str:
        r"""Convert LaTeX input name to absolute filename.

        Tries direct relative-path resolution first (handles paths like
        ``../sibling/file`` or ``sections/foo``), then falls back to a
        basename-only dict lookup for plain names like ``foo``.

        Args:
            input_name (str): Name from \input{} command.

        Returns:
            str: Absolute path to the file.

        Raises:
            FileNotFoundError: If no matching file can be located.
        """
        # Normalise separators so os.path works cross-platform
        norm = input_name.replace("\\", "/")

        # Strategy 1: resolve as a path relative to the project root
        candidate = os.path.normpath(os.path.join(absolute_folder, norm))
        if os.path.isfile(candidate):
            return candidate
        # Try appending each tex extension (LaTeX omits .tex in \input)
        for ext in tex_extensions:
            if os.path.isfile(candidate + ext):
                return candidate + ext

        # Strategy 2: bare-basename dict lookup (legacy fallback)
        bare = remove_extensions(norm.split("/")[-1])
        if bare in all_files:
            return all_files[bare]

        raise FileNotFoundError(
            f"Cannot resolve \\input{{{input_name}}}: tried '{candidate}' "
            f"and basename key '{bare}' in scanned files."
        )

    def get_input_file(input_name: str) -> str:
        r"""Get the contents of an input file referenced in LaTeX.

        Args:
            input_name (str): Name from \input{} command.

        Returns:
            str: Contents of the input file, or empty string if not found.
        """
        try:
            filename = input_to_filename(input_name)
            _resolved_input_dirs.add(os.path.dirname(os.path.abspath(filename)))
            return load_file(filename)
        except (KeyError, FileNotFoundError) as exc:
            print(f"File not found for input: {input_name} ({exc})")
            return ""
    # Search for \input{filename} patterns in the content
    _resolved_input_dirs: set = set()
    input_pattern = r'\\input\{([^}]+)\}'
    content_old = content
    done_matches = []

    while True:
        matches = regex.findall(input_pattern, content)
        for match in matches:
            if match in done_matches:
                continue
            content = content.replace(r"\input{"+match+"}", get_input_file(match))
            done_matches.append(match)
        if content == content_old:
            break
        content_old = content

    # Collect .bib files from directories outside the project root that were
    # touched by \input{} resolution (the initial os.walk already covers the
    # tree rooted at absolute_folder).
    for _d in _resolved_input_dirs:
        _d = os.path.normpath(_d)
        try:
            _rel = os.path.relpath(_d, absolute_folder)
            if not _rel.startswith('..'):
                continue  # already covered by the initial recursive walk
        except ValueError:
            pass  # different drive on Windows — definitely outside project root
        if os.path.isdir(_d):
            for _root, _dirs, _fls in os.walk(_d):
                for _fl in _fls:
                    if os.path.splitext(_fl)[1].lower() in bib_extensions:
                        _abs = os.path.abspath(os.path.join(_root, _fl))
                        if _abs not in bib_files:
                            bib_files.append(_abs)

    # Rebuild bib dict in case extra files were found
    _bib_files = {_basename_key(f): f for f in bib_files}
    all_files = {**_tex_files, **_bib_files, **_image_files}

    # Merge all collected .bib files, deduplicating by citation key
    merged_bib_content = merge_bib_files(bib_files)

    out = {"content": content, "tex_files": _tex_files, "bib_files": _bib_files, "image_files": _image_files, "all_files": all_files, "merged_bib_content": merged_bib_content}
    return LatexFile(**out)

