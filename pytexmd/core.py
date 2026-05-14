"""Core utilities for processing LaTeX files and generating documentation.

This module provides the main entry point for converting LaTeX files to Markdown and generating Sphinx documentation.
"""

__all__ = ["process_file"]

import os
from .filter import process_string
from .file_loader import load_tex_file
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
) -> None:
    """Process a LaTeX file and generate documentation.

    Loads the LaTeX file, expands its content, generates Sphinx documentation, and converts the content to Markdown.

    Args:
        input_file (str): Path to the input LaTeX file.
        output_folder (str): Path to the output folder for documentation.
        depth (int, optional): Depth for processing sections. Defaults to 3.
        output_suffix (str, optional): Suffix for output files. Defaults to ".md".

    Returns:
        None

    Example:
        process_file("main.tex", "docs")
    """
    latex_content = load_tex_file(input_file)
    file_string = latex_content.content
    create_sphinx_documentation(output_folder,project_name,author,version)
    source_folder = os.path.join(output_folder, "source")
    # Copy merged bibliography to the Sphinx source directory
    if latex_content.merged_bib_content:
        bib_dest = os.path.join(source_folder, "references.bib")
        with open(bib_dest, "w", encoding="utf-8") as _f:
            _f.write(latex_content.merged_bib_content)
        print(f"Bibliography written to {bib_dest}")
    process_string(source_folder, file_string, depth, output_suffix)
    # Re-write conf.py now that custom theorem types are known.
    create_config_file(output_folder,project_name,author,version,custom_types=CUSTOM_THEOREM_TYPES)
    #make_html(output_folder)
