"""Core filter classes and utilities for pytexmd.

This module provides the main classes and functions for parsing and processing LaTeX content,
including tree elements, searchers, and helpers for Markdown/MyST conversion.
"""

__all__ = [
    "Element",
    "Document",
    "Undefined",
    "RawText",
    "JunkSearcher",
    "ReplaceSearcher",
    "GuardianSearcher",
    "OneArgumentJunkSearcher",
    "OneArgumentCommandSearcher",
    "find_nearest_classes",
    "has_value_equal",
    "get_number_within_equation",
    "Searcher",
    "BeginEndSearcher",
    "SectionLikeSearcher",
    "SectionLike",
]

from typing import List, Optional, Tuple, Union, Callable,NamedTuple
from . import splitting

call_num = 0

class FileStructure():
    def __init__(self,file_name:str,content: str="",children:List["FileStructure"]=[]):
        self.file_name = file_name
        self.content = content
        self.children = children


class Element():
    """Base class for LaTeX tree elements.

    Attributes:
        children (List[Element] | None): Child elements.
        _modifiable_content (str): Content to be processed.
        parent (Element | None): Parent element.

    Example:
        >>> elem = Element("some content", None)
        >>> elem._modifiable_content
        'some content'
    """

    def __init__(self, modifiable_content: str, parent: Optional["Element"]):
        """Initialize an Element.

        Args:
            modifiable_content (str): Content to be processed.
            parent (Optional[Element]): Parent element.

        Example:
            >>> e = Element("abc", None)
            >>> e.parent is None
            True
        """
        self.children:List[Element]|None = None
        self._modifiable_content:str = ""
        self.parent:Element|None = None
        self._modifiable_content = modifiable_content
        self.parent = parent

    def hasattr(self, string: str) -> bool:
        """Check if the element has a given attribute.

        Args:
            string (str): Attribute name.

        Returns:
            bool: True if attribute exists, False otherwise.

        Example:
            >>> class Dummy(Element): pass
            >>> d = Dummy("x", None)
            >>> d.hasattr("_modifiable_content")
            True
        """
        try:
            object.__getattribute__(self,string)
            return True
        except AttributeError:
            return False

    def search_attribute_holder(self, string: str) -> Optional["Element"]:
        """Find the nearest ancestor with the given attribute.

        Args:
            string (str): Attribute name.

        Returns:
            Optional[Element]: Element holding the attribute, or None.

        Example:
            >>> class Dummy(Element): pass
            >>> d = Dummy("x", None)
            >>> d.search_attribute_holder("_modifiable_content") is d
            True
        """
        try:
            object.__getattribute__(self, string)
            return self
        except AttributeError:
            if self.parent is None:
                return None
            else:
                return self.parent.search_attribute_holder(string)

    def all_childs(self) -> List["Element"]:
        """Recursively collect all child elements.

        Returns:
            List[Element]: List of all child elements including self.

        Example:
            >>> e = Element("abc", None)
            >>> e.all_childs()[0] is e
            True
        """
        out = [self]
        if self.children is None:
            return out
        else:
            for child in self.children:
                out.extend(child.all_childs())
            return out

    def search_on_func(self, function: Callable[["Element"], bool]) -> Optional["Element"]:
        """Search ancestors using a predicate function.

        Args:
            function (Callable[[Element], bool]): Predicate function.

        Returns:
            Optional[Element]: First matching ancestor or None.

        Example:
            >>> e = Element("abc", None)
            >>> e.search_on_func(lambda x: True) is e
            True
        """
        if function(self):
            return self
        else:
            if self.parent is None:
                return None
            else:
                return self.parent.search_on_func(function)

    def search_class(self, searcher: type) -> Optional["Element"]:
        """Search ancestors for a specific class type.

        Args:
            searcher (type): Class type to search for.

        Returns:
            Optional[Element]: First matching ancestor or None.

        Example:
            >>> class Dummy(Element): pass
            >>> d = Dummy("x", None)
            >>> d.search_class(Dummy) is d
            True
        """
        if self.parent is None:
            if isinstance(self,searcher):
                return self
            else:
                return None
        else:
            if isinstance(self,searcher):
                return self
            else:
                return self.parent.search_class(searcher) 
    
    def search_up_on_func(self, function: Callable[["Element"], bool]) -> Optional["Element"]:
        """Search upwards in the tree for an element matching a predicate.

        Args:
            function (Callable[[Element], bool]): Predicate function.

        Returns:
            Optional[Element]: First matching element or None.

        Example:
            >>> class Dummy(Element): pass
            >>> d = Dummy("x", None)
            >>> d.search_up_on_func(lambda x: True) is d
            True
        """
        """
        if you are calling this function while the caller is not a child
        of his parent this will throw an error

        - during split_and_create the object will never be a child
        of his parent until it this function is finished!
        """
        if function(self):
            return self
        root = self.search_class(Document)
        all_childs = root.all_childs()
        split_on = -1
        for k,elem in enumerate(all_childs):
            if elem == self:
                split_on = k
                break
        #if split_on == -1:
        #    raise RuntimeError("FATAL ERROR couldn t find own class in roots all_childs " + str(self.__class__))
        all_childs = all_childs[:split_on]

        all_childs = all_childs[::-1]
        for elem in all_childs:
            if function(elem):
                return elem
        return None

    def __getattr__(self, name: str):
        """Get attribute from parent if not found in self.

        Args:
            name (str): Attribute name.

        Returns:
            Any: Attribute value or None.

        Example:
            >>> class Dummy(Element): pass
            >>> d = Dummy("x", None)
            >>> d.__getattr__("notfound") is None
            True
        """
        if self.parent is None:
            return None
            #raise AttributeError("No parent in the latex tree has the attribute " + name)
        else:
            return self.parent.__getattr__(name)
    
    def _finish_up(self) -> None:
        """Finalize the element by wrapping modifiable content in RawText.

        Example:
            >>> e = Element("abc", None)
            >>> e._finish_up()
            >>> isinstance(e.children[0], RawText)
            True
        """
        if self._modifiable_content != "":
            if self.children is None:
                self.children = []
            self.children.append(RawText(self._modifiable_content,self))
            self._modifiable_content = ""

        if self.children is None:
            self.children = [RawText(self._modifiable_content,self)]
                #print(type(self))
                #raise RuntimeError("something went wrong children is not none but _modifiable_content != \"")
        else:
            for child in self.children:
                child._finish_up()

    def expand(self, all_classes: List["Element"]) -> None:
        """Expand the element tree by processing children.

        Args:
            all_classes (List[Element]): List of element classes.

        Example:
            >>> class Dummy(Element): pass
            >>> e = Element("abc", None)
            >>> e.expand([Dummy])
        """
        global call_num 
        while True:
            call_num = call_num + 1

            if call_num % 100==0:
                print(".",end='')
        
            if call_num % 2000==0:
                print("\nnumber of expand calls ",call_num," ")
                
            if self._process_children(all_classes) == False:
                break


    def _process_children(self, all_classes: List["Element"]) -> bool:
        """Process children and update tree.

        Args:
            all_classes (List[Element]): List of element classes.

        Returns:
            bool: True if any child was updated, False otherwise.

        Example:
            >>> class Dummy(Element): pass
            >>> e = Element("abc", None)
            >>> e._process_children([Dummy])
            True
        """
        """
        #NOTE DO NOT OVERWRITE!!
        
        this function will return True if one child (or grant...grant child) has been updated
        """
        if self._modifiable_content != "":
            if self.children is None:
                self.children = []

            while self._modifiable_content != "":
                selected_classes = find_nearest_classes(self._modifiable_content,all_classes)
                if selected_classes == []:
                    if self.children == []:
                        self.children = None
                        return False
                    element = Undefined(self._modifiable_content,self)
                    self.children.append(element)
                    self._modifiable_content = ""
                else:
                    undefined_string,element,self._modifiable_content = selected_classes[0].split_and_create(self._modifiable_content,self)
                    
                    self.children.append(Undefined(undefined_string,self))
                    self.children.append(element)
            return True
        else:
            if self.children is None:
                return False
            out = False
            for child in self.children:
                out = out or child._process_children(all_classes)
            return out

    def to_string(self) -> str:
        """Output Markdown/MyST string.

        Returns:
            str: Markdown/MyST representation.

        Example:
            >>> class Dummy(Element):
            ...     def to_string(self): return "dummy"
            >>> Dummy("abc", None).to_string()
            'dummy'
        """
        raise NotImplementedError("no function to_string found")
    
    def to_file_structure(self,current_depth)->FileStructure|str:
        """Convert element to FileStructure representation.

        Returns:
            FileStructure | str: FileStructure or string representation.

        Example:
            >>> class Dummy(Element):
            ...     def to_structure(self): return "dummy"
            >>> Dummy("abc", None).to_structure()
            'dummy'
        """
        return self.to_string()


