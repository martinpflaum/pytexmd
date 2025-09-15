__all__ = ["Itemize","ItemizeItem","Enumeration","EnumerationItem"]

from .core import *
from .splitting import * 

def enum_style_roman(index: int) -> str:
    """
    Converts an index to an uppercase Roman numeral.

    Args:
        index (int): The index to convert.

    Returns:
        str: Uppercase Roman numeral.

    Example:
        ```python
        enum_style_roman(2)  # 'III'
        ```
    """
    roman = ["i","ii","iii","iv","v","vi","vii","viii","ix","x",
         "xi","xii","xiii","xiv","xv","xvi","xvii","xviii","xix","xx",
         "xxi","xxii","xxiii","xxiv","xxv","xxvi","xxvii","xxviii","xxix","xxx"]
    
    return roman[index].upper()

def enum_style_Roman(index: int) -> str:
    """
    Converts an index to an uppercase Roman numeral.

    Args:
        index (int): The index to convert.

    Returns:
        str: Uppercase Roman numeral.

    Example:
        ```python
        enum_style_Roman(0)  # 'I'
        ```
    """
    #roman = ["i","ii","iii","iv","v","vi","vii","viii","ix","x"]
    roman = ["I","II","III","IV","V","VI","VII","VIII","IX","X",
         "XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX",
         "XXI","XXII","XXIII","XXIV","XXV","XXVI","XXVII","XXVIII","XXIX","XXX"]
    return roman[index]

def enum_style_arabic(index: int) -> str:
    """
    Converts an index to an Arabic numeral (1-based).

    Args:
        index (int): The index to convert.

    Returns:
        str: Arabic numeral as string.

    Example:
        ```python
        enum_style_arabic(0)  # '1'
        ```
    """
    return str(index + 1)

def enum_style_alph(index: int) -> str:
    """
    Converts an index to a lowercase alphabet letter.

    Args:
        index (int): The index to convert.

    Returns:
        str: Lowercase letter.

    Example:
        ```python
        enum_style_alph(0)  # 'a'
        ```
    """
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    return lowercase[index]

def enum_style_Alph(index: int) -> str:
    """
    Converts an index to an uppercase alphabet letter.

    Args:
        index (int): The index to convert.

    Returns:
        str: Uppercase letter.

    Example:
        ```python
        enum_style_Alph(0)  # 'A'
        ```
    """
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return uppercase[index]

def enum_style_empty(index: int) -> str:
    """
    Returns an empty string for the label.

    Args:
        index (int): The index (unused).

    Returns:
        str: Empty string.

    Example:
        ```python
        enum_style_empty(0)  # ''
        ```
    """

    return ""

enum_styles = {"\\roman":enum_style_roman,"\\Roman":enum_style_Roman,"\\arabic":enum_style_arabic,"\\alph":enum_style_alph,"\\Alph":enum_style_Alph}


class ItemizeItem(Element):
    """
    Represents an item in a LaTeX itemize environment.

    Example:
        ```python
        item = ItemizeItem("First item", parent)
        print(item.to_string())
        ```
    """
    def __init__(self, modifiable_content: str, parent: Element, label: str = "•"):
        """
        Args:
            modifiable_content (str): The content of the item.
            parent (Element): The parent element.
            label (str, optional): The label for the item. Defaults to "•".
        """
        super().__init__("",parent)
        self.label = label

        self.children = [Undefined(label,self),Undefined(modifiable_content,self)]
    
    def label_name(self) -> str:
        """
        Returns the label of the item.

        Returns:
            str: The label.
        """
        return self.label#self.children[0].to_string()

    def to_string(self) -> str:
        """
        Converts the item to a formatted string.

        Returns:
            str: The formatted item string.
        """
        out = self.children[0].to_string()+"  "
        string_len = len(self.children[0].to_string()) + 2 

        self.children = self.children[1:]
        for child in self.children:
            out += child.to_string().lstrip().rstrip()+"\n"
        out = out.replace("\n","\n"+ " " * string_len)
        return out

    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\item' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.
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
        """
        pre,content = split_on_next(string,"\\item")

        if "\\item" in content:
            content,post = split_on_next(content,"\\item")
            post = "\\item" + post
        else:
            post = ""

        label = ""
        if first_char_brace(content,"["):
            label,content = split_on_first_brace(content,"[","]")
        elem_out = ItemizeItem(content,parent,label)
        
        return pre,elem_out,post

class Itemize(Element):
    """
    Represents a LaTeX itemize environment.

    Example:
        ```python
        itemize = Itemize("content", parent)
        print(itemize.to_string())
        ```
    """
    current_index = 0
    def __init__(self, modifiable_content: str, parent: Element):
        """
        Args:
            modifiable_content (str): The content of the itemize.
            parent (Element): The parent element.
        """
        super().__init__(modifiable_content,parent)
        
    def to_string(self) -> str:
        """
        Converts the itemize to a formatted string.

        Returns:
            str: The formatted itemize string.
        """
        out = "\n" 
        for child in self.children:
            out += child.to_string().rstrip().lstrip() + "\n"
        out = out.replace("\n","\n"+TAB)
        return out
    
    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\begin{itemize}' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.
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
        """
        
        pre,content,post = begin_end_split(string,"\\begin{itemize}","\\end{itemize}")
        
        elem_out = Itemize(content,parent)
        elem_out.expand([ItemizeItem])

        return pre,elem_out,post


