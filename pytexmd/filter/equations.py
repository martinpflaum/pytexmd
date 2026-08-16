#%%
"""Equation filter classes and utilities for pytexmd.

This module provides classes and functions for parsing and processing LaTeX equations,
environments, and math for Markdown/MyST conversion.
"""

__all__ = [
    "apply_latex_protection",
    "TexArray",
    "BeginEquationEnumElement",
    "BeginEquationEnumSearcher",
    "InlineLatex",
    "LatexText",
    "Cases",
    "DoubleDolarLatex",
    "BeginEquationElement",
    "BeginAlignStar",
    "BeginAlignSearcher",
    "get_all_filters",
    "MultiEquationElement",
]

#%%
#from drawtex import contains_drawtex,get_drawtex_searchers
from .splitting import *
from .core import *
from typing import List,Tuple,Union
from ..config import LATEX_REPLACEMENTS
import re as _re


def _handwritten_tag(content: str) -> str:
    r"""Return the value of a simple LaTeX ``\tag`` or ``\tag*`` command."""
    match = _re.search(r"\\tag\*?\s*\{([^{}]*)\}", content)
    return match.group(1).strip() if match else ""

class EquationLabel(Element):
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__("",parent)
        self.label = label_call(
            modifiable_content, LabelType.EQ, rename=parent.handwritten_tag
        )
        if self.label == "":
            self.label = "equation_label_error"
        parent.add_label(self.label)

    def to_string(self) -> str:
        return ""#"\\label{" + self.label + "}"
    
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\label")
    
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'EquationLabel', str]:
        pre,modifiable_content = split_on_next(string,"\\label",save_split=False)
        content,post = split_on_first_brace(modifiable_content,"{","}")
        out = EquationLabel(content,parent)
        return pre,out,post

def apply_latex_protection(string: Element) -> Element:
    """Expands and protects LaTeX environments and commands in the given element.

    Args:
        string (Element): The element to process.

    Returns:
        Element: The processed element.
    """
    multiline = ["split", "multline","align","breqn","equation"]
    
    #expandon = [JunkSearch("\\begin{" + elem + "}",save_split=False) for elem in multiline]
    #expandon += [JunkSearch("\\end{" + elem + "}",save_split=False) for elem in multiline]
    expandon = []
    for old_val,new_val in LATEX_REPLACEMENTS:
        expandon.append(ReplaceSearcher(old_val,new_val,save_split=False))
    #expandon += [Cases,LatexText]#,ReplaceSearcher(r"\mathbbm",r"\mathbb"),ReplaceSearcher(r"\widebar",r"\overline")]
    expandon += [GuardianSearcher("\\",save_split=False),GuardianSearcher("$",save_split=False),GuardianSearcher("{",save_split=False),GuardianSearcher("}",save_split=False)]
    string.expand(expandon) #lol -- was das für ein fehler
    return string


