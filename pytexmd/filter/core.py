
__all__ = ["Element","Document","Undefined","RawText","Globals","JunkSearch","ReplaceSearch","GuardianSearch","OneArgumentJunkSearch","OneArgumentCommandSearch","Label","SectionEnumerate"]

from typing import List, Optional, Tuple, Union, Callable
from . import splitting

TAB = "    "
call_num = 0

class Element():
    
    def __init__(self):
        self.children:List[Element]|None = None
        self._modifiable_content:str = ""
        self.parent:Element|None = None
    
    def hasattr(self, string:str)->bool:
        try:
            object.__getattribute__(self,string)
            return True
        except AttributeError:
            return False

    def search_attribute_holder(self, string:str)->Optional["Element"]:
        try:
            object.__getattribute__(self, string)
            return self
        except AttributeError:
            if self.parent is None:
                return None
            else:
                return self.parent.search_attribute_holder(string)

    def all_childs(self)->List["Element"]:
        out = [self]
        if self.children is None:
            return out
        else:
            for child in self.children:
                out.extend(child.all_childs())
            return out

    def search_on_func(self, function:Callable[["Element"],bool])->Optional["Element"]:
        if function(self):
            return self
        else:
            if self.parent is None:
                return None
            else:
                return self.parent.search_on_func(function)

    def search_class(self, searcher:type)->Optional["Element"]:
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
    
    def search_up_on_func(self, function:Callable[["Element"],bool])->Optional["Element"]:
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

    def __getattr__(self, name):
        """if hasattr(self, string):
            return self.__getattr__(name)
        """
        if self.parent is None:
            return None
            #raise AttributeError("No parent in the latex tree has the attribute " + name)
        else:
            return self.parent.__getattr__(name)
    
    def __init__(self, modifiable_content:str, parent:Optional["Element"]):
        """
        #NOTE PLEASE CALL super().__init__(pre_content,modifiable_content)
        in your child class

        string 
        """
        self._modifiable_content = modifiable_content
        self.parent = parent

    def _finish_up(self):
        """
        this function will be called at the very end 
        it puts modifable_content into an RawText wrapper
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

    def expand(self,all_classes:List["Element"]):
        global call_num 
        while True:
            call_num = call_num + 1

            if call_num % 100==0:
                print(".",end='')
        
            if call_num % 2000==0:
                print("\nnumber of expand calls ",call_num," ")
                
            if self._process_children(all_classes) == False:
                break


    def _process_children(self,all_classes):
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

    def to_string(self,tab_level:int)->str:
        """
        Output markdown myst string.
        """
        raise NotImplementedError("no function to_string found")


def find_nearest_classes(string: str, all_classes: List[Element]) -> List[Element]:
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
    """
    SectionEnumerate Searcher need to implement 
        
    def theorem_enviroment_name(self):
        return "document"

    """
    section_count = 0
    equation_count = 0
    
    def __init__(self, modifiable_content:str, parent, theorem_env_name, enum_parent_class):
        super().__init__(modifiable_content,parent)
        if (not isinstance(enum_parent_class,list)) and (not enum_parent_class is None):            
            enum_parent_class = [enum_parent_class]
        self.enum_parent_class = enum_parent_class
        self.theorem_env_name = theorem_env_name
    
    def label_name(self)->str:
        return self.get_section_enum()[:-1]

    def try_get_section_enum(self,class_name):
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

    def get_section_enum(self):

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

    def generate_child_equation_number(self):
        equation_number = self.equation_count + 1
        self.equation_count = self.equation_count + 1
        return equation_number

    def generate_child_section_number(self):
        section_number = self.section_count + 1
        self.section_count = self.section_count + 1
        return section_number

class Document(SectionEnumerate):
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

    def to_string(self,tab_level: int) -> str:
        """
        Output markdown myst string for document.
        """
        out = ""
        for child in self.children:
            out += child.to_string(tab_level)
        return out

class Undefined(Element):
    def __init__(self,modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)

    def to_string(self,tab_level: int) -> str:
        """
        Output markdown myst string for undefined content.
        """
        out = ""
        for child in self.children:
            out += child.to_string(tab_level)
        return out

class RawText(Element):
    def __init__(self,string: str, parent: Element):
        super().__init__("",parent)
        self.text = string

    def to_string(self, tab_level: int) -> str:
        """
        Output markdown myst string for raw text.
        """
        return tab_level+self.text

class Globals():
    pass

class JunkSearch():
    def __init__(self,junk_name: str, save_split: bool = True):
        self.junk_name = junk_name
        self.save_split = save_split

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.junk_name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.junk_name,self.save_split)
        return pre,Undefined("",parent),post


class ReplaceSearch():
    def __init__(self,junk_name: str, replacement: str, save_split: bool = True):
        self.junk_name = junk_name
        self.replacement = replacement
        self.save_split = save_split

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.junk_name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.junk_name,self.save_split)
        return pre,Undefined(self.replacement,parent),post

class GuardianSearch():
    def __init__(self,name: str, save_split: bool = True):
        self.name = name
        self.save_split = save_split

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.name,self.save_split)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, RawText, str]:
        pre,post = splitting.split_on_next(string,self.name,self.save_split)
        return pre,RawText(self.name,parent),post


class OneArgumentJunkSearch():
    def __init__(self, command_name: str, begin_brace: str = "{", end_brace: str = "}"):
        self.command_name,self.begin,self.end = command_name,begin_brace,end_brace

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.command_name)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.command_name)
        name,post = splitting.split_on_first_brace(post,self.begin,self.end)
        return pre,Undefined("",parent),post

class OneArgumentCommandSearch():
    def __init__(self, command_name: str, begin: str, end: str):
        self.command_name,self.begin,self.end = command_name,begin,end

    def position(self, string: str) -> int:
        return splitting.position_of(string,self.command_name)

    def split_and_create(self, string: str, parent: Element) -> Tuple[str, Undefined, str]:
        pre,post = splitting.split_on_next(string,self.command_name)
        name,post = splitting.split_on_first_brace(post)
        return pre,Undefined(self.begin + name + self.end,parent),post


class Label(Element):
    def __init__(self, modifiable_content: str, parent: Element, label_ref: str):
        super().__init__(modifiable_content, parent)
        
        if not hasattr(self.search_class(Document).globals,"labels"):
            self.search_class(Document).globals.labels = {}
        
        holder = self.search_attribute_holder("label_name")
        label_name = "label_error"
        if not holder is None:
            label_name = holder.label_name()
        self.search_class(Document).globals.labels[label_ref] = label_name
    
    @staticmethod
    def position(string: str) -> int:
        return splitting.position_of(string,"\\label")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> Tuple[str, 'Label', str]:
        pre,post = splitting.split_on_next(string,"\\label")
        label_ref,post = splitting.split_on_first_brace(post)
        return pre,Label("",parent,label_ref),post

    def to_string(self) -> str:
        return ""