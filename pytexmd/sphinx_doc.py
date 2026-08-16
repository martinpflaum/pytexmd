"""Create and build the Sphinx project used by pytexmd."""

import ast
import os
import time
from pathlib import Path
from pprint import pformat
from typing import Optional

from sphinx.cmd.build import main as sphinx_build
from sphinx.cmd.quickstart import main as sphinx_quickstart


DEFAULT_MATHJAX_MACROS = {
    "ltortoise": r"\unicode{x3014}",
    "rtortoise": r"\unicode{x3015}",
    "ltsbrak": [r"\mathopen{\ltortoise\mspace{1mu}}", 0],
    "rtsbrak": [r"\mathopen{\mspace{1mu}\rtortoise}", 0],
    "mathbbm": [r"\mathbb{#1}", 1],
    "widebar": [r"\overline{#1}", 1],
    "C": r"\mathbb{C}",
    "H": r"\mathbb{H}",
}
_MATHJAX_TAGS_MARKER = "# PyTeXmd manual equation tags"


def _ensure_mathjax_manual_tags(source_dir: str | Path) -> None:
    """Enable manual ``\\tag`` rendering in older generated configurations."""
    config_path = Path(source_dir) / "conf.py"
    content = config_path.read_text(encoding="utf-8")
    if _MATHJAX_TAGS_MARKER in content:
        return
    try:
        tree = ast.parse(content)
        assignment = next(
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "mathjax3_config"
                for target in node.targets
            )
        )
        config = ast.literal_eval(assignment.value)
    except (StopIteration, SyntaxError, ValueError):
        return
    if "tags" in config.get("tex", {}):
        return
    config_path.write_text(
        content.rstrip()
        + "\n\n"
        + _MATHJAX_TAGS_MARKER
        + '\nmathjax3_config.setdefault("tex", {})["tags"] = "ams"\n',
        encoding="utf-8",
    )


def load_config_template() -> str:
    """Load the Sphinx configuration template."""
    template_path = Path(__file__).parent / "templates" / "conf.txt"
    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()


def create_config_file(
    output_dir: str,
    project_name: str,
    author: str,
    version: str,
    bib_filenames: list = None,
    mathjax_macros: dict = None,
) -> None:
    """Create the Sphinx ``conf.py`` in the source directory."""
    try:
        source_dir = Path(output_dir) / "source"
        source_dir.mkdir(parents=True, exist_ok=True)
        config_path = source_dir / "conf.py"

        config_content = (
            load_config_template()
            .replace("XXPROJECTXX", repr(project_name))
            .replace("XXAUTHORSXX", repr(author))
            .replace("XXRELEASEXX", repr(version))
            .replace(
                "XXMATHJAXMACROSXX",
                pformat(
                    mathjax_macros
                    if mathjax_macros is not None
                    else DEFAULT_MATHJAX_MACROS,
                    sort_dicts=False,
                ),
            )
        )

        bib_list = bib_filenames if bib_filenames else ["references.bib"]
        config_content = config_content.replace(
            "bibtex_bibfiles = ['references.bib']",
            f"bibtex_bibfiles = {bib_list!r}",
        )

        with open(config_path, "w", encoding="utf-8") as file:
            file.write(config_content)

        print(f"Configuration file created at {config_path}")
    except Exception as exc:
        print(f"An error occurred while creating the configuration file: {exc}")


def create_sphinx_documentation(
    output_dir: str,
    project_name: str = "My Project",
    author: str = "Author",
    version: str = "1.0",
) -> None:
    """Create a Sphinx documentation structure with source and build folders."""
    if os.path.exists(output_dir) and os.path.exists(
        os.path.join(output_dir, "Makefile")
    ):
        print(f"Sphinx documentation already exists at {output_dir}. Skipping creation.")
        return

    output_dir = os.path.abspath(output_dir)
    sphinx_quickstart(
        [
            output_dir,
            "--release",
            version,
            "--sep",
            "--project",
            project_name,
            "--author",
            author,
            "--makefile",
            "--batchfile",
            "--language",
            "en",
        ]
    )

    print("waiting 0.5 seconds to let the file system catch up")
    time.sleep(0.5)

    try:
        index_rst_path = Path(output_dir) / "source" / "index.rst"
        if index_rst_path.exists():
            index_rst_path.unlink()
            print(f"Deleted auto-generated index.rst file at {index_rst_path}")
    except Exception as exc:
        print(f"Warning: Could not delete index.rst: {exc}")

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    create_config_file(output_dir, project_name, author, version)


def make_html(output_dir: str, raise_on_error: bool = False) -> Optional[Path]:
    """Build the Sphinx documentation to HTML format."""
    try:
        source_dir = os.path.join(output_dir, "source")
        build_dir = os.path.join(output_dir, "build")
        _ensure_mathjax_manual_tags(source_dir)
        result = sphinx_build(["-M", "html", source_dir, build_dir])
        if result != 0:
            raise RuntimeError(f"Sphinx HTML build failed with exit code {result}")
        print(f"Sphinx documentation built successfully at {build_dir}")
        return Path(build_dir) / "html"
    except Exception as exc:
        print(f"An error occurred while building the documentation: {exc}")
        if raise_on_error:
            raise
        return None
