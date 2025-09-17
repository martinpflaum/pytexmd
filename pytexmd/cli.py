"""Command-line interface for pytexmd.

This module provides a CLI for processing LaTeX files and generating documentation.
"""

__all__ = ['process_file']

from .core import process_file
import argparse

def main() -> None:
    """Main entry point for the CLI.

    Parses command-line arguments and processes the specified LaTeX file.

    Args:
        input_file (str): File to process.
        output_folder (str): Output folder.
        depth (int): How many sub files should be created according to sections and paragraphs etc.
        output_suffix (str): Suffix for output files.
        project_name (str): Project name.
        author (str): Author name.
        version (str): Version string.

    Returns:
        None

    Example:
        python -m pytexmd.cli main.tex output_folder --depth 3 --output_suffix .md --project_name "My Project" --author "Author" --version "1.0"
    """
    parser = argparse.ArgumentParser(description="My Library CLI")
    parser.add_argument("input_file", help="File to process", type=str)
    parser.add_argument("output_folder", help="Output folder", type=str)
    parser.add_argument("--depth", help="(not supported yet)How many sub files should be created according to sections and paragraphs etc.", default=0, type=int)
    parser.add_argument("--output_suffix", help="Suffix for output files", default=".md", type=str)
    parser.add_argument("--project_name", help="Project name", default="My Project", type=str)
    parser.add_argument("--author", help="Author name", default="Author", type=str)
    parser.add_argument("--version", help="Version string", default="1.0", type=str)
    args = parser.parse_args()
    print(f"Processing {args.input_file}")
    process_file(
        args.input_file,
        args.output_folder,
        args.depth,
        args.output_suffix,
        args.project_name,
        args.author,
        args.version
    )

if __name__ == "__main__":
    main()