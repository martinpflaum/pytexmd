#%%
#from drawtex import contains_drawtex,get_drawtex_searchers
from .splitting import *
from .core import *
from . import misc

def apply_latex_protection(string: Element) -> Element:
    multiline = ["split", "multline","align","breqn","equation"]
    
    expandon = [JunkSearch("\\begin{" + elem + "}",save_split=False) for elem in multiline]
    expandon += [JunkSearch("\\end{" + elem + "}",save_split=False) for elem in multiline]

    expandon += [Label,Cases,LatexText,ReplaceSearch("\mathbbm","\mathbb"),ReplaceSearch("\widebar","\overline")]
    expandon += [TexArray,GuardianSearch("{",save_split=False),GuardianSearch("}",save_split=False)]
    string.expand(expandon) #lol -- was das für ein fehler
    return string


class TexArray(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(string: str) -> int:
        if "\\begin{array}" in string:
            return position_of(string,"\\begin{array}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        pre,content,post = begin_end_split(string,"\\begin{array}","\\end{array}")
        out = TexArray(content,parent)
        out.expand([LatexText])
        out.expand([GuardianSearch("\\\\"),GuardianSearch("\\&"),GuardianSearch("&")])
        
        return pre,out,post

    def to_string(self) -> str:
        out = "\\begin{array}"
        for child in self.children:
            out += child.to_string()

        out += "\\end{array}"
        return out

class BeginEquationEnumElement(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
        number_within_equation = parent.search_class(Document).globals.number_within_equation

        search_func = lambda instance : has_value_equal(instance,"theorem_env_name",number_within_equation)
        section_enum = parent.search_up_on_func(search_func)
        self.section_number = section_enum.generate_child_equation_number()
    
    def label_name(self) -> str:
        return "("+self.get_section_enum()[:-1] + ")"
   
    def get_section_enum(self) -> str:
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
        """
        out = f"\n````{{math}}\n% Equation {self.get_section_enum()[:-1]}\n"
        for child in self.children:
            out += child.to_string()
        out += "\n````\n"
        return out


class BeginEquationEnumSearcher():
    def __init__(self, name: str):
        super().__init__()
        self.name = name
    def position(self, string: str) -> int:
        return position_of(string,"\\begin{"+self.name+ "}")
    
    def split_and_create(self, string: str, parent: Element) -> tuple:
        pre,content,post = begin_end_split(string,"\\begin{"+self.name+"}","\\end{"+self.name+"}")
        out = BeginEquationEnumElement(content,parent)
        out = apply_latex_protection(out)
        #section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        return pre,out,post


class InlineLatex(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(string: str) -> int:
        if position_of(string,"$",save_split=False) == position_of(string,"$$",save_split=False):
            return -1
        else:
            return position_of(string,"$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
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
        out = f"`$"
        for child in self.children:
            out += child.to_string()
        out += "$`"
        return out

class LatexText(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\text")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        pre,post = split_on_next(string,"\\text")
        content,post = split_on_first_brace(post)
        out = LatexText(content,parent)
        out.expand([GuardianSearch("$"),GuardianSearch("\\\\"),GuardianSearch("\\text")])
        return pre,out,post

    def to_string(self) -> str:
        out = "\\text{"
        for child in self.children:
            out += child.to_string()
        out += "}"

        return out

class Cases(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(string: str) -> int:
        if "\\begin{cases}" in string:
            return position_of(string,"\\begin{cases}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        pre,content,post = begin_end_split(string,"\\begin{cases}","\\end{cases}")
        out = Cases(content,parent)
        out.expand([LatexText])
        out.expand([GuardianSearch("\\\\"),GuardianSearch("\\&"),GuardianSearch("&")])
        
        return pre,out,post

    def to_string(self) -> str:
        out = "\\begin{cases}"
        for child in self.children:
            out += child.to_string()

        out += "\\end{cases}"
        return out
    
class DoubleDolarLatex(Element):
    prio_elem = True
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"$$",save_split=False)
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        pre,modifiable_content = split_on_next(string,"$$",save_split=False)
        content,post = split_on_next(modifiable_content,"$$",save_split=False)  
        out = Undefined("\n````{math}\n" + content + "\n````\n",parent)
        out = apply_latex_protection(out)
        out.expand([GuardianSearch("\\\\")])
        #out.expand([ReplaceSearch("\\\\","</span><br><br><span class='display'>"),JunkSearch("&")])
        return pre,out,post


class BeginEquationElement(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
    
    def to_string(self) -> str:
        """
        Output markdown myst string for equation block.
        """
        out = "\n````{math}\n"
        for child in self.children:
            out += child.to_string()
        out += "\n````\n"
        return out




class BeginAlignStar():
    def __init__(self, begin: str, end: str):
        super().__init__()
        self.begin,self.end = begin,end
    def position(self, string: str) -> int:
        return position_of(string,self.begin)
    
    def split_and_create(self, string: str, parent: Element) -> tuple:
        pre,content,post = begin_end_split(string,self.begin,self.end)
        
        """if contains_drawtex(content):
            out = Undefined(content,parent)
            out.expand(get_drawtex_searchers())
            out = apply_latex_protection(out)
            return pre,out,post
        """
        out = Undefined("\n````{math}\n" + content + "\n````\n",parent)
        out = apply_latex_protection(out)
        out.expand([GuardianSearch("\\\\")])
        return pre,out,post


class BeginAlignSearcher():
    def __init__(self, begin: str, end: str):
        super().__init__()
        self.begin,self.end = begin,end

    def position(self, string: str) -> int:
        return position_of(string,self.begin)
        
    def split_and_create(self, string: str, parent: Element) -> tuple:
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
