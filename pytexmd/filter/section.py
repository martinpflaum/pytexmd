"""Section and theorem filter classes and utilities for pytexmd.

This module provides classes and functions for parsing and processing LaTeX sections,
theorems, references, and formatting for Markdown/MyST conversion.
"""

__all__ = [
    "Section",
    "Chapter",
    "SectionStar",
    "ChapterStar",
    "Subsection",
    "SubsectionStar",
    "Ref",
    "EqRef",
    "Proof",
    "Textbf",
    "Emph",
    "Para",
    "SectionEnumerate",
    "Cite",
    "get_all_filters",
    "get_number_within_equation",
    "get_theoremSearchers",
    "Textit",
    "MystLabel",
]
from typing import List, Tuple
from .core import *
from .splitting import *

PRF_TYPES = {
    "algorithm": "prf:algorithm",
    "axiom": "prf:axiom",
    "conjecture": "prf:conjecture",
    "corollary": "prf:corollary",
    "criteria": "prf:criteria",
    "definition": "prf:definition",
    "example": "prf:example",
    "lemma": "prf:lemma",
    "observation": "prf:observation",
    "property": "prf:property",
    "proposition": "prf:proposition",
    "proof": "prf:proof",
    "remark": "prf:remark",
    "theorem": "prf:theorem"
}

"""
proof_theorem_types = [
    ("theorem", "Theorem"),
    ("definition", "Definition"),
    ("remark", "Remark"),
    ("claim", "Claim"),  # <-- custom type
]
"""
for key in list(PRF_TYPES.keys()):
    PRF_TYPES[key+"s"] = PRF_TYPES[key]
    
class MystLabel(Element):
    """Element for MyST label.

    Args:
        modifiable_content (str): Content to process.
        parent (Element): Parent element.
        label_ref (str): Label reference.

    Example:
        >>> label = MystLabel("content", None, "mylabel")
        >>> isinstance(label, MystLabel)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        
        self.label_ref = label_ref
    
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\label")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'MystLabel', str]:
        pre,post = split_on_next(string,"\\label")
        label_ref,post = split_on_first_brace(post)
        return pre,MystLabel("",parent,label_ref),post

    def to_string(self) -> str:
        return "\n:label: "+self.label_ref.strip()+"\n"

class Para(SectionEnumerate):
    """Element for LaTeX \\para section.

    Example:
        >>> para = Para("content", 1, None)
        >>> isinstance(para, Para)
        True
    """
    def __init__(self, modifiable_content: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"para","section")
        self.section_number = section_number
    
    def to_string(self) -> str:
        out = "\n# " + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\para")

    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> Tuple[str, 'Para', str]:
        pre,post = split_on_next(input,"\\para")
        section_number = parent.search_class(SectionEnumerate).generate_child_section_number()
        return pre,Para("",section_number,parent),post

    
class Chapter(SectionEnumerate):
    """Element for LaTeX \\chapter section.

    Example:
        >>> chapter = Chapter("content", "Chapter 1", 1, None)
        >>> isinstance(chapter, Chapter)
        True
    """
    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"chapter","document")
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\chapter")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> Tuple[str, 'Chapter', str]:
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
        out = "\n# " + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out

class ChapterStar(Element):
    """Element for LaTeX \\chapter* section.

    Example:
        >>> chapter_star = ChapterStar("content", "Intro", None)
        >>> isinstance(chapter_star, ChapterStar)
        True
    """
    prio_elem = True
    def __init__(self, modifiable_content: str, section_name: str, parent: Element):
        super().__init__(modifiable_content,parent)
        self.children = [Undefined(section_name,self)]
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\chapter*")


    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'ChapterStar', str]:
        pre,content = split_on_next(input,"\\chapter*")
        
        name,content =  split_on_first_brace(content)
        if "\\chapter" in content:
            content,post = split_on_next(content,"\\chapter")
            post = "\\chapter" + post
        else:
            post = ""
        
        return pre,ChapterStar(content,name,parent),post

    def to_string(self) -> str:
        out = "\n# " + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


class SectionStar(Element):
    """Element for LaTeX \\section* section.

    Example:
        >>> section_star = SectionStar("content", "Intro", None)
        >>> isinstance(section_star, SectionStar)
        True
    """
    prio_elem = True
    def __init__(self, modifiable_content: str, section_name: str, parent: Element):
        super().__init__(modifiable_content,parent)
        self.children = [Undefined(section_name,self)]
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\section*")
            
    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'SectionStar', str]:
        pre,content = split_on_next(input,"\\section*")
        
        name,content = split_on_first_brace(content)
        if "\\section" in content:
            content,post = split_on_next(content,"\\section")
            post = "\\section" + post
        else:
            post = ""
        
        return pre,SectionStar(content,name,parent),post

    def to_string(self) -> str:
        out = "\n# " + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


class Subsection(SectionEnumerate):
    """Element for LaTeX \\subsection section.

    Example:
        >>> subsection = Subsection("content", "Subsection 1", 1, None)
        >>> isinstance(subsection, Subsection)
        True
    """
    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"subsection",["section"])
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\subsection")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> Tuple[str, 'Section', str]:
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
        out = "\n## " + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out



class Section(SectionEnumerate):
    """Element for LaTeX \\section section.

    Example:
        >>> section = Section("content", "Section 1", 1, None)
        >>> isinstance(section, Section)
        True
    """
    def __init__(self, modifiable_content: str, section_name: str, section_number: int, parent: SectionEnumerate):
        super().__init__(modifiable_content,parent,"section",["chapter","document"])
        self.children = [Undefined(section_name,self)]
        self.section_number = section_number
        
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\section")
            
    @staticmethod
    def split_and_create(input: str, parent: SectionEnumerate) -> Tuple[str, 'Section', str]:
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
        out = "\n# " + self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out

class SubsectionStar(Element):
    """Element for LaTeX \\subsection* section.

    Example:
        >>> subsection_star = SubsectionStar("content", None)
        >>> isinstance(subsection_star, SubsectionStar)
        True
    """
    prio_elem = True
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\subsection*")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'SubsectionStar', str]:
        pre,post = split_on_next(input,"\\subsection*")
        name,post = split_on_first_brace(post)
        return pre,SubsectionStar(name,parent),post

    def to_string(self) -> str:
        out = "\n# "+" "+ self.children[0].to_string()  + "\n"
        for child in self.children[1:]:
            out += child.to_string()
        #print("out ",out)
        return out


class Ref(Element):
    """Element for LaTeX \\ref reference.

    Example:
        >>> ref = Ref("content", None, "mylabel")
        >>> isinstance(ref, Ref)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        try:
            self.label_name = self.search_class(Document).globals.labels[label_ref]
        except Exception:
            self.label_name = "ref_error"
        self.label_ref = label_ref
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\ref")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Ref', str]:
        pre,post = split_on_next(input,"\\ref")
        label_ref,post = split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self) -> str:
        return "[](#"+self.label_ref+")"


