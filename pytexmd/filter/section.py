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
]

from .core import Element,Undefined,Document,SectionEnumerate
from . import splitting
from . import misc

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

        out = "<br><br><strong>"+ self.get_section_enum()[:-1]+"</strong>"
        
        return out

    @staticmethod
    def position(input: str) -> int:
        return splitting.position_of(input,"\\para")

    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,post = splitting.split_on_next(input,"\\para")
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        return pre,Para("",section_number,parent),post

    
class Chapter(SectionEnumerate):

    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"chapter","document")
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return splitting.position_of(input,"\\chapter")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,content = splitting.split_on_next(input,"\\chapter")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content =  splitting.split_on_first_brace(content,error_replacement="chapter_error")
        if "\\chapter" in content:
            content,post = splitting.split_on_next(content,"\\chapter")
            post = "\\chapter" + post
        else:
            post = ""
        
        return pre,Chapter(content,name,section_number,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "</p><h1 style='font-size:50px;line-height: 80%;'>" + str(self.section_number) + " "+ self.children[0].to_string()  + "</h1><p>"
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
        return splitting.position_of(input,"\\chapter*")


    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,content = splitting.split_on_next(input,"\\chapter*")
        
        name,content =  splitting.split_on_first_brace(content)
        if "\\chapter" in content:
            content,post = splitting.split_on_next(content,"\\chapter")
            post = "\\chapter" + post
        else:
            post = ""
        
        return pre,ChapterStar(content,name,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "</p><h1 style='font-size:50px;line-height: 80%;'>" + self.children[0].to_string()  + "</h1><p>"
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
        return splitting.position_of(input,"\\section*")
            
    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,content = splitting.split_on_next(input,"\\section*")
        
        name,content = splitting.split_on_first_brace(content)
        if "\\section" in content:
            content,post = splitting.split_on_next(content,"\\section")
            post = "\\section" + post
        else:
            post = ""
        
        return pre,SectionStar(content,name,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "</p><h1>" + self.children[0].to_string()  + "</h1><p>"
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
        return splitting.position_of(input,"\\subsection")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,content = splitting.split_on_next(input,"\\subsection")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content =  splitting.split_on_first_brace(content)
        if "\\subsection" in content:
            content,post = splitting.split_on_next(content,"\\subsection")
            post = "\\subsection" + post
        else:
            post = ""
        
        return pre,Section(content,name,section_number,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "</p><h2>" + self.get_section_enum()[:-1] + " "+ self.children[0].to_string()  + "</h2><p>"
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
        return splitting.position_of(input,"\\section")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> tuple:
        pre,content = splitting.split_on_next(input,"\\section")
        
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        name,content = splitting.split_on_first_brace(content)
        if "\\section" in content:
            content,post = splitting.split_on_next(content,"\\section")
            post = "\\section" + post
        else:
            post = ""
        
        return pre,Section(content,name,section_number,parent),post

    def to_string(self) -> str:
        """
        first children ist name of Section
        """
        out = "</p><h1>" + self.get_section_enum()[:-1] + " "+ self.children[0].to_string()  + "</h1><p>"
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
        return splitting.position_of(input,"\\subsection*")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = splitting.split_on_next(input,"\\subsection*")
        name,post = splitting.split_on_first_brace(post)
        return pre,SubsectionStar(name,parent),post

    def to_string(self) -> str:
        out = "</p><h2>"
        for child in self.children:
            out += child.to_string()
        out += "</h2><p>"
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
        return splitting.position_of(input,"\\ref")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = splitting.split_on_next(input,"\\ref")
        label_ref,post = splitting.split_on_first_brace(post)
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
        return splitting.position_of(input,"\\eqref")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = splitting.split_on_next(input,"\\eqref")
        label_ref,post = splitting.split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self) -> str:
        return self.label_name

class Proof(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        self.name = "Proof"
        if not splitting.split_rename(modifiable_content) is None:
            self.name,modifiable_content = splitting.split_rename(modifiable_content) 
        self.name += "."
        super().__init__(modifiable_content,parent)
        
    @staticmethod
    def position(input: str) -> int:
        if "\\begin{proof}" in input:
            return splitting.position_of(input,"\\begin{proof}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,content,post = splitting.begin_end_split(input,"\\begin{proof}","\\end{proof}")
        return pre,Proof(content,parent),post

    def to_string(self) -> str:
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
        return splitting.position_of(input,"\\textbf")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = splitting.split_on_next(input,"\\textbf")
        name,post = splitting.split_on_first_brace(post)
        return pre,Textbf(name,parent),post

    def to_string(self) -> str:
        out = "<strong>"
        for child in self.children:
            out += child.to_string()
        out += "</strong>"
        return out

class Cite(Element):
    def __init__(self, modifiable_content: str, parent: Element, citations: list):
        super().__init__(modifiable_content,parent)
        self.citations = citations
    
    @staticmethod
    def position(input: str) -> int:
        return splitting.position_of(input,"\\cite")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = splitting.split_on_next(input,"\\cite")
        name,post = splitting.split_on_first_brace(post)
        tmp = ""
        for elem in name.split(" "):
            tmp += elem
        citations = tmp.split(",")
        return pre,Cite("",parent,citations),post

    def to_string(self) -> str:
        out = ""
        for elem in self.citations:
            out += "<dt-cite key=\"" + elem +"\"></dt-cite>"
        return out


class Emph(Element):
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return splitting.position_of(input,"\\emph")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> tuple:
        pre,post = splitting.split_on_next(input,"\\emph")
        name,post = splitting.split_on_first_brace(post)
        return pre,Emph(name,parent),post

    def to_string(self) -> str:
        out = "<i>"
        for child in self.children:
            out += child.to_string()
        out += "</i>"
        return out
    
class TheoremElement(SectionEnumerate):
    def __init__(self, modifiable_content: str, section_number: int, parent: Element, display_name: str, theorem_env_name: str, enum_parent_class):
        super().__init__(modifiable_content,parent,theorem_env_name,enum_parent_class)
        self.section_number = section_number 
        self.display_name = display_name
        

    def label_name(self) -> str:
        return self.get_section_enum()[:-1]
    
    def to_string(self, tab_lvl: int) -> str:
        """
        Output markdown myst string for theorem block.
        """
        out = f"\n:::{{.theorem}} {self.display_name} {self.get_section_enum()[:-1]}\n"
        for child in self.children:
            out += child.to_string(tab_lvl)
        out += "\n:::\n"
        return out


class TheoremSearcher():
    def __init__(self, theorem_env_name: str, enum_parent_class, display_name: str):
        self.display_name = display_name
        self.theorem_env_name = theorem_env_name
        self.enum_parent_class = enum_parent_class
    def position(self, input: str) -> int:
        return splitting.position_of(input,"\\begin{" + self.theorem_env_name + "}")
            
    def split_and_create(self, input: str, parent: Element) -> tuple:
        pre,content,post = splitting.begin_end_split(input,"\\begin{"+self.theorem_env_name+"}","\\end{"+self.theorem_env_name+"}")
        
        search_func = lambda instance : misc.has_value_equal(instance,"theorem_env_name",self.enum_parent_class)
        
        #potential bug - normaly you would have a space or new line
        section_enum = parent.children[-1].search_up_on_func(search_func)
        section_number = section_enum.generate_child_section_number()
        
        return pre,TheoremElement(content,section_number,parent,self.display_name,self.theorem_env_name,self.enum_parent_class),post

def get_theoremSearchers(input: str) -> list:
    need_fix = []
    pending_envs = []
    shared_parent_fixer = {"section":"document","subsection":"section"}
    while True:
        pre,post = splitting.split_on_next(input,"\\newtheorem")
        if input == pre:
            break
        theorem_env_name,post = splitting.split_on_first_brace(post)
        display_name = ""
        if splitting.first_char_brace(post):
            enum_parent_class = ""
            display_name,post = splitting.split_on_first_brace(post)
            if splitting.first_char_brace(post,"["):
                enum_parent_class,post = splitting.split_on_first_brace(post,"[","]")
            else:
                enum_parent_class = None
            shared_parent_fixer[theorem_env_name] = enum_parent_class
            pending_envs.append((theorem_env_name,enum_parent_class,display_name))
        else:
            if splitting.first_char_brace(post,"["):
                shared_parent,post = splitting.split_on_first_brace(post,"[","]")
                display_name,post = splitting.split_on_first_brace(post)
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


def get_all_filters() -> list:
    return [SectionStar,Para,Chapter,Section,ChapterStar,SubsectionStar,Proof,Emph,Textbf]
