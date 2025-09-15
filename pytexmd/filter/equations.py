#%%
#from drawtex import contains_drawtex,get_drawtex_searchers
from .splitting import *
from .core import *

def apply_latex_protection(string: Element) -> Element:
    """
    Expands and protects LaTeX environments and commands in the given element.

    Args:
        string (Element): The element to process.

    Returns:
        Element: The processed element.

    Example:
        ```python
        protected = apply_latex_protection(some_element)
        ```
    """
    multiline = ["split", "multline","align","breqn","equation"]
    
    expandon = [JunkSearch("\\begin{" + elem + "}",save_split=False) for elem in multiline]
    expandon += [JunkSearch("\\end{" + elem + "}",save_split=False) for elem in multiline]

    expandon += [Label,Cases,LatexText,ReplaceSearch(r"\mathbbm",r"\mathbb"),ReplaceSearch(r"\widebar",r"\overline")]
    expandon += [TexArray,GuardianSearch("$",save_split=False),GuardianSearch("{",save_split=False),GuardianSearch("}",save_split=False)]
    string.expand(expandon) #lol -- was das für ein fehler
    return string


class TexArray(Element):
    """
    Represents a LaTeX array environment.

    Example:
        ```python
        arr = TexArray("a & b \\\\ c & d", parent)
        print(arr.to_string())
        ```
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
        """
        Find position of '\\begin{array}' in string.

        Args:
            string (str): Input string.

        Returns:
            int: Position index or -1.
        """
        if "\\begin{array}" in string:
            return position_of(string,"\\begin{array}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Split string on array environment and create TexArray.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, TexArray, post)
        """
        pre,content,post = begin_end_split(string,"\\begin{array}","\\end{array}")
        out = TexArray(content,parent)
        out.expand([LatexText])
        out.expand([GuardianSearch("\\\\"),GuardianSearch("\\&"),GuardianSearch("&")])
        
        return pre,out,post

    def to_string(self) -> str:
        """
        Convert array to LaTeX string.

        Returns:
            str: LaTeX array string.
        """
        out = "\\begin{array}"
        for child in self.children:
            out += child.to_string()

        out += "\\end{array}"
        return out

class BeginEquationEnumElement(Element):
    """
    Represents an enumerated equation environment.

    Example:
        ```python
        eq = BeginEquationEnumElement("E=mc^2", parent)
        print(eq.to_string())
        ```
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside the environment.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
        number_within_equation = parent.search_class(Document).globals.number_within_equation

        search_func = lambda instance : has_value_equal(instance,"theorem_env_name",number_within_equation)
        section_enum = parent.search_up_on_func(search_func)
        self.section_number = section_enum.generate_child_equation_number()
    
    def label_name(self) -> str:
        """
        Returns the label name for the equation.

        Returns:
            str: Label name.
        """
        return "("+self.get_section_enum()[:-1] + ")"
   
    def get_section_enum(self) -> str:
        """
        Get section enumeration string.

        Returns:
            str: Section enumeration.
        """
        number_within_equation = self.search_class(Document).globals.number_within_equation
        #print("number_within_equation",number_within_equation)
        if number_within_equation is None:
            return str(self.section_number) + "."
        else:
            search_func = lambda instance : has_value_equal(instance,"theorem_env_name",number_within_equation)
            section_enum = None
            if self.parent._modifiable_content != "":
                if len(self.parent.children) > 0:
                    section_enum = self.parent.children[-1].search_up_on_func(search_func)
                else:
                    section_enum = self.parent.search_up_on_func(search_func)
            else:
                section_enum = self.search_up_on_func(search_func)

            if section_enum is None:
                raise RuntimeError("couldn't find enumaration parent: --"+number_within_equation +"-- in BeginEquationEnumElement")

            out = section_enum.get_section_enum()
            out += str(self.section_number) + "."
            return out

    def to_string(self) -> str:
        """
        Output markdown myst string for equation block with tag.

        Returns:
            str: Markdown string.
        """
        pre = f"\n$$\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = pre+out.lstrip().rstrip()
        out += "\n$$\n"
        return out


class BeginEquationEnumSearcher():
    """
    Searches for enumerated equation environments.

    Example:
        ```python
        searcher = BeginEquationEnumSearcher("equation")
        pos = searcher.position(some_string)
        ```
    """
    def __init__(self, name: str):
        """
        Args:
            name (str): Environment name.
        """
        super().__init__()
        self.name = name
    def position(self, string: str) -> int:
        """
        Find position of environment begin.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(string,"\\begin{"+self.name+ "}")
    
    def split_and_create(self, string: str, parent: Element) -> tuple:
        """
        Split string and create enumerated equation element.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, element, post)
        """
        pre,content,post = begin_end_split(string,"\\begin{"+self.name+"}","\\end{"+self.name+"}")
        out = BeginEquationEnumElement(content,parent)
        out = apply_latex_protection(out)
        #section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        return pre,out,post