class EqRef(Element):
    """Element for LaTeX \\eqref reference.

    Example:
        >>> eqref = EqRef("content", None, "eq1")
        >>> isinstance(eqref, EqRef)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        try:
            self.label_name = self.search_class(Document).globals.labels[label_ref]
        except Exception:
            self.label_name = "ref_error"
        self.label_ref = label_ref
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\eqref")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Ref', str]:
        pre,post = split_on_next(input,"\\eqref")
        label_ref,post = split_on_first_brace(post)
        return pre,Ref("",parent,label_ref),post

    def to_string(self) -> str:
        return "[](#"+self.label_ref+")"

class Proof(Element):
    """Element for LaTeX proof environment.

    Example:
        >>> proof = Proof("content", None)
        >>> isinstance(proof, Proof)
        True
    """
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
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Proof', str]:
        pre,content,post = begin_end_split(input,"\\begin{proof}","\\end{proof}")
        out = Proof(content,parent)
        out.expand([MystLabel])
        
        return pre,out,post

    def to_string(self) -> str:
        pre = f"\n:::{{prf:proof}} {self.name}\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = out.lstrip().rstrip()
        out = pre +out+ "\n:::\n"
        return out

    
class Textbf(Element):
    """Element for LaTeX \\textbf command.

    Example:
        >>> bold = Textbf("content", None)
        >>> isinstance(bold, Textbf)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\textbf")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Textbf', str]:
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
    """Element for LaTeX \\cite command.

    Example:
        >>> cite = Cite("content", None, ["ref1", "ref2"])
        >>> isinstance(cite, Cite)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element, citations: list[str]):
        super().__init__(modifiable_content,parent)
        self.citations = citations
    
    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\cite")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Cite', str]:
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
    """Element for LaTeX \\emph command.

    Example:
        >>> emph = Emph("content", None)
        >>> isinstance(emph, Emph)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\emph")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Emph', str]:
        pre,post = split_on_next(input,"\\emph")
        name,post = split_on_first_brace(post)
        return pre,Emph(name,parent),post

    def to_string(self) -> str:
        out = "*"
        for child in self.children:
            out += child.to_string()
        out += "*"
        return out
    

