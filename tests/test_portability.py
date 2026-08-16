import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

from app.PytexmdConverter import gui
from app.PytexmdEditor import editor
from pytexmd.filter.file_maker import string_to_filename


class CrossPlatformPathTests(unittest.TestCase):
    def _project(self, root: Path) -> None:
        source = root / "source"
        html = root / "build" / "html"
        source.mkdir(parents=True)
        html.mkdir(parents=True)
        (source / "conf.py").write_text("", encoding="utf-8")
        (source / "index.md").write_text("# Home\n", encoding="utf-8")
        (html / "index.html").write_text("home", encoding="utf-8")

    def test_project_root_may_be_named_source_or_html(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            for name in ("source", "html"):
                root = parent / name
                self._project(root)
                project = editor.SphinxProject(root)
                self.assertEqual(project.root, root.resolve())

    def test_source_and_built_html_directories_resolve_to_project(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._project(root)

            from_source = editor.SphinxProject(root / "source")
            from_html = editor.SphinxProject(root / "build" / "html")

            self.assertEqual(from_source.root, root.resolve())
            self.assertEqual(from_html.root, root.resolve())

    def test_symlinked_source_directory_uses_canonical_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "project"
            actual_source = parent / "actual-source"
            (root / "build" / "html").mkdir(parents=True)
            actual_source.mkdir()
            (actual_source / "conf.py").write_text("", encoding="utf-8")
            (actual_source / "index.md").write_text("# Home\n", encoding="utf-8")
            try:
                (root / "source").symlink_to(actual_source, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"Directory symlinks are unavailable: {exc}")

            project = editor.SphinxProject(root)

            self.assertEqual(project.source, actual_source.resolve())
            self.assertEqual(project.read_page("index.md")["path"], "index.md")

    def test_toctree_backslashes_normalize_to_posix_document_names(self):
        markdown = """```{toctree}
chapters\\intro
```
"""
        entries = editor._toctree_entries(markdown, "index.md")
        self.assertEqual(entries[0].document, "chapters/intro.md")

    def test_windows_reserved_names_are_avoided_on_every_platform(self):
        self.assertEqual(string_to_filename("CON"), "section_con")
        self.assertEqual(string_to_filename("lpt1"), "section_lpt1")


class CrossPlatformStartupTests(unittest.TestCase):
    @unittest.skipIf(gui.tk is None, "Tkinter is not installed")
    def test_converter_has_clear_headless_linux_error(self):
        with (
            patch.object(gui.tk, "Tk", side_effect=gui.tk.TclError("no display")),
            self.assertRaisesRegex(SystemExit, "graphical display"),
        ):
            gui.main()

    def test_editor_reports_socket_startup_errors(self):
        errors = io.StringIO()
        with (
            patch.object(sys, "argv", ["pytexmd-editor", "project"]),
            patch.object(
                editor, "launch_editor", side_effect=OSError("socket unavailable")
            ),
            redirect_stderr(errors),
            self.assertRaises(SystemExit),
        ):
            editor.main()
        self.assertIn("socket unavailable", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
