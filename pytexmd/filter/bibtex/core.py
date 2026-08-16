"""BibTeX filters for converting .bbl files to .bib format.

These Element subclasses parse \\begin{thebibliography}...\\end{thebibliography}
content and produce BibTeX .bib output via to_string().

Hierarchy:
    TheBibliography  →  BibItem  →  NewBlock  →  EmphText
"""

__all__ = ["TheBibliography", "BibItem", "NewBlock", "EmphText", "convert_bbl_to_bib"]

import re
from typing import List, Optional, Tuple

from ..core import Element, Undefined
from ..splitting import (
    split_on_first_brace,
    split_on_next,
    begin_end_split,
    position_of,
)


def _clean(text: str) -> str:
    """Strip LaTeX markup, leaving plain text suitable for a .bib field value."""
    # Iteratively unwrap nested braces: {text} → text
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r'\{([^{}]*)\}', r'\1', text)
    # Remove LaTeX commands (e.g. \em, \textbf, \protect)
    text = re.sub(r'\\[a-zA-Z]+\*?', ' ', text)
    # Remove remaining lone backslashes
    text = text.replace('\\', '')
    return re.sub(r'\s+', ' ', text).strip()


class EmphText(Element):
    r"""Leaf element for {\em ...} or {\it ...}.

    Uses split_on_first_brace for brace-balanced extraction so titles like
    ``{\em General topology. {C}hapters 1--4}`` are not truncated at the
    first inner ``}``.
    """

    def __init__(self, inner: str, parent: Optional[Element]):
        super().__init__("", parent)
        self._inner = inner

    @staticmethod
    def position(input: str) -> int:
        best = -1
        for marker in ('{\\em ', '{\\it '):
            idx = input.find(marker)
            if idx != -1 and (best == -1 or idx < best):
                best = idx
        return best

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, "EmphText", str]:
        em_start = -1
        for marker in ('{\\em ', '{\\it '):
            idx = input.find(marker)
            if idx != -1 and (em_start == -1 or idx < em_start):
                em_start = idx
        pre = input[:em_start]
        inner, post = split_on_first_brace(input[em_start:])
        inner = re.sub(r'^\\(?:em|it)\s*', '', inner)
        return pre, EmphText(inner, parent), post

    def to_string(self) -> str:
        return _clean(self._inner)

    def _finish_up(self) -> None:
        pass  # leaf — no children to recurse into


class NewBlock(Element):
    r"""Element for one \newblock section inside a bibitem body.

    Expands its content into EmphText children so that italicised book titles
    are extracted with correct brace depth.
    """

    def __init__(self, content: str, parent: Optional[Element]):
        super().__init__(content, parent)
        self._raw = content  # preserved for plain_text()

    @staticmethod
    def position(input: str) -> int:
        return position_of(input, '\\newblock')

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, "NewBlock", str]:
        pre, rest = split_on_next(input, '\\newblock')
        if '\\newblock' in rest:
            content, post = split_on_next(rest, '\\newblock')
            post = '\\newblock' + post
        else:
            content, post = rest, ''
        elem = NewBlock(content.strip(), parent)
        elem.expand([EmphText])
        return pre, elem, post

    def has_emph(self) -> bool:
        """True if this block contains an EmphText child."""
        return any(isinstance(c, EmphText) for c in (self.children or []))

    def emph_text(self) -> str:
        """Return text of the first EmphText child, or ''."""
        for c in (self.children or []):
            if isinstance(c, EmphText):
                return c.to_string()
        return ''

    def plain_text(self) -> str:
        """Return clean plain text of the whole block (LaTeX stripped)."""
        return _clean(self._raw)

    def to_string(self) -> str:
        if self.children:
            parts = []
            for c in self.children:
                if isinstance(c, EmphText):
                    parts.append(c.to_string())
                else:
                    # Undefined child — raw text captured before/after EmphText
                    parts.append(c._modifiable_content)
            return ''.join(parts)
        return self._raw

    def _finish_up(self) -> None:
        pass  # expand() already set up children