class Textit(Element):
    """Element for LaTeX \\textit command.

    Example:
        >>> textit = Textit("content", None)
        >>> isinstance(textit, Textit)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    @staticmethod
    def position(input: str) -> int:
        return position_of(input,"\\textit")

    @staticmethod
    def split_and_create(input: str, parent: Element) -> Tuple[str, 'Emph', str]:
        pre,post = split_on_next(input,"\\textit")
        name,post = split_on_first_brace(post)
        return pre,Emph(name,parent),post

    def to_string(self) -> str:
        out = "*"
        for child in self.children:
            out += child.to_string()
        out += "*"
        return out
    
    
class TheoremElement(SectionEnumerate):
    """Element for LaTeX theorem environments.

    Example:
        >>> thm = TheoremElement("content", None, "Theorem", "theorem", ["section"])
        >>> isinstance(thm, TheoremElement)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element, display_name: str, theorem_env_name: str, enum_parent_class):
        super().__init__(modifiable_content,parent,theorem_env_name,enum_parent_class)
        self.display_name = display_name
        theorem_type = "admonition"
        if display_name.lower() in PRF_TYPES.keys():
            theorem_type = PRF_TYPES[display_name.lower()]
        self.theorem_type = theorem_type

    def to_string(self) -> str:
        """Convert to Markdown theorem block.

        Returns:
            str: Markdown theorem block.
        """
        

        pre = "\n:::{"+self.theorem_type+"} "+f""
        out = ""
        for child in self.children:
            out += child.to_string()
        out = out.lstrip().rstrip()
        if out.startswith("["):
            _,middle,out = begin_end_split(out,"[","]")
            out = middle.strip()+"\n" + out.lstrip()
        else:
            out = "\n"+out.lstrip()
        out = pre + out
        
        out += "\n:::\n"
        return out


class TheoremSearcher():
    """Searcher for LaTeX theorem environments.

    Example:
        >>> searcher = TheoremSearcher("theorem", ["section"], "Theorem")
        >>> isinstance(searcher, TheoremSearcher)
        True
    """
    def __init__(self, theorem_env_name: str, enum_parent_class, display_name: str):
        self.display_name = display_name
        self.theorem_env_name = theorem_env_name
        self.enum_parent_class = enum_parent_class
    
    def position(self, input: str) -> int:
        """Find position of theorem environment.

        Args:
            input (str): Input string.

        Returns:
            int: Position index.
        """
        return position_of(input,"\\begin{" + self.theorem_env_name + "}")
            
    def split_and_create(self, input: str, parent: Element) -> Tuple[str, TheoremElement, str]:
        """Split string and create TheoremElement.

        Args:
            input (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, TheoremElement, str]: Pre-content, TheoremElement, post-content.
        """
        pre,content,post = begin_end_split(input,"\\begin{"+self.theorem_env_name+"}","\\end{"+self.theorem_env_name+"}")
        
        out = TheoremElement(content,parent,self.display_name,self.theorem_env_name,self.enum_parent_class)
        out.expand([MystLabel])
        
        return pre,out,post

def get_theoremSearchers(input: str) -> list:
    """Extract theorem searchers from LaTeX preamble.

    Args:
        input (str): LaTeX preamble string.

    Returns:
        list: List of TheoremSearcher instances.

    Example:
        >>> result = get_theoremSearchers(r"\\newtheorem{theorem}{Theorem}")
        >>> isinstance(result, list)
        True
    """
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

def get_number_within_equation(input: str) -> str:
    """Extract equation numbering context from LaTeX string.

    Args:
        input (str): LaTeX string.

    Returns:
        str: Numbering context or "document".

    Example:
        >>> get_number_within_equation("abc\\numberwithin{equation}{section}")
        'section'
    """
    input = input.split("\\numberwithin{equation}")
    if len(input) == 1:
        return "document" 
    out,_ = split_on_first_brace(input[1])
    return out

def get_all_filters() -> list:
    """Returns all section-related filter classes/searchers.

    Returns:
        list: List of filter classes/searchers.

    Example:
        >>> filters = get_all_filters()
        >>> isinstance(filters, list)
        True
    """
    return [SectionStar,Para,Chapter,Section,ChapterStar,SubsectionStar,Proof,Emph,Textbf,Textit,Ref,EqRef,Cite]