class InlineLatex(Element):
    """
    Represents inline LaTeX math ($...$).

    Example:
        ```python
        inline = InlineLatex("x^2", parent)
        print(inline.to_string())
        ```
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
        """
        Find position of inline math.

        Args:
            string (str): Input string.

        Returns:
            int: Position index or -1.
        """
        if position_of(string,"$",save_split=False) == position_of(string,"$$",save_split=False):
            return -1
        else:
            return position_of(string,"$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Split string and create InlineLatex element.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, InlineLatex, post)
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
        """
        Convert to inline math string.

        Returns:
            str: Inline math string.
        """
        out = f"$"
        for child in self.children:
            out += child.to_string()
        out += "$"
        return out

class LatexText(Element):
    """
    Represents LaTeX text command.

    Example:
        ```python
        text = LatexText("hello", parent)
        print(text.to_string())
        ```
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
        """
        Find position of '\\text' in string.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(string,"\\text")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Split string and create LatexText element.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, LatexText, post)
        """
        pre,post = split_on_next(string,"\\text")
        content,post = split_on_first_brace(post)
        out = LatexText(content,parent)
        out.expand([GuardianSearch("$"),GuardianSearch("\\\\"),GuardianSearch("\\text")])
        return pre,out,post

    def to_string(self) -> str:
        """
        Convert to LaTeX text string.

        Returns:
            str: LaTeX text string.
        """
        out = "\\text{"
        for child in self.children:
            out += child.to_string()
        out += "}"

        return out

class Cases(Element):
    """
    Represents LaTeX cases environment.

    Example:
        ```python
        cases = Cases("x & y \\\\ z & w", parent)
        print(cases.to_string())
        ```
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
        """
        Find position of '\\begin{cases}'.

        Args:
            string (str): Input string.

        Returns:
            int: Position index or -1.
        """
        if "\\begin{cases}" in string:
            return position_of(string,"\\begin{cases}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Split string and create Cases element.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, Cases, post)
        """
        pre,content,post = begin_end_split(string,"\\begin{cases}","\\end{cases}")
        out = Cases(content,parent)
        out.expand([LatexText])
        out.expand([GuardianSearch("\\\\"),GuardianSearch("\\&"),GuardianSearch("&")])
        
        return pre,out,post

    def to_string(self) -> str:
        """
        Convert to LaTeX cases string.

        Returns:
            str: LaTeX cases string.
        """
        out = "\\begin{cases}"
        for child in self.children:
            out += child.to_string()

        out += "\\end{cases}"
        return out
    
class DoubleDolarLatex(Element):
    """
    Represents display math ($$...$$).

    Example:
        ```python
        dbl = DoubleDolarLatex("x^2", parent)
        ```
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
        """
        Find position of '$$' in string.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(string,"$$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Split string and create DoubleDolarLatex element.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, DoubleDolarLatex, post)
        """
        pre,modifiable_content = split_on_next(string,"$$",save_split=False)
        content,post = split_on_next(modifiable_content,"$$",save_split=False)  
        out = Undefined("\n$$\n" + content.rstrip().lstrip() + "\n$$\n",parent)
        out = apply_latex_protection(out)
        out.expand([GuardianSearch("\\\\")])
        #out.expand([ReplaceSearch("\\\\","</span><br><br><span class='display'>"),JunkSearch("&")])
        return pre,out,post


class BeginEquationElement(Element):
    """
    Represents a basic equation environment.

    Example:
        ```python
        eq = BeginEquationElement("E=mc^2", parent)
        print(eq.to_string())
        ```
    """
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): Content inside the environment.
            parent (Element): Parent element.
        """
        super().__init__(modifiable_content,parent)
    
    def to_string(self) -> str:
        """
        Output markdown myst string for equation block.

        Returns:
            str: Markdown string.
        """
        pre = f"\n$$\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = pre+out.lstrip().rstrip()
        out += "\n$$\n"
        return out



class BeginAlignStar():
    """
    Searches for non-enumerated align-like environments.

    Example:
        ```python
        searcher = BeginAlignStar("\\begin{align*}", "\\end{align*}")
        ```
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
        """
        Find position of begin delimiter.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(string,self.begin)
    
    def split_and_create(self, string: str, parent: Element) -> tuple:
        """
        Split string and create element for align* environment.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, element, post)
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
        out.expand([GuardianSearch("\\\\")])
        return pre,out,post


class BeginAlignSearcher():
    """
    Searches for enumerated align-like environments.

    Example:
        ```python
        searcher = BeginAlignSearcher("\\begin{align}", "\\end{align}")
        ```
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
        """
        Find position of begin delimiter.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(string,self.begin)
        
    def split_and_create(self, string: str, parent: Element) -> tuple:
        """
        Split string and create element for align environment.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            tuple: (pre, element, post)
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
        out.expand([GuardianSearch("\\\\")])
        return pre,out,post
       
def get_all_filters() -> list:
    """
    Returns all equation-related filter classes/searchers.

    Returns:
        list: List of filter classes/searchers.

    Example:
        ```python
        filters = get_all_filters()
        ```
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
