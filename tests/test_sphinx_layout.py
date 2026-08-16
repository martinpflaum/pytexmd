import tempfile
import unittest
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
    def test_repeated_unnumbered_proofs_do_not_break_page_layout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            create_config_file(
                str(root),
                "Layout Test",
                "Author",
                "1.0",
                custom_types={
                    "paragraph": "Paragraph",
                    "theorem_and_definition": "Theorem and Definition",
                },
            )
            source = root / "source"
            (source / "_static").mkdir()
            (source / "references.bib").write_text("", encoding="utf-8")
            (source / "index.md").write_text(
                """# Page

:::{prf:paragraph}
:nonumber:

First block.
:::

:::{prf:proposition}
:nonumber:

Second block.
:::

:::{prf:theorem_and_definition}
:nonumber:

Custom block.
:::

::::{prf:paragraph}
:nonumber:

Block containing display math.

:::{math}
x = 1
:::
::::

:::{prf:theorem_and_definition}
:nonumber:

Second custom block.
:::

:::{prf:proof}

Proof content.
:::

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


if __name__ == "__main__":
    unittest.main()