def get_number_within_equation(string: str) -> str:
    """Extract equation numbering context from LaTeX string.

    Args:
        string (str): LaTeX string.

    Returns:
        str: Numbering context or "document".

    Example:
        >>> get_number_within_equation("abc\\numberwithin{equation}{section}")
        'section'
    """
    string = string.split("\\numberwithin{equation}")
    if len(string) == 1:
        return "document" 
    out,_ = splitting.split_on_first_brace(string[1])
    return out

def has_value_equal(instance: Element, attribute_name: str, value) -> bool:
    """Check if an element's attribute equals a value.

    Args:
        instance (Element): Element instance.
        attribute_name (str): Attribute name.
        value: Value to compare.

    Returns:
        bool: True if attribute equals value, False otherwise.

    Example:
        >>> class Dummy(Element): pass
        >>> d = Dummy("x", None)
        >>> d.section_number = 5
        >>> has_value_equal(d, "section_number", 5)
        True
    """
    if instance.hasattr(attribute_name):
        return (object.__getattribute__(instance,attribute_name)==value)
    else:
        return False

def find_nearest_classes(string: str, all_classes: List[Element]) -> List[Element]:
    """Find nearest matching element classes in a string.

    Args:
        string (str): Input string.
        all_classes (List[Element]): List of element classes.

    Returns:
        List[Element]: List of nearest matching classes.

    Example:
        >>> class Dummy:
        ...     @staticmethod
        ...     def position(s): return s.find("x")
        >>> find_nearest_classes("abcxdef", [Dummy])
        [Dummy]
    """
    min_distance = 99999
    out = []
    for elem in all_classes:
        dist = elem.position(string)
        if dist == -1:
            continue
        else:
            if dist == min_distance:
                out.append(elem)
            if dist <= min_distance:
                min_distance = dist
                out = [elem]
        
    if out != []:
        for elem in out:
            try:
                if hasattr(elem, 'prio_elem'):
                    return [elem]
            except AttributeError:
                pass
    return out


