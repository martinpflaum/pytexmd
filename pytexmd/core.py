"""Core utilities for processing LaTeX files and generating documentation.

This module provides the main entry point for converting LaTeX files to Markdown and generating Sphinx documentation.
"""

__all__ = ["process_file"]

import os
from .filter import process_string
from .file_loader import load_tex_file, convert_bbl_to_bib
from .sphinx_doc import create_sphinx_documentation, make_html, create_config_file
from .filter.splitting import split_rename
from .filter.text import CUSTOM_THEOREM_TYPES

def process_file(
    input_file: str,
    output_folder: str,
    depth: int = 3,
    output_suffix: str = ".md",
    project_name: str = "My Project",
    author: str = "Author",
    version: str = "1.0",
    mathjax_macros: dict = None,
) -> None:
    """Process a LaTeX file and generate documentation.

    Loads the LaTeX file, expands its content, generates Sphinx documentation, and converts the content to Markdown.

    Args:
        input_file (str): Path to the input LaTeX file.
        output_folder (str): Path to the output folder for documentation.
        depth (int, optional): Depth for processing sections. Defaults to 3.
        output_suffix (str, optional): Suffix for output files. Defaults to ".md".
        mathjax_macros (dict, optional): MathJax macro definitions for conf.py.

    Returns:
        None

    Example:
        process_file("main.tex", "docs")
    """
    latex_content = load_tex_file(input_file)
    file_string = latex_content.content
    create_sphinx_documentation(output_folder,project_name,author,version)
    source_folder = os.path.join(output_folder, "source")

    # Copy every .bib file found in the project directly to the Sphinx
    # source folder. For .bbl files (compiled bibliography output), convert
    # them to .bib format first so sphinxcontrib.bibtex can parse them.
    import shutil
    copied_bib_names: list[str] = []
    for abs_path in latex_content.bib_files.values():
        ext = os.path.splitext(abs_path)[1].lower()
        if ext == '.bbl':
            # Convert \begin{thebibliography} format → BibTeX database format
            dest_name = os.path.splitext(os.path.basename(abs_path))[0] + '.bib'
            dest = os.path.join(source_folder, dest_name)
            try:
                with open(abs_path, 'r', encoding='utf-8', errors='replace') as f:
                    bbl_content = f.read()
                bib_content = convert_bbl_to_bib(bbl_content)
                with open(dest, 'w', encoding='utf-8') as f:
                    f.write(bib_content)
                copied_bib_names.append(dest_name)
                print(f"Bibliography converted .bbl -> .bib: {dest}")
            except OSError as exc:
                print(f"Warning: could not convert {abs_path}: {exc}")
        else:
            dest = os.path.join(source_folder, os.path.basename(abs_path))
            try:
                shutil.copy2(abs_path, dest)
                copied_bib_names.append(os.path.basename(abs_path))
                print(f"Bibliography file copied: {dest}")
            except OSError as exc:
                print(f"Warning: could not copy {abs_path}: {exc}")

    process_string(source_folder, file_string, depth, output_suffix)
    # Re-write conf.py now that custom theorem types are known.
    create_config_file(output_folder, project_name, author, version,
                       custom_types=CUSTOM_THEOREM_TYPES,
                       bib_filenames=copied_bib_names,
                       mathjax_macros=mathjax_macros)
    #make_html(output_folder)
