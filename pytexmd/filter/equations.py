#%%
"""Equation filter classes and utilities for pytexmd.

This module provides classes and functions for parsing and processing LaTeX equations,
environments, and math for Markdown/MyST conversion.
"""

__all__ = [
    "EquationLabel",
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
    "get_all_filters"
]

#%%
#from drawtex import contains_drawtex,get_drawtex_searchers
from .splitting import *
from .core import *
from typing import List,Tuple,Union

class EquationLabel(Element):
    """Element for LaTeX equation labels.

    Args:
        modifiable_content (str): Content to process.
        parent (Element): Parent element.
        label_ref (str): Label reference.
    """
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        
        #if not hasattr(self.search_class(Document).globals,"labels"):
        #    self.search_class(Document).globals.labels = {}
        
        #holder = self.search_attribute_holder("label_name")
        #label_name = "label_error"
        #if not holder is None:
        #    label_name = holder.label_name()
        self.label_ref = label_ref
        #self.search_class(Document).globals.labels[label_ref] = label_name
    
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\label")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'EquationLabel', str]:
        pre,post = split_on_next(string,"\\label")
        label_ref,post = split_on_first_brace(post)
        return pre,EquationLabel("",parent,label_ref),post

    def to_string(self) -> str:
        return r"\label"+"{"+self.label_ref+"}"

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
    expandon = [EquationLabel]
    expandon += [Cases,LatexText,ReplaceSearcher(r"\mathbbm",r"\mathbb"),ReplaceSearcher(r"\widebar",r"\overline")]
    expandon += [TexArray,GuardianSearcher("$",save_split=False),GuardianSearcher("{",save_split=False),GuardianSearcher("}",save_split=False)]
    string.expand(expandon) #lol -- was das für ein fehler
    return string


class TexArray(Element):
    """Represents a LaTeX array environment.

    Example:
        >>> arr = TexArray("a & b \\\\ c & d", None)
        >>> isinstance(arr.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside the array.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(string: str) -> int:
        if "\\begin{array}" in string:
            return position_of(string,"\\begin{array}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'TexArray', str]:
        pre,content,post = begin_end_split(string,"\\begin{array}","\\end{array}")
        out = TexArray(content,parent)
        out.expand([LatexText])
        out.expand([GuardianSearcher("\\\\"),GuardianSearcher("\\&"),GuardianSearcher("&")])
        
        return pre,out,post

    def to_string(self) -> str:
        out = "\\begin{array}"
        for child in self.children:
            out += child.to_string()

        out += "\\end{array}"
        return out

class BeginEquationEnumElement(Element):
    """Represents an enumerated equation environment.

    Example:
        >>> eq = BeginEquationEnumElement("E=mc^2", None)
        >>> isinstance(eq.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside the environment.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)

        #search_func = lambda instance : has_value_equal(instance,"theorem_env_name",number_within_equation)
        #section_enum = parent.search_up_on_func(search_func)
        

    def to_string(self) -> str:
        pre = f"\n$$\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = pre+out.lstrip().rstrip()
        out += "\n$$\n"
        return out


class BeginEquationEnumSearcher():
    """Searcher for enumerated equation environments.

    Example:
        >>> searcher = BeginEquationEnumSearcher("equation")
        >>> isinstance(searcher, BeginEquationEnumSearcher)
        True
    """
    def __init__(self, command_name: str):
        """
        Args:
            name (str): Environment name.
        """
        super().__init__()
        self.begin_end_search = BeginEndSearcher(command_name,)
        
    def position(self, string: str) -> int:
        return self.begin_end_search.position(string)
    
    def split_and_create(self, string: str, parent: Element) -> Tuple[str, BeginEquationEnumElement, str]:
        pre,content,post = self.begin_end_search.split_and_create(string, parent)
        out = BeginEquationEnumElement(content,parent)
        out = apply_latex_protection(out)
        return pre,out,post


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

    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"$$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'Undefined', str]:
        pre,modifiable_content = split_on_next(string,"$$",save_split=False)
        content,post = split_on_next(modifiable_content,"$$",save_split=False)  
        out = Undefined("\n$$\n" + content.rstrip().lstrip() + "\n$$\n",parent)
        out = apply_latex_protection(out)
        out.expand([GuardianSearcher("\\\\")])
        #out.expand([ReplaceSearch("\\\\","</span><br><br><span class='display'>"),JunkSearch("&")])
        return pre,out,post


class BeginEquationElement(Element):
    """Represents a basic equation environment.

    Example:
        >>> eq = BeginEquationElement("E=mc^2", None)
        >>> isinstance(eq.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside the environment.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
    
    def to_string(self) -> str:
        pre = f"\n$$\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = pre+out.lstrip().rstrip()
        out += "\n$$\n"
        return out



class BeginAlignStar():
    """Searcher for non-enumerated align-like environments.

    Example:
        >>> searcher = BeginAlignStar("\\begin{align*}", "\\end{align*}")
        >>> isinstance(searcher, BeginAlignStar)
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
    
    def split_and_create(self, string: str, parent: Element) -> Tuple[str, 'Undefined', str]:
        """Split string and create element for align* environment.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, Undefined, str]: Pre-content, Undefined, post-content.
        """
        pre,content,post = begin_end_split(string,self.begin,self.end)
        
        """if contains_drawtex(content):
            out = Undefined(content,parent)
            out.expand(get_drawtex_searchers())
            out = apply_latex_protection(out)
            return pre,out,post
        """
        out = Undefined("\n$$\n" + content.lstrip().rstrip() + "\n$$\n",parent)
        out = apply_latex_protection(out)
        out.expand([GuardianSearcher("\\\\")])
        return pre,out,post


class BeginAlignSearcher():
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
        
    def split_and_create(self, string: str, parent: Element) -> Tuple[str, BeginEquationEnumElement, str]:
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
        
        out = BeginEquationEnumElement(content,parent)
        out = apply_latex_protection(out)
        out.expand([GuardianSearcher("\\\\")])
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
    multiline = ["split", "multline","align","breqn","equation"]
    multiline_enum = [BeginAlignSearcher("\\begin{"+ elem+"}","\\end{"+ elem+"}") for elem in multiline]
    multiline_no_enum = [BeginAlignStar("\\begin{"+ elem+"*}","\\end{"+ elem+"*}") for elem in multiline]
    out = [DoubleDolarLatex]#DoubleDolarLatex
    out += [BeginAlignStar("\\[","\\]"),BeginAlignStar("\\begin{displaymath}","\\end{displaymath}") ,InlineLatex]
    #ReplaceSearch("\\\\","\n")
    out.extend(multiline_enum)
    out.extend(multiline_no_enum)
    return out
    multiline_no_enum = [BeginAlignStar("\\begin{"+ elem+"*}","\\end{"+ elem+"*}") for elem in multiline]
    out = [DoubleDolarLatex]#DoubleDolarLatex
    out += [BeginAlignStar("\\[","\\]"),BeginAlignStar("\\begin{displaymath}","\\end{displaymath}") ,InlineLatex]
    #ReplaceSearch("\\\\","\n")
    out.extend(multiline_enum)
    out.extend(multiline_no_enum)
    return out