class InlineLatex(Element):
    """Represents inline LaTeX math ($...$).

    Example:
        >>> inline = InlineLatex("x^2", None)
        >>> isinstance(inline.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside $...$.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(string: str) -> int:
        if position_of(string,"$",save_split=False) == position_of(string,"$$",save_split=False):
            return -1
        else:
            return position_of(string,"$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'InlineLatex', str]:
        """Split string and create InlineLatex element.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, InlineLatex, str]: Pre-content, InlineLatex, post-content.
        """
        pre,modifiable_content = split_on_next(string,"$",save_split=False)
        in_outer_dollar = ""
        post = "" 
        content = ""

        while True:
            pending_pre_end,post = split_on_next(modifiable_content,"$",save_split=False)
            if not "\\text" in pending_pre_end:
                content = in_outer_dollar + pending_pre_end
                break
            content_unknown,tmp_post = split_on_next(modifiable_content,"\\text",save_split=False)
            brace_content,modifiable_content = split_on_first_brace(tmp_post)
            in_outer_dollar += content_unknown + "\\text{" + brace_content + "}"
            
        out = InlineLatex(content,parent)
        out = apply_latex_protection(out)
        

        #pre,content,post = begin_end_split(string,"\\begin{document}","\\end{document}")
        return pre,out,post

    def to_string(self) -> str:
        out = f"$"
        for child in self.children:
            out += child.to_string()
        out += "$"
        return out
class DoubleDolarLatex(Element):
    """Represents display math ($$...$$).

    Example:
        >>> dbl = DoubleDolarLatex("x^2", None)
        >>> isinstance(dbl, DoubleDolarLatex)
        True
    """
    prio_elem = True
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside $$...$$.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
        self.label = ""
        self.enumerated = False
        self.handwritten_tag = _handwritten_tag(modifiable_content)

    def add_label(self,label: str):
        if self.label != "":
            print("this label is going to be overwritten:", self.label, "new:", label)
        self.label = label.strip()

    def to_string(self) -> str:
        pre = "\n"
        if self.label != "":
            pre += "(" + self.label + ")=\n"
        pre += ":::{math}\n"

        out = ""
        for child in self.children:
            out += child.to_string()
        """        if not self.enumerated:
            if "\\notag" not in out:
                pre += "\\notag\n"
        """
        pre += out.strip()
        pre += "\n:::\n"
        return pre
    
    def _after_finish_up(self) -> None:
        if self.parent is not None:
            self.parent._propagate_colon_count(3)

    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"$$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'Undefined', str]:
        pre,modifiable_content = split_on_next(string,"$$",save_split=False)
        content,post = split_on_next(modifiable_content,"$$",save_split=False)  
        out = DoubleDolarLatex(content,parent)
        #out = Undefined("\n$$\n" + content.rstrip().lstrip() + "\n$$\n",parent)
        out.expand([EquationLabel])
        out = apply_latex_protection(out)
        out.expand([GuardianSearcher("\\\\")])
        #out.expand([ReplaceSearch("\\\\","</span><br><br><span class='display'>"),JunkSearch("&")])
        return pre,out,post


EQUATIONS_MAPPER = {r"\[":r"\begin{equation*}",r"\]":r"\end{equation*}"}

class DefaultEquation(Element):
    """Searcher for non-enumerated align-like environments.

    Example:
        >>> searcher = BeginAlignStar("\\begin{align*}", "\\end{align*}")
        >>> isinstance(searcher, BeginAlignStar)
        True
    """
    def __init__(self,modifiable_content: str, parent: Element, begin: str, end: str):
        """
        Args:
            begin (str): Begin delimiter.
            end (str): End delimiter.
        """
        super().__init__(modifiable_content,parent)
        if begin in EQUATIONS_MAPPER:
            begin = EQUATIONS_MAPPER[begin]
        if end in EQUATIONS_MAPPER:
            end = EQUATIONS_MAPPER[end]
        self.begin = begin
        self.end = end

        self.label = ""
        self.handwritten_tag = _handwritten_tag(modifiable_content)
        if "*" in self.begin:
            self.enumerated = False
        else:
            self.enumerated = True

    def add_label(self,label: str):
        if self.label != "":
            print("this label is going to be overwritten:", self.label, "new:", label)
        self.label = label.strip()

    def to_string(self) -> str:
        pre = "\n"
        if self.label != "":
            pre += "(" + self.label + ")=\n"
        pre += ":::{math}\n"

        out = ""
        for child in self.children:
            out += child.to_string()
        pre += out.strip()
        pre += "\n:::\n"
        return pre

    def _after_finish_up(self) -> None:
        if self.parent is not None:
            self.parent._propagate_colon_count(3)


# TikZ-family environments that should be emitted as {tikz} directives rather
# than {math} blocks.  The environment content is preserved as-is; for envs
# other than tikzpicture the caller is responsible for loading the required
# LaTeX package (e.g. tikz-cd via tikz_latex_preamble in conf.py).
_TIKZ_ENVS = [
    "tikzpicture",
    "tikzcd",
    "tikzfadingfrompicture",
]

def _extract_tikz_only(content: str):
    """Return ``(tikz_content, label, env_name)`` if *content* consists solely
    of a recognised TikZ-family environment plus an optional ``\\label``,
    otherwise ``None``.

    For ``tikzpicture`` the inner content (without the begin/end tags) is
    returned.  For every other environment the full ``\\begin{env}...\\end{env}``
    block is returned so that sphinxcontrib-tikz receives a self-contained
    snippet.
    """
    work = content

    # Pull out \label{...} if present
    raw_label = ""
    label_match = _re.search(r"\\label\s*\{([^}]*)\}", work)
    if label_match:
        raw_label = label_match.group(1).strip()
        work = work[:label_match.start()] + work[label_match.end():]

    for env_name in _TIKZ_ENVS:
        begin_tok = "\\begin{" + env_name + "}"
        end_tok   = "\\end{"   + env_name + "}"
        begin_pos = work.find(begin_tok)
        end_pos   = work.find(end_tok)
        if begin_pos == -1 or end_pos == -1:
            continue

        remaining = work[:begin_pos] + work[end_pos + len(end_tok):]
        if remaining.strip():
            continue  # real math content exists alongside the figure

        if env_name == "tikzpicture":
            # Strip the wrapper tags; sphinxcontrib-tikz adds them back
            tikz_content = work[begin_pos + len(begin_tok):end_pos]
        else:
            # Keep the full environment so sphinxcontrib-tikz gets a valid snippet
            tikz_content = work[begin_pos:end_pos + len(end_tok)]

        return tikz_content, raw_label, env_name

    return None


class MultiEquationElement(Element):
    """Container for multiple equation blocks produced by splitting a multi-label
    align environment.  Each child is a separate :class:`DefaultEquation`.
    """

    def __init__(self, parent: Element):
        super().__init__("", parent)
        self.children = []

    def to_string(self) -> str:
        return "".join(child.to_string() for child in self.children)

    def _after_finish_up(self) -> None:
        if self.parent is not None:
            self.parent._propagate_colon_count(3)


class DefaultEquationSearcher():
    """Searcher for enumerated align-like environments.

    Example:
        >>> searcher = BeginAlignSearcher("\\begin{align}", "\\end{align}")
        >>> isinstance(searcher, BeginAlignSearcher)
        True
    """
    def __init__(self, begin: str, end: str):
        """
        Args:
            begin (str): Begin delimiter.
            end (str): End delimiter.
        """
        super().__init__()
        self.begin,self.end = begin,end

    def position(self, string: str) -> int:
        """Find position of begin delimiter.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(string,self.begin)
        
    def split_and_create(self, string: str, parent: Element) -> Tuple[str, DefaultEquation, str]:
        """Split string and create element for align environment.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, BeginEquationEnumElement, str]: Pre-content, element, post-content.
        """
        pre,content,post = begin_end_split(string,self.begin,self.end)

        # Tikz-only: if the content is just a tikzpicture + optional \label,
        # emit a {tikz} directive instead of a {math} block.
        tikz_result = _extract_tikz_only(content)
        if tikz_result is not None:
            from .text import TikzElement, _ALL_TIKZ_LIBS
            tikz_content, raw_label, _env_name = tikz_result
            registered_label = ""
            if raw_label:
                registered_label = label_call(raw_label, LabelType.REF)
            return pre, TikzElement(parent, tikz_content, "", _ALL_TIKZ_LIBS, label=registered_label), post

        # Fast path: zero or one \label → no splitting needed
        if content.count("\\label") <= 1:
            out = DefaultEquation(content,parent,self.begin,self.end)
            out.expand([EquationLabel])
            out = apply_latex_protection(out)
            return pre,out,post

        # Multiple labels: split rows on \\ (LaTeX row separator) and group
        # each run of rows up-to-and-including the labeled row into its own block.
        rows = content.split("\\\\")
        blocks: list = []
        current: list = []
        for row in rows:
            current.append(row)
            if "\\label" in row:
                blocks.append(current)
                current = []
        if current:  # trailing unlabeled rows
            blocks.append(current)

        container = MultiEquationElement(parent)
        for block_rows in blocks:
            block_content = "\\begin{aligned} " + " \\\\ ".join(block_rows) + " \\end{aligned}"
            sub_eq = DefaultEquation(block_content.strip(), container, self.begin, self.end)
            sub_eq.expand([EquationLabel])
            sub_eq = apply_latex_protection(sub_eq)
            container.children.append(sub_eq)

        return pre, container, post
       
