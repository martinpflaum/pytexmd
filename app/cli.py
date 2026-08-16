"""Command-line application for generating a complete HTML documentation site."""

import argparse
import json
from pathlib import Path
import webbrowser

from pytexmd.core import process_file
from pytexmd.sphinx_doc import make_html


def generate_html(
    input_file: str,
    output_folder: str,
    depth: int = 3,
    project_name: str = "My Project",
    author: str = "Author",
    version: str = "1.0",
    mathjax_macros: dict | None = None,
) -> Path:
    """Convert a LaTeX project to MyST sources and a Sphinx HTML site."""
    input_path = Path(input_file).expanduser().resolve()
    if not input_path.is_file():
        raise FileNotFoundError(f"LaTeX input file not found: {input_path}")

    output_path = Path(output_folder).expanduser().resolve()
    process_file(
        str(input_path),
        str(output_path),
        depth=depth,
        project_name=project_name,
        author=author,
        version=version,
        mathjax_macros=mathjax_macros,
    )
    html_directory = make_html(str(output_path), raise_on_error=True)
    index_path = html_directory / "index.html"
    if not index_path.is_file():
        raise RuntimeError(f"Sphinx did not generate {index_path}")
    return index_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a LaTeX project into a PyTeXmd/Furo HTML site."
    )
    parser.add_argument("input_file", help="Main LaTeX file, such as main.tex")
    parser.add_argument("output_folder", help="Destination Sphinx project folder")
    parser.add_argument("--depth", default=3, type=int, help="Section split depth")
    parser.add_argument("--project-name", default="My Project")
    parser.add_argument("--author", default="Author")
    parser.add_argument("--version", default="1.0")
    parser.add_argument(
        "--macros-file",
        type=Path,
        help="JSON file containing the MathJax macros object",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        dest="open_browser",
        help="Open the generated site in the default browser",
    )
    args = parser.parse_args()

    mathjax_macros = None
    if args.macros_file is not None:
        try:
            mathjax_macros = json.loads(args.macros_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            parser.exit(1, f"pytexmd-html: error: invalid macros file: {exc}\n")
        if not isinstance(mathjax_macros, dict):
            parser.exit(1, "pytexmd-html: error: macros file must contain a JSON object\n")

    try:
        index_path = generate_html(
            args.input_file,
            args.output_folder,
            depth=args.depth,
            project_name=args.project_name,
            author=args.author,
            version=args.version,
            mathjax_macros=mathjax_macros,
        )
    except (OSError, RuntimeError) as exc:
        parser.exit(1, f"pytexmd-html: error: {exc}\n")

    print(f"HTML site generated at: {index_path}")
    if args.open_browser:
        webbrowser.open(index_path.as_uri())


if __name__ == "__main__":
    main()
