import tempfile
import unittest
from pathlib import Path

from app.PytexmdConverter.file_detection import detect_project_files


class ProjectFileDetectionTests(unittest.TestCase):
    def test_report_matches_recursive_inventory_and_input_rules(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            project = workspace / "project"
            external = workspace / "external"
            (project / "sections").mkdir(parents=True)
            external.mkdir()
            main = project / "main.tex"
            main.write_text(
                r"\input{sections/chapter}\input{../external/appendix}\input{missing}",
                encoding="utf-8",
            )
            (project / "sections" / "chapter.tex").write_text(
                r"\input{detail}", encoding="utf-8"
            )
            # Nested inputs are resolved from the main project root.
            (project / "detail.tex").write_text("detail", encoding="utf-8")
            (project / "references.bib").write_text("", encoding="utf-8")
            (project / "figure.svg").write_text("<svg/>", encoding="utf-8")
            (external / "appendix.tex").write_text("appendix", encoding="utf-8")
            (external / "external.bib").write_text("", encoding="utf-8")

            report = detect_project_files(main)

        detected = {item.path.name: item for item in report.files}
        self.assertTrue(report.root.is_absolute())
        self.assertTrue(all(item.path.is_absolute() for item in report.files))
        self.assertIn("main.tex", detected)
        self.assertIn("chapter.tex", detected)
        self.assertIn("detail.tex", detected)
        self.assertIn("references.bib", detected)
        self.assertIn("figure.svg", detected)
        self.assertIn("appendix.tex", detected)
        self.assertIn("external.bib", detected)
        self.assertIn(
            r"resolved from \input{sections/chapter}",
            detected["chapter.tex"].mechanisms,
        )
        self.assertIn(
            "bibliography scan beside external input",
            detected["external.bib"].mechanisms,
        )
        self.assertEqual(report.missing_inputs, ("missing",))

    def test_report_identifies_bare_basename_collisions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            main = root / "main.tex"
            main.write_text("", encoding="utf-8")
            (root / "asset.png").write_bytes(b"png")
            (root / "asset.pdf").write_bytes(b"pdf")

            report = detect_project_files(main)

        self.assertEqual(len(report.collisions), 1)
        self.assertIn("asset:", report.collisions[0])


if __name__ == "__main__":
    unittest.main()
