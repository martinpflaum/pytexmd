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
        None

    Returns:
        None

    Example:
        python -m pytexmd.cli main.tex output_folder --file_depth 3
    """
    parser = argparse.ArgumentParser(description="My Library CLI")
    parser.add_argument("filename", help="File to process",type=str)
    parser.add_argument("output_folder", help="File to process",type=str)
    parser.add_argument("--file_depth", help="How many sub files should be created according to sections and paragraphs etc..", default=3,type=int)
    args = parser.parse_args()
    print(f"Processing {args.filename}")
    process_file(args.filename,args.output_folder,args.file_depth)

if __name__ == "__main__":
    main()