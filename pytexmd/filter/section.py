__all__ = [
    "Section",
    "Chapter",
    "SectionStar",
    "ChapterStar",
    "Subsection",
    "SubsectionStar",
    "Label",
    "Ref",
    "EqRef",
    "Proof",
    "Textbf",
    "Emph",
    "Para",
    "SectionEnumerate",
    "Cite"
    "get_all_filters",
    "get_number_within_equation",
    "get_theoremSearchers"
]

from .core import *
from .splitting import *

class Para(SectionEnumerate):
    def __init__(self, modifiable_content: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"para","section")
        self.section_number = section_number
    def label_name(self) -> str:
        return self.get_section_enum()[:-1]

    def to_string(self) -> str:
        """
        first children ist name of Section
        """

        out = "\n#"+ self.get_section_enum()[:-1]+"\n"
        
        return out

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\para")

    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,post = split_on_next(input,"\\para")
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        return pre,Para("",section_number,parent),post

    
class Chapter(SectionEnumerate):

    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"chapter","document")
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\chapter")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,content = split_on_next(input,"\\chapter")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content =  split_on_first_brace(content,error_replacement="chapter_error")
        if "\\chapter" in content:
            content,post = split_on_next(content,"\\chapter")
            post = "\\chapter" + post
        else:
            post = ""
        
        return pre,Chapter(content,name,section_number,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "\n#" + str(self.section_number) + " "+ self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out

class ChapterStar(Element):
    prio_elem = True
    def __init__(self, modifiable_content: str, section_name: str, parent: Element):
        super().__init__(modifiable_content,parent)
        self.children = [Undefined(section_name,self)]
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\chapter*")


    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,content = split_on_next(input,"\\chapter*")
        
        name,content =  split_on_first_brace(content)
        if "\\chapter" in content:
            content,post = split_on_next(content,"\\chapter")
            post = "\\chapter" + post
        else:
            post = ""
        
        return pre,ChapterStar(content,name,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "\n#" + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


class SectionStar(Element):
    prio_elem = True
    def __init__(self, modifiable_content: str, section_name: str, parent: Element):
        super().__init__(modifiable_content,parent)
        self.children = [Undefined(section_name,self)]
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\section*")
            
    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,content = split_on_next(input,"\\section*")
        
        name,content = split_on_first_brace(content)
        if "\\section" in content:
            content,post = split_on_next(content,"\\section")
            post = "\\section" + post
        else:
            post = ""
        
        return pre,SectionStar(content,name,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "\n#" + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


class Subsection(SectionEnumerate):

    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"subsection",["section"])
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\subsection")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,content = split_on_next(input,"\\subsection")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content =  split_on_first_brace(content)
        if "\\subsection" in content:
            content,post = split_on_next(content,"\\subsection")
            post = "\\subsection" + post
        else:
            post = ""
        
        return pre,Section(content,name,section_number,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "\n##" + self.get_section_enum()[:-1] + " "+ self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out



class Section(SectionEnumerate):

    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"section",["chapter","document"])
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\section")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,content = split_on_next(input,"\\section")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content = split_on_first_brace(content)
        if "\\section" in content:
            content,post = split_on_next(content,"\\section")
            post = "\\section" + post
        else:
            post = ""
        
        return pre,Section(content,name,section_number,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "\n#" + self.get_section_enum()[:-1] + " "+ self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out

class SubsectionStar(Element):
    prio_elem = True
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\subsection*")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = split_on_next(input,"\\subsection*")
        name,post = split_on_first_brace(post)
        return pre,SubsectionStar(name,parent),post

    def to_string(self) -> str:
        out = "\n#"+" "+ self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


class Ref(Element):
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        try:
            self.label_name = self.search_class(Document).globals.labels[label_ref]
        except Exception:
            self.label_name = "ref_error"

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\ref")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = split_on_next(input,"\\ref")
        label_ref,post = split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self) -> str:
        return self.label_name


class EqRef(Element):
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        try:
            self.label_name = self.search_class(Document).globals.labels[label_ref]
        except Exception:
            self.label_name = "ref_error"

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\eqref")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = split_on_next(input,"\\eqref")
        label_ref,post = split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self) -> str:
        return self.label_name

class Proof(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        self.name = "Proof"
        if not split_rename(modifiable_content) is None:
            self.name,modifiable_content = split_rename(modifiable_content) 
        self.name += "."
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(input: str) -> int:
        if "\\begin{proof}" in input:
            return position_of(input,"\\begin{proof}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,content,post = begin_end_split(input,"\\begin{proof}","\\end{proof}")
        return pre,Proof(content,parent),post

    def to_string(self) -> str:
        out = f"\n:::{{.proof}} {self.name}\n"
        for child in self.children:
            out += child.to_string()
        out += "\n:::\n"
        return out

        
        out = f"<br><i>{self.name}</i>"
        for child in self.children:
            #print(type(child))
            out += child.to_string()
        return out

    
class Textbf(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\textbf")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = split_on_next(input,"\\textbf")
        name,post = split_on_first_brace(post)
        return pre,Textbf(name,parent),post

    def to_string(self) -> str:
        out = "**"
        for child in self.children:
            out += child.to_string()
        out += "**"
        return out

class Cite(Element):
    def __init__(self, modifiable_content: str, parent: Element, citations: list[str]):
        super().__init__(modifiable_content,parent)
        self.citations = citations
    
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\cite")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = split_on_next(input,"\\cite")
        name,post = split_on_first_brace(post)
        tmp = ""
        for elem in name.split(" "):
            tmp += elem
        citations = tmp.split(",")
        return pre,Cite("",parent,citations),post

    def to_string(self) -> str:
        out = "["
        for elem in self.citations:
            out += f"@{elem.lstrip().rstrip()}; "
        out = out[:-2]+"]"
        return out


class Emph(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\emph")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = split_on_next(input,"\\emph")
        name,post = split_on_first_brace(post)
        return pre,Emph(name,parent),post

    def to_string(self) -> str:
        out = "*"
        for child in self.children:
            out += child.to_string()
        out += "*"
        return out
    
class TheoremElement(SectionEnumerate):
    def __init__(self, modifiable_content: str, section_number: int, parent: Element, display_name: str, theorem_env_name: str, enum_parent_class):
        super().__init__(modifiable_content,parent,theorem_env_name,enum_parent_class)
        self.section_number = section_number 
        self.display_name = display_name
        

    def label_name(self) -> str:
        return self.get_section_enum()[:-1]
    
    def to_string(self) -> str:
        """
        Output markdown myst string for theorem block.
        """
        pre = "\n:::{admonition} "+f"{self.display_name} {self.get_section_enum()[:-1]}\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = out.lstrip().rstrip()
        out = pre + out
        
        out += "\n:::\n"
        return out


class TheoremSearcher():
    def __init__(self, theorem_env_name: str, enum_parent_class, display_name: str):
        self.display_name = display_name
        self.theorem_env_name = theorem_env_name
        self.enum_parent_class = enum_parent_class
    def position(self, input: str) -> int:
        return position_of(input,"\\begin{" + self.theorem_env_name + "}")
            
    def split_and_create(self, input: str, parent: Element) -> tuple:
        pre,content,post = begin_end_split(input,"\\begin{"+self.theorem_env_name+"}","\\end{"+self.theorem_env_name+"}")
        
        search_func = lambda instance : has_value_equal(instance,"theorem_env_name",self.enum_parent_class)
        
        #potential bug - normaly you would have a space or new line
        section_enum = parent.children[-1].search_up_on_func(search_func)
        section_number = section_enum.generate_child_section_number()
        
        return pre,TheoremElement(content,section_number,parent,self.display_name,self.theorem_env_name,self.enum_parent_class),post

def get_theoremSearchers(input: str) -> list:
    need_fix = []
    pending_envs = []
    shared_parent_fixer = {"section":"document","subsection":"section"}
    while True:
        pre,post = split_on_next(input,"\\newtheorem")
        if input == pre:
            break
        theorem_env_name,post = split_on_first_brace(post)
        display_name = ""
        if first_char_brace(post):
            enum_parent_class = ""
            display_name,post = split_on_first_brace(post)
            if first_char_brace(post,"["):
                enum_parent_class,post = split_on_first_brace(post,"[","]")
            else:
                enum_parent_class = None
            shared_parent_fixer[theorem_env_name] = enum_parent_class
            pending_envs.append((theorem_env_name,enum_parent_class,display_name))
        else:
            if first_char_brace(post,"["):
                shared_parent,post = split_on_first_brace(post,"[","]")
                display_name,post = split_on_first_brace(post)
                need_fix.append((theorem_env_name,shared_parent,display_name))
            else:
                print("theoremenv error in ",theorem_env_name)
        input = post
        
    for theorem_env_name,shared_parent,display_name in need_fix:
        pending_envs.append((theorem_env_name,shared_parent_fixer[shared_parent],display_name))
    
    out = []
    for elem in pending_envs:
        print(elem)
        out.append(TheoremSearcher(*elem))
    return out

def get_number_within_equation(input:str)->str:
    input = input.split("\\numberwithin{equation}")
    if len(input) == 1:
        return "document" 
    out,_ = split_on_first_brace(input[1])
    return out

def get_all_filters() -> list:
    return [SectionStar,Para,Chapter,Section,ChapterStar,SubsectionStar,Proof,Emph,Textbf]
