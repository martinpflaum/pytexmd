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
]

#%%
#from drawtex import contains_drawtex,get_drawtex_searchers
from .splitting import *
from .core import *
from typing import List,Tuple,Union
from ..config import LATEX_REPLACEMENTS


class EquationLabel(Element):
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__("",parent)
        self.label = label_call(modifiable_content,LabelType.EQ)
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
        self.enumerated = True

    def add_label(self,label: str):
        if self.label != "":
            print("this label is going to be overwritten:", self.label, "new:", label)
        self.label = label.strip()

    def to_string(self) -> str:
        pre = "\n:::{math}\n"
        if self.label != "":
            pre += ":label: " + self.label + "\n"
        if not self.enumerated:
            pre += ":enumerated: false\n"

        out = ""
        for child in self.children:
            out += child.to_string()
        pre += out.strip()
        pre += "\n:::\n"
        return pre
    
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
        self.enumerated = True

    def add_label(self,label: str):
        if self.label != "":
            print("this label is going to be overwritten:", self.label, "new:", label)
        self.label = label.strip()

    def to_string(self) -> str:
        pre = "\n:::{math}\n"
        if self.label != "":
            pre += ":label: " + self.label + "\n"
        if not self.enumerated:
            pre += ":enumerated: false\n"
            
        out = ""
        for child in self.children:
            out += child.to_string()
        pre += out.strip()
        pre += "\n:::\n"
        return pre

 
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
        
        """if contains_drawtex(content):
            out = Undefined(content,parent)
            out.expand(get_drawtex_searchers())
            out = apply_latex_protection(out)
            return pre,out,post
        """
        
        out = DefaultEquation(content,parent,self.begin,self.end)
        out.expand([EquationLabel])
        out = apply_latex_protection(out)
        return pre,out,post
       
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
    