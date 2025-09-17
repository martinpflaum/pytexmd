class Para(SectionEnumerate):
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
