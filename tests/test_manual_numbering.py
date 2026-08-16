import tempfile
import unittest
from pathlib import Path

from pytexmd.filter import core
from pytexmd.filter.core import Document, Undefined
from pytexmd.filter.equations import DefaultEquation, DefaultEquationSearcher
from pytexmd.filter.file_maker import write_section_files
from pytexmd.filter.text import TheoremElement, TheoremSearcher, get_theoremSearchers


class ManualNumberingTests(unittest.TestCase):
    def setUp(self):
        core.LABEL_TO_LABEL_TYPE.clear()
        core.LABEL_TO_RENAME.clear()
        core.USED_LABELS.clear()

    def test_theorem_is_not_automatically_numbered(self):
        searcher = TheoremSearcher("theorem", None, "Theorem")
        _, theorem, _ = searcher.split_and_create(
            r"\begin{theorem}[2.7]Content\end{theorem}", Document("", None)
        )
        theorem._finish_up()

        output = theorem.to_string()

        self.assertIn("{admonition} Theorem 2.7", output)
        self.assertIn(":class: pytexmd-admonition theorem", output)
        self.assertNotIn("dropdown", output)

    def test_equation_uses_only_explicit_tag(self):
        searcher = DefaultEquationSearcher(r"\begin{equation}", r"\end{equation}")
        _, equation, _ = searcher.split_and_create(
            r"\begin{equation}x=1\tag{A}\end{equation}", Document("", None)
        )
        equation._finish_up()

        output = equation.to_string()

        self.assertIn(r"\tag{A}", output)
        self.assertNotIn(":label:", output)
        self.assertNotIn("unamed_label", output)

    def test_equation_label_is_an_anchor_not_a_number_request(self):
        searcher = DefaultEquationSearcher(r"\begin{equation}", r"\end{equation}")
        _, equation, _ = searcher.split_and_create(
            r"\begin{equation}x=1\label{eq:x}\end{equation}", Document("", None)
        )
        equation._finish_up()

        output = equation.to_string()

        self.assertIn("(eq:x_0)=", output)
        self.assertNotIn(":label:", output)

    def test_eqref_uses_the_handwritten_tag(self):
        searcher = DefaultEquationSearcher(r"\begin{equation}", r"\end{equation}")
        _, equation, _ = searcher.split_and_create(
            r"\begin{equation}x=1\tag{A.3}\label{eq:x}\end{equation}",
            Document("", None),
        )
        equation._finish_up()

        self.assertEqual(core.ref_call("eq:x"), "[(A.3)](#eq:x_0)")

    def test_starred_newtheorem_declaration_is_supported(self):
        searchers = get_theoremSearchers(r"\newtheorem*{claim}{Claim}")

        self.assertEqual(len(searchers), 1)
        self.assertEqual(searchers[0].theorem_env_name, "claim")

    def test_generated_toctree_is_not_numbered(self):
        root = {
            "command": "document",
            "name": "index",
            "level": -1,
            "content": "",
            "children": [
                {"command": r"\section", "name": "1 First", "level": 2,
                 "content": "## 1 First", "children": []},
                {"command": r"\section", "name": "4 Second", "level": 2,
                 "content": "## 4 Second", "children": []},
            ],
        }

        with tempfile.TemporaryDirectory() as output_dir:
            write_section_files(root, output_dir, max_depth=2)
            output = Path(output_dir, "index.md").read_text(encoding="utf-8")

        self.assertNotIn(":numbered:", output)
        self.assertIn("1_first", output)
        self.assertIn("4_second", output)

    def test_theorem_fence_contains_nested_math_directive(self):
        document = Document("", None)
        theorem = TheoremElement(document, "Theorem", "theorem", None)
        theorem.children = [
            Undefined("", theorem),
            DefaultEquation("x = 1", theorem, r"\begin{equation}", r"\end{equation}"),
        ]

        theorem._finish_up()
        output = theorem.to_string()

        self.assertIn("::::{admonition} Theorem", output)
        self.assertIn(":class: pytexmd-admonition theorem", output)
        self.assertIn(":::{math}\nx = 1\n:::", output)
        self.assertTrue(output.rstrip().endswith("::::"))


if __name__ == "__main__":
    unittest.main()