def get_all_filters() -> list:
    """Returns all equation-related filter classes/searchers.

    Returns:
        list: List of filter classes/searchers.

    Example:
        >>> filters = get_all_filters()
        >>> isinstance(filters, list)
        True
    """
    #The derivatives are 
    multiline = ["split", "multline","align","breqn","equation","displaymath","gather","flalign","alignat","eqnarray","math"]
    multiline_enum = [DefaultEquationSearcher("\\begin{"+ elem+"}","\\end{"+ elem+"}") for elem in multiline]
    multiline_no_enum = [DefaultEquationSearcher("\\begin{"+ elem+"*}","\\end{"+ elem+"*}") for elem in multiline]
    out = [DoubleDolarLatex,InlineLatex,DefaultEquationSearcher("\\[","\\]")]
    out.extend(multiline_enum)
    out.extend(multiline_no_enum)
    return out
    

















class LatexText(Element):
    """Represents LaTeX text command.

    Example:
        >>> text = LatexText("hello", None)
        >>> isinstance(text.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside \\text{}.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\text")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'LatexText', str]:
        pre,post = split_on_next(string,"\\text")
        content,post = split_on_first_brace(post)
        out = LatexText(content,parent)
        out.expand([GuardianSearcher("$"),GuardianSearcher("\\\\"),GuardianSearcher("\\text")])
        return pre,out,post

    def to_string(self) -> str:
        out = "\\text{"
        for child in self.children:
            out += child.to_string()
        out += "}"

        return out

class Cases(Element):
    """Represents LaTeX cases environment.

    Example:
        >>> cases = Cases("x & y \\\\ z & w", None)
        >>> isinstance(cases.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside cases.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\begin{cases}")
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'Cases', str]:
        pre,content,post = begin_end_split(string,"\\begin{cases}","\\end{cases}")
        out = Cases(content,parent)
        out.expand([LatexText])
        out.expand([GuardianSearcher("\\\\"),GuardianSearcher("\\&"),GuardianSearcher("&")])
        
        return pre,out,post

    def to_string(self) -> str:
        out = "\\begin{cases}"
        for child in self.children:
            out += child.to_string()

        out += "\\end{cases}"
        return out