class EnumerationItem(Element):
    """
    Represents an item in a LaTeX enumerate environment.

    Example:
        ```python
        enum_item = EnumerationItem("First", parent)
        print(enum_item.to_string())
        ```
    """
    def __init__(self, modifiable_content: str, parent: Element, label: str = None):
        """
        Args:
            modifiable_content (str): The content of the item.
            parent (Element): The parent element.
            label (str, optional): The label for the item.
        """
        super().__init__("",parent)

        self.label = ""
        if label is None:
            enumeration = self.search_class(Enumeration)
            self.label = enumeration.generate_item_label()
        else:
            self.label = label
            
        self.children = [Undefined(self.label,self),Undefined(modifiable_content,self)]
    
    def label_name(self) -> str:
        """
        Returns the label of the enumeration item.

        Returns:
            str: The label.
        """
        return self.label

    def to_string(self) -> str:
        
        out = self.children[0].to_string()+"  "
        string_len = len(self.children[0].to_string()) + 2 

        self.children = self.children[1:]
        for child in self.children:
            out += child.to_string().lstrip().rstrip()+"\n"
        out = out.replace("\n","\n"+ " " * string_len)
        return out

    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\item' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.
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
        """
        pre,content = split_on_next(string,"\\item")

        if "\\item" in content:
            content,post = split_on_next(content,"\\item")
            post = "\\item" + post
        else:
            post = ""

        label = None
        if first_char_brace(content,"["):
            label,content = split_on_first_brace(content,"[","]")
        elem_out = EnumerationItem(content,parent,label)
        
        return pre,elem_out,post
       
class Enumeration(Element):
    """
    Represents a LaTeX enumerate environment.

    Example:
        ```python
        enum = Enumeration("content", parent, enum_style_arabic, "(", ")")
        print(enum.to_string())
        ```
    """
    current_index = 0
    def __init__(self, modifiable_content: str, parent: Element, style_func: callable, left: str, right: str):
        """
        Args:
            modifiable_content (str): The content of the enumerate.
            parent (Element): The parent element.
            style_func (callable): Function to generate item labels.
            left (str): Left delimiter for label.
            right (str): Right delimiter for label.
        """
        super().__init__(modifiable_content,parent)
        self.style_func,self.left,self.right = style_func,left,right

    def to_string(self) -> str:
        """
        Converts the enumerate to a formatted string.

        Returns:
            str: The formatted enumerate string.
        """
        out = "\n" 
        for child in self.children:
            out += child.to_string().rstrip().lstrip() + "\n"
        out = out.replace("\n","\n"+TAB)
        return out
    
    @staticmethod
    def position(string: str) -> int:
        """
        Finds the position of '\\begin{enumerate}' in the string.

        Args:
            string (str): The input string.

        Returns:
            int: The position index.
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
        """
        
        pre,content,post = begin_end_split(string,"\\begin{enumerate}","\\end{enumerate}")
        
        style_func = None
        left = ""
        right = ""
        
        if first_char_brace(content,"["):
            options,content = split_on_first_brace(content,"[","]")
            options_pre,options_post = split_on_next(options,"label")
            options_post = options_post.lstrip()
            options_post = options_post[1:]#remove = 
            options_label = ""
            if first_char_brace(options_post,"{"):
                options_label,options_post = split_on_first_brace(options_post)
            
            tmp = options_post.split(",")[0]
            options_label = options_label + tmp
            
            for style in enum_styles.keys():
                if style in options_label:
                    style_func = enum_styles[style]
                    tmp = options_label.split(style)
                    left = tmp[0]
                    _,right = split_on_next(tmp[1],"*")
                    break 

            if style_func is None:
                style_func = enum_style_empty
                left = options_label
        else:
            style_func = enum_style_arabic
            right = "."

        left = left.replace("\\sffamily","")
        left = left.replace("{","")
        left = left.replace("}","")
        
        right = right.replace("\\sffamily","")
        right = right.replace("{","")
        right = right.replace("}","")
        

        elem_out = Enumeration(content,parent,style_func,left,right)
        elem_out.expand([EnumerationItem])

        return pre,elem_out,post

    def generate_item_label(self) -> str:
        """
        Generates the label for the next item.

        Returns:
            str: The generated label.
        """
        self.current_index = self.current_index + 1
        return self.left + self.style_func(self.current_index-1)+ self.right



def get_all_filters():
    """
    Returns all filter classes for enum environments.

    Returns:
        list: List of filter classes.

    Example:
        ```python
        filters = get_all_filters()
        ```
    """
    return [Itemize,Enumeration]