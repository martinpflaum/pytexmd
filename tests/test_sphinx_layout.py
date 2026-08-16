import tempfile
import unittest
import ast
from html.parser import HTMLParser
from pathlib import Path

from sphinx.cmd.build import build_main

from pytexmd.sphinx_doc import create_config_file


class _DivBalanceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.open_divs = 0
        self.unmatched_closing_divs = 0

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.open_divs += 1

    def handle_endtag(self, tag):
        if tag != "div":
            return
        if self.open_divs:
            self.open_divs -= 1
        else:
            self.unmatched_closing_divs += 1


class SphinxLayoutTests(unittest.TestCase):
    def test_config_uses_supplied_mathjax_macros(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            macros = {"R": [r"\mathbb{#1}", 1]}

            create_config_file(
                str(root),
                "Macro's Test",
                "O'Brien",
                "1.0",
                mathjax_macros=macros,
            )

            module = ast.parse(
                (root / "source" / "conf.py").read_text(encoding="utf-8")
            )
            assignment = next(
                node
                for node in module.body
                if isinstance(node, ast.Assign)
                and any(
                    isinstance(target, ast.Name) and target.id == "mathjax3_config"
                    for target in node.targets
                )
            )
            self.assertEqual(
                ast.literal_eval(assignment.value)["tex"]["macros"], macros
            )

    def test_repeated_unnumbered_proofs_do_not_break_page_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_config_file(
                str(root),
                "Layout Test",
                "Author",
                "1.0",
            )
            source = root / "source"
            (source / "_static").mkdir()
            (source / "references.bib").write_text("", encoding="utf-8")
            (source / "index.md").write_text(
                """# Page

:::{admonition} Paragraph
:class: pytexmd-admonition paragraph

First block.
:::

:::{admonition} Proposition
:class: pytexmd-admonition proposition

Second block.
:::

:::{admonition} Theorem and Definition
:class: pytexmd-admonition theorem-and-definition

Custom block.
:::

::::{admonition} Paragraph
:class: pytexmd-admonition paragraph

Block containing display math.

:::{math}
x = 1
:::
::::

:::{admonition} Theorem and Definition
:class: pytexmd-admonition theorem-and-definition

Second custom block.
:::

:::{admonition} Proof
:class: pytexmd-admonition proof

Proof content.
:::

```{tikz}
\\draw[->] (0,0) -- (1,1);
```

```{tikz}
\\thiscommanddoesnotexist
```

Content after a failed TikZ render.
""",
                encoding="utf-8",
            )
            output = root / "build"

            result = build_main(["-b", "html", str(source), str(output)])
            self.assertEqual(result, 0)

            html = (output / "index.html").read_text(encoding="utf-8")
            parser = _DivBalanceParser()
            parser.feed(html)

        self.assertEqual(parser.unmatched_closing_divs, 0)
        self.assertEqual(parser.open_divs, 0)
        self.assertIn("Theorem and Definition", html)
        self.assertNotIn("Theorem_And_Definition", html)
        self.assertIn("Block containing display math.", html)
        self.assertIn("Second custom block.", html)
        self.assertIn("Content after a failed TikZ render.", html)
        self.assertIn("TikZ diagram source", html)
        self.assertIn("thiscommanddoesnotexist", html)
        if r"\draw[-&gt;]" not in html:
            self.assertRegex(html, r'<img [^>]*src="[^"]*tikz-[^"]+\.(?:png|svg)"')


if __name__ == "__main__":
    unittest.main()