class BibItem(Element):
    r"""Element for a single \bibitem entry.

    Parses the citation key and preamble (author + year) at creation time,
    then expands the body into NewBlock children.  to_string() renders a
    @misc BibTeX record.
    """

    def __init__(self, key: str, body: str, parent: Optional[Element]):
        super().__init__(body, parent)
        self.key = key
        # Parse author + year from the preamble (text before first \newblock)
        preamble = re.split(r'\\newblock\b', body, maxsplit=1)[0].strip()
        year_m = re.search(r'\((\d{4}[a-z]?)\)', preamble)
        self._year = year_m.group(1) if year_m else ''
        author_raw = re.sub(r'\s*\(\d{4}[a-z]?\)\.?\s*$', '', preamble).strip().rstrip('.,')
        self._author = _clean(author_raw)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input, '\\bibitem')

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, "BibItem", str]:
        pre, rest = split_on_next(input, '\\bibitem')
        rest = rest.lstrip()
        # Skip optional \bibitem[label]{key} cite-label
        if rest.startswith('['):
            _, rest = split_on_first_brace(rest, '[', ']')
        # Extract citation key from {key}
        key, rest = split_on_first_brace(rest)
        # Body runs until the next \bibitem or end of string
        if '\\bibitem' in rest:
            body, post = split_on_next(rest, '\\bibitem')
            post = '\\bibitem' + post
        else:
            body, post = rest, ''
        elem = BibItem(key.strip(), body.strip(), parent)
        elem.expand([NewBlock])
        return pre, elem, post

    def to_string(self) -> str:
        """Render as a @misc BibTeX entry."""
        newblocks: List[NewBlock] = [
            c for c in (self.children or []) if isinstance(c, NewBlock)
        ]
        title = ''
        if newblocks:
            first = newblocks[0]
            if first.has_emph():
                title = first.emph_text()
            else:
                title = first.plain_text().rstrip('.')

        lines = [f'@misc{{{self.key},']
        if self._author:
            lines.append(f'  author = {{{self._author}}},')
        if title:
            lines.append(f'  title = {{{title}}},')
        if self._year:
            lines.append(f'  year = {{{self._year}}},')
        lines.append('}')
        return '\n'.join(lines)

    def _finish_up(self) -> None:
        pass  # expand() already set up children


class TheBibliography(Element):
    r"""Top-level element for \begin{thebibliography}...\end{thebibliography}.

    Expands its content into BibItem children and renders the full .bib output.
    """

    def __init__(self, content: str, parent: Optional[Element]):
        super().__init__(content, parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input, '\\begin{thebibliography}')

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, "TheBibliography", str]:
        pre, content, post = begin_end_split(
            input, '\\begin{thebibliography}', '\\end{thebibliography}'
        )
        # Drop the mandatory {N} argument that follows \begin{thebibliography}
        content = re.sub(r'^\s*\{[^}]*\}', '', content).strip()
        elem = TheBibliography(content, parent)
        elem.expand([BibItem])
        return pre, elem, post

    def to_string(self) -> str:
        entries = [
            c.to_string()
            for c in (self.children or [])
            if isinstance(c, BibItem)
        ]
        return '\n\n'.join(entries)

    def _finish_up(self) -> None:
        pass  # expand() already set up children


def convert_bbl_to_bib(bbl_content: str) -> str:
    """Convert .bbl content to .bib format using the filter element pipeline.

    Args:
        bbl_content: Raw content of a .bbl file containing
            ``\\begin{thebibliography}...\\end{thebibliography}``.

    Returns:
        BibTeX .bib database string with one ``@misc`` entry per bibitem.
    """
    wrapper = Undefined(bbl_content, None)
    wrapper.expand([TheBibliography])
    for child in (wrapper.children or []):
        if isinstance(child, TheBibliography):
            return child.to_string()
    return ''
