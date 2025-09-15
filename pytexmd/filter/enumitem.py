__all__ = ["Itemize","ItemizeItem","Enumeration","EnumerationItem"]

from .core import *
from .splitting import * 

def enum_style_roman(index: int) -> str:
    roman = ["i","ii","iii","iv","v","vi","vii","viii","ix","x",
         "xi","xii","xiii","xiv","xv","xvi","xvii","xviii","xix","xx",
         "xxi","xxii","xxiii","xxiv","xxv","xxvi","xxvii","xxviii","xxix","xxx"]
    
    return roman[index].upper()

def enum_style_Roman(index: int) -> str:
    #roman = ["i","ii","iii","iv","v","vi","vii","viii","ix","x"]
    roman = ["I","II","III","IV","V","VI","VII","VIII","IX","X",
         "XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX",
         "XXI","XXII","XXIII","XXIV","XXV","XXVI","XXVII","XXVIII","XXIX","XXX"]
    return roman[index]

def enum_style_arabic(index: int) -> str:
    return str(index + 1)

def enum_style_alph(index: int) -> str:
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    return lowercase[index]

def enum_style_Alph(index: int) -> str:
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return uppercase[index]

def enum_style_empty(index: int) -> str:
    return ""

enum_styles = {"\\roman":enum_style_roman,"\\Roman":enum_style_Roman,"\\arabic":enum_style_arabic,"\\alph":enum_style_alph,"\\Alph":enum_style_Alph}


class ItemizeItem(Element):
    def __init__(self, modifiable_content: str, parent: Element, label: str = "•"):
        super().__init__("",parent)
        self.label = label

        self.children = [Undefined(label,self),Undefined(modifiable_content,self)]
    
    def label_name(self) -> str:
        return self.label#self.children[0].to_string()

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
        return position_of(string,"\\item")
            
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
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
    current_index = 0
    def __init__(self, modifiable_content: str, parent: Element):
        super().__init__(modifiable_content,parent)
        
    def to_string(self) -> str:
        out = "\n" 
        for child in self.children:
            out += child.to_string().rstrip().lstrip() + "\n"
        out = out.replace("\n","\n"+TAB)
        return out
    
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\begin{itemize}")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        
        pre,content,post = begin_end_split(string,"\\begin{itemize}","\\end{itemize}")
        
        elem_out = Itemize(content,parent)
        elem_out.expand([ItemizeItem])

        return pre,elem_out,post


class EnumerationItem(Element):
    def __init__(self, modifiable_content: str, parent: Element, label: str = None):
        super().__init__("",parent)

        self.label = ""
        if label is None:
            enumeration = self.search_class(Enumeration)
            self.label = enumeration.generate_item_label()
        else:
            self.label = label
            
        self.children = [Undefined(self.label,self),Undefined(modifiable_content,self)]
    
    def label_name(self) -> str:
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
        return position_of(string,"\\item")
            
    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
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
    current_index = 0
    def __init__(self, modifiable_content: str, parent: Element, style_func: callable, left: str, right: str):
        super().__init__(modifiable_content,parent)
        self.style_func,self.left,self.right = style_func,left,right

    def to_string(self) -> str:
        out = "\n" 
        for child in self.children:
            out += child.to_string().rstrip().lstrip() + "\n"
        out = out.replace("\n","\n"+TAB)
        return out
    
    @staticmethod
    def position(string: str) -> int:
        return position_of(string,"\\begin{enumerate}")

    @staticmethod
    def split_and_create(string: str, parent: Element) -> tuple:
        
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
        self.current_index = self.current_index + 1
        return self.left + self.style_func(self.current_index-1)+ self.right



def get_all_filters():
    return [Itemize,Enumeration]