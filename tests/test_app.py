import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.PytexmdConverter.cli import generate_html


class HtmlApplicationTests(unittest.TestCase):
    def test_generate_html_runs_conversion_and_build(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            input_file = root / "main.tex"
            input_file.write_text(r"\documentclass{article}", encoding="utf-8")
            output_folder = root / "site"
            html_folder = output_folder / "build" / "html"
            html_folder.mkdir(parents=True)
            (html_folder / "index.html").write_text("site", encoding="utf-8")

            with (
                patch("app.PytexmdConverter.cli.process_file") as process,
                patch(
                    "app.PytexmdConverter.cli.make_html", return_value=html_folder
                ) as build,
            ):
                result = generate_html(
                    str(input_file),
                    str(output_folder),
                    project_name="Example",
                    author="Author",
                    version="2.0",
                    mathjax_macros={"R": r"\mathbb{R}"},
                )

        self.assertEqual(result, html_folder / "index.html")
        process.assert_called_once_with(
            str(input_file.resolve()),
            str(output_folder.resolve()),
            depth=3,
            project_name="Example",
            author="Author",
            version="2.0",
            mathjax_macros={"R": r"\mathbb{R}"},
        )
        build.assert_called_once_with(str(output_folder.resolve()), raise_on_error=True)

    def test_generate_html_rejects_missing_input(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaises(FileNotFoundError),
        ):
            generate_html(str(Path(directory) / "missing.tex"), directory)


if __name__ == "__main__":
    unittest.main()