class Searcher():
    """Base class for searchers to find LaTeX constructs.

    Example:
        >>> class DummySearcher(Searcher):
        ...     def position(self, s): return s.find("x")
        ...     def split_and_create(self, s, p): return "", Element("x", p), ""
        >>> ds = DummySearcher()
        >>> ds.position("abcxdef")
        3
    """
    def __init__(self):
        super().__init__()
    
    def position(self, string: str) -> int:
        """Find position of construct in string.

        Args:
            string (str): Input string.
        
        Returns:
            int: Position index, or -1 if not found.
        """
        raise NotImplementedError("no function position found")
    
    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Element, str]:
        """Split string and create element for construct.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, Element, str]: Pre-content, created element, post-content.
        """
        raise NotImplementedError("no function split_and_create found")
    
class BeginEndSearcher(Searcher):
    """Searcher for LaTeX environments with \begin and \end.

    Attributes:
        name (str): Environment name.
        save_split (bool): Whether to save the split command.

    Example:
        >>> searcher = BeginEndSearcher("itemize")
        >>> searcher.name
        'itemize'
    """
    def __init__(self, command_name: str, element_type:type, save_split: bool = True):
        """
        Args:
            name (str): Environment name.
            save_split (bool, optional): Whether to save the split command. Defaults to True.
        """
        super().__init__()
        self.command_name = command_name
        self.save_split = save_split
        self.element_type = element_type
    
    def position(self, string: str) -> int:
        return splitting.position_of(string,"\\begin{"+self.command_name+ "}",self.save_split)
    
    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Element, str]:
        pre,content,post = splitting.begin_end_split(string,"\\begin{"+self.command_name+"}","\\end{"+self.command_name+"}")
        out = self.element_type(content,parent)
        return pre,out,post

SECTION_LIKE_COMMANDS = [
    "\\part",
    "\\chapter",
    "\\section",
    "\\subsection",
    "\\subsubsection",
    "\\paragraph",
    "\\subparagraph"
]

SECTION_LIKE_COMMANDS_TO_HASHTAGS = {
    "\\part": "# ",
    "\\chapter": "# ",
    "\\section": "# ",
    "\\subsection": "## ",
    "\\subsubsection": "### ",
    "\\paragraph": "#### ",
    "\\subparagraph": "#### ",
    "\\part*": "# ",
    "\\chapter*": "# ",
    "\\section*": "# ",
    "\\subsection*": "## ",
    "\\subsubsection*": "### ",
    "\\paragraph*": "#### ",
    "\\subparagraph*": "#### ",
}
class SectionLike(Element):
    """Element for section-like LaTeX commands.

    """
    def __init__(self, modifiable_content:str, parent,command_name:str, name:str):
        super().__init__(modifiable_content,parent)
        self.name = name
        self.command_name = command_name

    def to_string(self) -> str:
        pre = "\n" + SECTION_LIKE_COMMANDS_TO_HASHTAGS[self.command_name] + self.name + "\n"
        out = ""
        for child in self.children:
            out += child.to_string()
        out = pre + out.lstrip()
        return out
    
    def to_file_structure(self,current_depth)->FileStructure:
        if current_depth <= 0:
            return self.to_string()
        
        out = ""
        childs = []
        for child in self.children:
            struct = child.to_file_structure(current_depth-1)
            if isinstance(struct,str):
                out += struct
            else:
                if struct.file_name is None:
                    out += struct.content
                    childs.extend(struct.children)
                else:
                    childs.append(struct)
        return FileStructure(self.name,out,childs)
        
