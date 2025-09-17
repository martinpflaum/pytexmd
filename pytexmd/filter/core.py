"""Core filter classes and utilities for pytexmd.

This module provides the main classes and functions for parsing and processing LaTeX content,
including tree elements, searchers, and helpers for Markdown/MyST conversion.
"""

__all__ = [
    "Element",
    "Document",
    "Undefined",
    "RawText",
    "Globals",
    "JunkSearch",
    "ReplaceSearch",
    "GuardianSearch",
    "OneArgumentJunkSearch",
    "OneArgumentCommandSearch",
    "SectionEnumerate",
    "find_nearest_classes",
    "has_value_equal",
    "TAB",
    "get_number_within_equation"
]

from typing import List, Optional, Tuple, Union, Callable
from . import splitting

TAB = "    "
call_num = 0

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

class SectionEnumerate(Element):
    """Element for section and equation enumeration.

    Attributes:
        section_count (int): Section counter.
        equation_count (int): Equation counter.
        enum_parent_class (list): Parent classes for enumeration.
        theorem_env_name (str): Theorem environment name.

    Example:
        >>> class Dummy(SectionEnumerate):
        ...     def __init__(self): super().__init__("", None, "dummy", None)
        >>> d = Dummy()
        >>> d.generate_child_section_number()
        1
    """
    section_count = 0
    equation_count = 0
    
    def __init__(self, modifiable_content:str, parent, theorem_env_name, enum_parent_class):
        super().__init__(modifiable_content,parent)
        if (not isinstance(enum_parent_class,list)) and (not enum_parent_class is None):            
            enum_parent_class = [enum_parent_class]
        self.enum_parent_class = enum_parent_class
        self.theorem_env_name = theorem_env_name
    
    
    def try_get_section_enum(self, class_name) -> Optional[str]:
        """Try to get section enumeration for a class.

        Args:
            class_name: Class name.

        Returns:
            Optional[str]: Section enumeration string or None.
        """
        if class_name is None:
            return str(self.section_number) + "."
        else:
            search_func = lambda instance : has_value_equal(instance,"theorem_env_name",class_name)

            section_enum = self.search_up_on_func(search_func)
            
            if section_enum is None:
                return None
            else:
                out = section_enum.get_section_enum()
                out += str(self.section_number) + "."
                return out

    def get_section_enum(self) -> str:
        """Get section enumeration string.

        Returns:
            str: Section enumeration.
        """
        if self.enum_parent_class is None:
            return str(self.section_number) + "."
        else:
            out = None
            for elem in self.enum_parent_class:
                out = self.try_get_section_enum(elem)
                if not out is None:
                    break
            if out is None:
                out = "E"
                print("couldn't find enumaration parent: --"+self.enum_parent_class +"-- in enviroment: --" + self.theorem_env_name +"--")
            return out

    def generate_child_equation_number(self) -> int:
        """Generate next equation number.

        Returns:
            int: Equation number.
        """
        equation_number = self.equation_count + 1
        self.equation_count = self.equation_count + 1
        return equation_number

    def generate_child_section_number(self) -> int:
        """Generate next section number.

        Returns:
            int: Section number.
        """
        section_number = self.section_count + 1
        self.section_count = self.section_count + 1
        return section_number

class Document(SectionEnumerate):
    """Element representing a LaTeX document."""
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent,"document",None)
        self.globals = Globals()
    

    def get_section_enum(self) -> str:
        return ""

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

class Undefined(Element):
    """Element for undefined LaTeX content."""
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    def to_string(self) -> str:
        out = ""
        for child in self.children:
            out += child.to_string()
        return out

class RawText(Element):
    """Element for raw text content."""
    def __init__(self,string: str, parent: Element):
        super().__init__("",parent)
        self.text = string

    def to_string(self) -> str:
        return self.text

class Globals():
    """Global settings for document parsing."""
    pass

class JunkSearch():
    """Searcher for junk LaTeX commands."""
    def __init__(self,junk_name: str, save_split: bool = True):
        self.junk_name = junk_name
        self.save_split = save_split

    def position(self, string: str) -> int:
        """Find position of junk command in string.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return splitting.position_of(string,self.junk_name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        """Split string and create Undefined element for junk.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, Undefined, str]: Pre-content, Undefined element, post-content.
        """
        pre,post = splitting.split_on_next(string,self.junk_name,self.save_split)
        return pre,Undefined("",parent),post


class ReplaceSearch():
    """Searcher for replacing LaTeX commands."""
    def __init__(self,junk_name: str, replacement: str, save_split: bool = True):
        self.junk_name = junk_name
        self.replacement = replacement
        self.save_split = save_split

    def position(self, string: str) -> int:
        """Find position of command to replace.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return splitting.position_of(string,self.junk_name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        """Split string and create Undefined element with replacement.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, Undefined, str]: Pre-content, Undefined element, post-content.
        """
        pre,post = splitting.split_on_next(string,self.junk_name,self.save_split)
        return pre,Undefined(self.replacement,parent),post

class GuardianSearch():
    """Searcher for guarding LaTeX commands."""
    def __init__(self,name: str, save_split: bool = True):
        self.name = name
        self.save_split = save_split

    def position(self, string: str) -> int:
        """Find position of guardian command.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return splitting.position_of(string,self.name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, RawText, str]:
        """Split string and create RawText element for guardian.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, RawText, str]: Pre-content, RawText element, post-content.
        """
        pre,post = splitting.split_on_next(string,self.name,self.save_split)
        return pre,RawText(self.name,parent),post


class OneArgumentJunkSearch():
    """Searcher for junk commands with one argument."""
    def __init__(self, command_name: str, begin_brace: str = "{", end_brace: str = "}"):
        self.command_name,self.begin,self.end = command_name,begin_brace,end_brace

    def position(self, string: str) -> int:
        """Find position of command.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return splitting.position_of(string,self.command_name)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        """Split string and create Undefined element for one-argument junk.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, Undefined, str]: Pre-content, Undefined element, post-content.
        """
        pre,post = splitting.split_on_next(string,self.command_name)
        name,post = splitting.split_on_first_brace(post,self.begin,self.end)
        return pre,Undefined("",parent),post

class OneArgumentCommandSearch():
    """Searcher for commands with one argument."""
    def __init__(self, command_name: str, begin: str, end: str):
        self.command_name,self.begin,self.end = command_name,begin,end

    def position(self, string: str) -> int:
        """Find position of command.

        Args:
            string (str): Input string.

        Returns:
            int: Position index.
        """
        return splitting.position_of(string,self.command_name)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        """Split string and create Undefined element for one-argument command.

        Args:
            string (str): Input string.
            parent (Element): Parent element.

        Returns:
            Tuple[str, Undefined, str]: Pre-content, Undefined element, post-content.
        """
        pre,post = splitting.split_on_next(string,self.command_name)
        name,post = splitting.split_on_first_brace(post)
        return pre,Undefined(self.begin + name + self.end,parent),post

