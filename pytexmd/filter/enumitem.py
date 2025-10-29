__all__ = ["Itemize","ItemizeItem","Enumeration","EnumerationItem"]

from .core import *
from .splitting import * 



#enum_styles = {"\\roman":enum_style_roman,"\\Roman":enum_style_Roman,"\\arabic":enum_style_arabic,"\\alph":enum_style_alph,"\\Alph":enum_style_Alph}


class ItemizeItem(Element):
    """
    Represents an item in a LaTeX itemize environment.

    Example:
        >>> item = ItemizeItem("First item", None)
        >>> print(item.to_string())
        •  First item
    """
    def __init__(self, modifiable_content: str, parent: Element, rename_item: str = "*"):
        super().__init__("",parent)
        self.rename_item = rename_item

        self.children = [Undefined(self.rename_item,self),Undefined(modifiable_content,self)]

    def label_name(self) -> str:
        """
        Returns the label of the item.

        Returns:
            str: The label.

        Example:
            >>> item = ItemizeItem("abc", None)
            >>> item.label_name()
            '•'
        """
        return self.rename_item#self.children[0].to_string()

    def to_string(self) -> str:
        """
        Converts the item to a formatted string.

        Returns:
            str: The formatted item string.

        Example:
            >>> item = ItemizeItem("abc", None)
            >>> isinstance(item.to_string(), str)
            True
        """
        #string_len = len(self.children[0].to_string()) + 2 

        
        out = self.children[0].to_string()+" "
        tmp = self.children[1].to_string().lstrip().rstrip()
        for i, line in enumerate(tmp.split("\n")):
            if i==0:
                out += line.strip() + "\n"
            else:
                out += "   " + line.strip() + "\n"
        out = out.rstrip()
        return out

    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\item' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.

        Example:
            >>> ItemizeItem.position("\\item abc")
            0
        """
        return position_of(string,"\\item")
            
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Splits the string on '\\item' and creates an ItemizeItem.

        Args:
            string (str): The input string.
            parent (Element): The parent element.

        Returns:
            tuple: (pre, ItemizeItem, post)

        Example:
            >>> pre, item, post = ItemizeItem.split_and_create("\\item abc", None)
            >>> isinstance(item, ItemizeItem)
            True
        """
        pre,content = split_on_next(string,"\\item")

        if "\\item" in content:
            content,post = split_on_next(content,"\\item")
            post = "\\item" + post
        else:
            post = ""

        rename_item = ""
        if first_char_brace(content,"["):
            rename_item,content = split_on_first_brace(content,"[","]")
        elem_out = ItemizeItem(content,parent,rename_item)

        return pre,elem_out,post

class Itemize(Element):
    """
    Represents a LaTeX itemize environment.

    Example:
        >>> itemize = Itemize("content", None)
        >>> isinstance(itemize.to_string(), str)
        True
    """
    current_index = 0
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): The content of the itemize.
            parent (Element): The parent element.

        Example:
            >>> itemize = Itemize("abc", None)
            >>> isinstance(itemize, Itemize)
            True
        """
        super().__init__(modifiable_content,parent)
        
    def to_string(self) -> str:
        """
        Converts the itemize to a formatted string.

        Returns:
            str: The formatted itemize string.

        Example:
            >>> itemize = Itemize("abc", None)
            >>> isinstance(itemize.to_string(), str)
            True
        """
        out = "\n" 
        for child in self.children:
            out += child.to_string().rstrip().lstrip() + "\n"
        return out
    
    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\begin{itemize}' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.

        Example:
            >>> Itemize.position("\\begin{itemize}abc")
            0
        """
        return position_of(string,"\\begin{itemize}")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Splits the string on itemize environment and creates an Itemize.

        Args:
            string (str): The input string.
            parent (Element): The parent element.

        Returns:
            tuple: (pre, Itemize, post)

        Example:
            >>> pre, itemize, post = Itemize.split_and_create("\\begin{itemize}abc\\end{itemize}", None)
            >>> isinstance(itemize, Itemize)
            True
        """
        
        pre,content,post = begin_end_split(string,"\\begin{itemize}","\\end{itemize}")
        
        elem_out = Itemize(content,parent)
        elem_out.expand([ItemizeItem])

        return pre,elem_out,post


class EnumerationItem(Element):
    """
    Represents an item in a LaTeX enumerate environment.

    Example:
        >>> enum_item = EnumerationItem("First", None)
        >>> isinstance(enum_item.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element, rename_item: str = None):
        """
        Args:
            modifiable_content (str): The content of the item.
            parent (Element): The parent element.
            rename_item (str, optional): The label for the item.

        Example:
            >>> enum_item = EnumerationItem("abc", None)
            >>> enum_item.label
            ''
        """
        super().__init__("",parent)
        modifiable_content = modifiable_content.lstrip().rstrip()
        self.rename_item = ""
        if rename_item is None:
            enumeration: Enumeration = self.search_class(Enumeration)
            self.rename_item = enumeration.generate_item_label()
        else:
            self.rename_item = rename_item

        self.rename_item_str = None
        if modifiable_content.startswith("\\label"):
            label,modifiable_content = split_on_first_brace(modifiable_content[len("\\label"):],"{" ,"}")
            self.rename_item_str = label_call(label,LabelType.ENUMERATION_ITEM,self.rename_item)
        self.children = [Undefined(self.rename_item, self), Undefined(modifiable_content, self)]

    def label_name(self) -> str:
        """
        Returns the label of the enumeration item.

        Returns:
            str: The label.

        Example:
            >>> enum_item = EnumerationItem("abc", None)
            >>> enum_item.label_name()
            ''
        """
        return self.rename_item

    def to_string(self) -> str: 
        out = ""
        if self.rename_item_str is None:
            out = self.children[0].to_string().strip()+" "
        else:
            out = self.children[0].to_string().strip()+" "+"(" + self.rename_item_str + ")=\n   " 
        tmp = self.children[1].to_string().lstrip().rstrip()
        for i, line in enumerate(tmp.split("\n")):
            if i==0:
                out += line.strip() + "\n"
            else:
                out += "   " + line.strip() + "\n"
        out = out.rstrip()
        return out

    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\item' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.

        Example:
            >>> EnumerationItem.position("\\item abc")
            0
        """
        return position_of(string,"\\item")
            
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Splits the string on '\\item' and creates an EnumerationItem.

        Args:
            string (str): The input string.
            parent (Element): The parent element.

        Returns:
            tuple: (pre, EnumerationItem, post)

        Example:
            >>> pre, enum_item, post = EnumerationItem.split_and_create("\\item abc", None)
            >>> isinstance(enum_item, EnumerationItem)
            True
        """
        pre,content = split_on_next(string,"\\item")

        if "\\item" in content:
            content,post = split_on_next(content,"\\item")
            post = "\\item" + post
        else:
            post = ""


        rename_item = None
        if first_char_brace(content,"["):
            rename_item,content = split_on_first_brace(content,"[","]")
        elem_out = EnumerationItem(content,parent,rename_item)

        return pre,elem_out,post
       