class SectionLikeSearcher(Searcher):
    """Searcher for LaTeX commands.

    Attributes:
        name (str): Command name.
        save_split (bool): Whether to save the split command.
    """
    def __init__(self, command_name: str):
        """
        Args:
            name (str): Command name.
            save_split (bool, optional): Whether to save the split command. Defaults to True.
        """
        super().__init__()
        self.command_name = command_name
        
    
    def position(self, string: str) -> int:
        return splitting.position_of(string,self.command_name+"{",False)
    
    def split_and_create(self,input: str, parent: Element) -> Tuple[str, Element, str]:
        #TODO HANDLE NESTED SECTIONS AKA LEVEL DEPENDENCIES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        pre,content = splitting.split_on_next(input,self.command_name)
        name,content = splitting.split_on_first_brace(content)
        if self.command_name + "{" in content:
            content,post = splitting.split_on_next(content,self.command_name + "{",False)
            post = self.command_name + "{" + post
        else:
            post = ""
        
        return pre,SectionLike(content,parent,self.command_name,name),post

def get_section_like_filters() -> List[Searcher]:
    out = []
    for command in SECTION_LIKE_COMMANDS:
        out.append(SectionLikeSearcher(command))
        out.append(SectionLikeSearcher(command+"*"))
        
    return out

class Document(Element):
    """Element representing a LaTeX document."""
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
        

    @staticmethod
    def position(string: str) -> int:
        if "\\begin{document}" in string:
            return splitting.position_of(string,"\\begin{document}")
        else:
            return -1
        
    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'Document', str]:
        pre,content,post = splitting.begin_end_split(string,"\\begin{document}","\\end{document}")
        return pre,Document(content,parent),post

    def to_string(self) -> str:
        out = ""
        for child in self.children:
            out += child.to_string()
        return out

    def to_file_structure(self,current_depth)->FileStructure:
        if current_depth <= 0:
            return self.to_string()
        
        out = ""
        childs = []
        for child in self.children:
            struct = child.to_file_structure(current_depth-1)
            if isinstance(struct,str):
                out += struct
            else:
                childs.append(struct)
        return FileStructure(self.name,out,childs)
            
class Undefined(Element):
    """Element for undefined LaTeX content."""
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    def to_string(self) -> str:
        out = ""
        for child in self.children:
            out += child.to_string()
        return out

    def to_file_structure(self,current_depth)->FileStructure:
        if current_depth <= 0:
            return self.to_string()
        
        out = ""
        childs = []
        for child in self.children:
            struct = child.to_file_structure(current_depth)
            if isinstance(struct,str):
                out += struct
            else:
                childs.append(struct)
        return FileStructure(None,out,childs)

class RawText(Element):
    """Element for raw text content."""
    def __init__(self,string: str, parent: Element):
        super().__init__("",parent)
        self.text = string

    def to_string(self) -> str:
        return self.text


class JunkSearcher(Searcher):
    """Searcher for junk LaTeX commands."""
    def __init__(self,junk_name: str, save_split: bool = True):
        self.junk_name = junk_name
        self.save_split = save_split

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.junk_name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.junk_name,self.save_split)
        return pre,Undefined("",parent),post


class ReplaceSearcher(Searcher):
    """Searcher for replacing LaTeX commands."""
    def __init__(self,junk_name: str, replacement: str, save_split: bool = True):
        self.junk_name = junk_name
        self.replacement = replacement
        self.save_split = save_split

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.junk_name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.junk_name,self.save_split)
        return pre,Undefined(self.replacement,parent),post

class GuardianSearcher(Searcher):
    """Searcher for guarding LaTeX commands."""
    def __init__(self,name: str, save_split: bool = True):
        self.name = name
        self.save_split = save_split

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, RawText, str]:
        pre,post = splitting.split_on_next(string,self.name,self.save_split)
        return pre,RawText(self.name,parent),post


class OneArgumentJunkSearcher(Searcher):
    """Searcher for junk commands with one argument."""
    def __init__(self, command_name: str, begin_brace: str = "{", end_brace: str = "}"):
        self.command_name,self.begin,self.end = command_name,begin_brace,end_brace

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.command_name)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.command_name)
        name,post = splitting.split_on_first_brace(post,self.begin,self.end)
        return pre,Undefined("",parent),post

class OneArgumentCommandSearcher(Searcher):
    """Searcher for commands with one argument."""
    def __init__(self, command_name: str, begin: str, end: str):
        self.command_name,self.begin,self.end = command_name,begin,end

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.command_name)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.command_name)
        name,post = splitting.split_on_first_brace(post)
        return pre,Undefined(self.begin + name + self.end,parent),post

