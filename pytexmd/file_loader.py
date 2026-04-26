r"""File loader utilities for LaTeX projects.

This module provides functions and classes to load LaTeX files and their associated resources
(recursively), such as .tex, .bib, and image files. It also expands \input{} commands in the main
LaTeX file.

Typical usage example:
    latex_file = load_tex_file("main.tex")
"""

__all__ = ["load_tex_file", "LatexFile"]

import os
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
    """
    content: str
    tex_files: Dict[str, str]
    bib_files: Dict[str, str]
    image_files: Dict[str, str]
    all_files: Dict[str, str]


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
        with open(file_name, 'r') as f:
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
            return load_file(filename)
        except (KeyError, FileNotFoundError) as exc:
            print(f"File not found for input: {input_name} ({exc})")
            return ""
    # Search for \input{filename} patterns in the content
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
    out = {"content": content, "tex_files": _tex_files, "bib_files": _bib_files, "image_files": _image_files, "all_files": all_files}
    return LatexFile(**out)

