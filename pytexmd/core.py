"""Core utilities for processing LaTeX files and generating documentation.

This module provides the main entry point for converting LaTeX files to Markdown and generating Sphinx documentation.
"""

__all__ = ["process_file"]

from .filter import process_string
from .file_loader import load_tex_file
from .sphinx_doc import create_sphinx_documentation,make_html


def process_file(
    input_file: str,
    output_folder: str,
    depth: int = 3,
    output_suffix: str = ".md",
    project_name: str = "My Project",
    author: str = "Author",
    version: str = "1.0"
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
    process_string(output_folder+"\\"+"source",file_string,depth,output_suffix)
    make_html(output_folder)