class Enumeration(Element):
    """
    Represents a LaTeX enumerate environment.

    Example:
        >>> enum = Enumeration("content", None, enum_style_arabic, "(", ")")
        >>> isinstance(enum.to_string(), str)
        True
    """
    def __init__(self, modifiable_content: str, parent: Element,start):
        """
        
        Example:
            >>> enum = Enumeration("abc", None, enum_style_arabic, "(", ")")
            >>> isinstance(enum, Enumeration)
            True
        """
        super().__init__(modifiable_content,parent)
        self.current_index = start
    
    def generate_item_label(self) -> str:
        out = str(self.current_index) + "."
        self.current_index += 1
        return out

    def to_string(self) -> str:
        """
        Converts the enumerate to a formatted string.

        Returns:
            str: The formatted enumerate string.

        Example:
            >>> enum = Enumeration("abc", None, enum_style_arabic, "(", ")")
            >>> isinstance(enum.to_string(), str)
            True
        """
        out = "\n" 
        for child in self.children:
            out += child.to_string().rstrip().lstrip() + "\n"
        return out
    
    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\begin{enumerate}' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.

        Example:
            >>> Enumeration.position("\\begin{enumerate}abc")
            0
        """
        return position_of(string,"\\begin{enumerate}")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        """
        Splits the string on enumerate environment and creates an Enumeration.

        Args:
            string (str): The input string.
            parent (Element): The parent element.

        Returns:
            tuple: (pre, Enumeration, post)

        Example:
            >>> pre, enum, post = Enumeration.split_and_create("\\begin{enumerate}abc\\end{enumerate}", None)
            >>> isinstance(enum, Enumeration)
            True
        """
        
        pre,content,post = begin_end_split(string,"\\begin{enumerate}","\\end{enumerate}")
        content = content.lstrip().rstrip()
        start = 1
        if content.startswith("["):
            _pre,_content,_post =begin_end_split(content,"[","]")
            content = _post.lstrip().rstrip()
            if "label" in _content:
                label_str = _content.split("label")[1].split("=")[1].strip().split(",")[0].strip()
                # Here you could implement parsing of label_str to set style_func, left, right
            if "start" in _content:
                start_str = _content.split("start")[1].split("=")[1].strip().split(",")[0].strip()
                try:
                    start = int(start_str)
                except:
                    start = 1
        elem_out = Enumeration(content,parent,start)
        elem_out.expand([EnumerationItem])

        return pre,elem_out,post


def get_all_filters():
    """
    Returns all filter classes for enum environments.

    Returns:
        list: List of filter classes.

    Example:
        >>> filters = get_all_filters()
        >>> isinstance(filters, list)
        True
    """
    return [Itemize, Enumeration]