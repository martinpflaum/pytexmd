import sys
import tempfile
import threading
import types
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.request import urlopen

from app.PytexmdEditor.editor import (
    SphinxProject,
    apply_visual_changes,
    choose_project_path,
    launch_editor,
    parse_editable_blocks,
)

SAMPLE_MARKDOWN = r"""# Original heading

Original paragraph.

:::{prf:theorem} Original title
:nonumber:

Theorem body.
:::

:::{math}
:label: equation-one

x = 1 \tag{1}
:::

```{tikz}
\draw (0,0) -- (1,1);
```
"""


class EditorRoundTripTests(unittest.TestCase):
    def test_parser_exposes_structured_editable_content(self):
        elements = {
            (block.kind, block.index): block.value
            for block in parse_editable_blocks(SAMPLE_MARKDOWN)
        }

        self.assertEqual(elements[("heading", 0)], "Original heading")
        self.assertEqual(elements[("paragraph", 0)], "Original paragraph.")
        self.assertEqual(elements[("directive_title", 0)], "Original title")
        self.assertIn("prf:theorem", elements[("admonition", 0)])
        self.assertEqual(elements[("equation", 0)], r"x = 1 \tag{1}")
        self.assertEqual(elements[("tikz_scale", 0)], "1")

    def test_visual_changes_round_trip_to_myst(self):
        updated = apply_visual_changes(
            SAMPLE_MARKDOWN,
            [
                {"kind": "heading", "index": 0, "value": "Edited heading"},
                {"kind": "paragraph", "index": 0, "value": "Edited paragraph."},
                {"kind": "directive_title", "index": 0, "value": "Edited title"},
                {"kind": "equation", "index": 0, "value": r"y = 2 \tag{2}"},
                {"kind": "tikz_scale", "index": 0, "value": "0.65"},
            ],
        )

        self.assertIn("# Edited heading", updated)
        self.assertIn("Edited paragraph.", updated)
        self.assertIn(":::{prf:theorem} Edited title", updated)
        self.assertIn(r"y = 2 \tag{2}", updated)
        self.assertIn(":label: equation-one", updated)
        self.assertIn(":xscale: 0.65", updated)
        self.assertIn(r"\draw (0,0) -- (1,1);", updated)

    def test_whole_admonitions_and_lists_are_editable(self):
        markdown = """# Page

:::{prf:proof} Details
:label: proof-label

Proof body.
:::

- First
- Second

Custom A
: Alpha
Custom B
: Beta

1.
: First enumerated item
2.
: Second enumerated item
"""
        blocks = parse_editable_blocks(markdown)
        elements = {(block.kind, block.index): block.value for block in blocks}
        list_blocks = [block for block in blocks if block.kind == "list"]

        self.assertIn(":label: proof-label", elements[("admonition", 0)])
        self.assertEqual(elements[("list", 0)], "- First\n- Second")
        self.assertEqual(elements[("list", 1)], "Custom A\n: Alpha\nCustom B\n: Beta")
        self.assertEqual(list_blocks[0].metadata["style"], "bullet")
        self.assertEqual(list_blocks[1].metadata["style"], "custom_enumeration")
        self.assertEqual(list_blocks[2].metadata["style"], "enumeration")

        updated = apply_visual_changes(
            markdown,
            [
                {
                    "kind": "admonition",
                    "index": 0,
                    "value": ":::{prf:proof} Revised\n:label: revised-proof\n\nNew proof.\n:::",
                },
                {"kind": "list", "index": 0, "value": "- One\n- Two"},
            ],
        )
        self.assertIn(":label: revised-proof", updated)
        self.assertIn("- One\n- Two", updated)

    def test_overlapping_admonition_and_child_edits_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Overlapping visual edits"):
            apply_visual_changes(
                SAMPLE_MARKDOWN,
                [
                    {
                        "kind": "admonition",
                        "index": 0,
                        "value": ":::{prf:theorem} Replacement\n:::",
                    },
                    {"kind": "directive_title", "index": 0, "value": "Title"},
                ],
            )

    def test_stale_and_duplicate_visual_edits_have_distinct_errors(self):
        with self.assertRaisesRegex(ValueError, "no longer mapped"):
            apply_visual_changes(
                SAMPLE_MARKDOWN,
                [{"kind": "directive_title", "index": 99, "value": "Stale"}],
            )

        with self.assertRaisesRegex(ValueError, "Duplicate editable element"):
            apply_visual_changes(
                SAMPLE_MARKDOWN,
                [
                    {"kind": "heading", "index": 0, "value": "First"},
                    {"kind": "heading", "index": 0, "value": "Second"},
                ],
            )

    def test_project_chooser_returns_selected_directory(self):
        tkinter = types.ModuleType("tkinter")
        filedialog = types.ModuleType("tkinter.filedialog")
        tkinter_root = MagicMock()
        tkinter.Tk = tkinter_root
        tkinter.TclError = RuntimeError
        tkinter.filedialog = filedialog
        filedialog.askdirectory = MagicMock(return_value="C:/project")
        with patch.dict(
            sys.modules,
            {"tkinter": tkinter, "tkinter.filedialog": filedialog},
        ):
            selected = choose_project_path()

        self.assertEqual(selected, "C:/project")
        tkinter_root.return_value.withdraw.assert_called_once_with()
        tkinter_root.return_value.destroy.assert_called_once_with()

    def test_project_saves_source_with_backup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "conf.py").write_text("project = 'Test'\n", encoding="utf-8")
            page = source / "index.md"
            page.write_text(SAMPLE_MARKDOWN, encoding="utf-8")
            project = SphinxProject(root)

            project.save_source("index.md", "# Replacement\n", rebuild=False)

            self.assertEqual(page.read_text(encoding="utf-8"), "# Replacement\n")
            backups = list((root / ".pytexmd-editor" / "backups").rglob("index.md"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), SAMPLE_MARKDOWN)

    def test_project_rejects_paths_outside_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "conf.py").write_text("", encoding="utf-8")
            project = SphinxProject(root)

            with self.assertRaises(ValueError):
                project.read_page("../outside.md")

    def test_page_management_updates_real_toctree_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "conf.py").write_text("", encoding="utf-8")
            (source / "index.md").write_text(
                """# Home

```{toctree}
:maxdepth: 2

chapter
references
```
""",
                encoding="utf-8",
            )
            (source / "chapter.md").write_text("# Chapter\n", encoding="utf-8")
            (source / "references.md").write_text("# References\n", encoding="utf-8")
            project = SphinxProject(root)

            with patch.object(project, "build", return_value="built"):
                relative, _ = project.create_page("New Results")
                project.move_page(relative, "up")

            index = (source / "index.md").read_text(encoding="utf-8")
            self.assertLess(index.index("new_results"), index.index("chapter"))
            self.assertLess(index.index("chapter"), index.index("references"))
            self.assertEqual(
                [page["path"] for page in project.pages()],
                ["index.md", "new_results.md", "chapter.md", "references.md"],
            )

            with patch.object(project, "build", return_value="built"):
                project.delete_page(relative)

            self.assertFalse((source / relative).exists())
            self.assertNotIn(
                "new_results", (source / "index.md").read_text(encoding="utf-8")
            )
            self.assertTrue(
                list((root / ".pytexmd-editor" / "backups").rglob(relative))
            )

    def test_required_pages_cannot_be_deleted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "conf.py").write_text("", encoding="utf-8")
            (source / "index.md").write_text("# Home\n", encoding="utf-8")
            project = SphinxProject(root)

            with self.assertRaises(ValueError):
                project.delete_page("index.md")

    def test_editor_server_serves_project_and_editable_preview(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            html = root / "build" / "html"
            source.mkdir()
            html.mkdir(parents=True)
            (source / "conf.py").write_text("", encoding="utf-8")
            (source / "index.md").write_text("# Page\n", encoding="utf-8")
            (html / "index.html").write_text(
                "<html><body><main><article><h1>Page</h1></article></main></body></html>",
                encoding="utf-8",
            )
            server = launch_editor(root, open_browser=False)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()

            try:
                with urlopen(server.editor_url + "api/project") as response:
                    project_payload = response.read().decode("utf-8")
                with urlopen(server.editor_url + "preview/index.html") as response:
                    preview = response.read().decode("utf-8")
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=2)

            self.assertIn('"path": "index.md"', project_payload)
            self.assertIn("pytexmd-select", preview)


if __name__ == "__main__":
    unittest.main()
