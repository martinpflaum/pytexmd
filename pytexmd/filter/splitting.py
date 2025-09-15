from typing import Tuple, List, Optional, Union, Callable

def get_all_allchars_no_abc()->str:
    """
    super small subset of - this really makes this programm slow otherwise :D
    allchars_no_abc = [chr(k) for k in range(256)]
    allchars_no_abc = ''.join(allchars_no_abc)
    allchars_no_abc = allchars_no_abc.replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ","")
    allchars_no_abc = allchars_no_abc.replace("abcdefghijklmnopqrstuvwxyz","")
    return allchars_no_abc
    """
    return '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n ' # is removed

def save_command_split(string:str, split_on:str)->List[str]:
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(split_on,str):
        raise ValueError("split_on must be a string")
    if split_on == "$":
        return string.split("$")
    for appendix in get_all_allchars_no_abc():
        string = string.replace(split_on + appendix,"XXXsplit_meXXX"+appendix)
    string = string.split("XXXsplit_meXXX")
    return string

"""
def remove_empty_at_begin(string:str)->str:
    return string.lstrip()
    out = 0
    for k,elem in enumerate(string):
        if elem == " " or elem == "\n" or elem =="*":
            if elem =="*":
                print("unexpected * your numbering is probably wrong :'D")
            out = k + 1
        else:
            break
    
    #return string[out:]
"""

def first_char_brace(string:str, begin_brace:str = "{")->bool:
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(begin_brace,str):
        raise ValueError("begin_brace must be a string")
    string = string.lstrip()
    if len(string) == 0:
        return False
    return string[0] == begin_brace

def split_on_first_brace(string:str, begin_brace = "{",end_brace = "}", error_replacement="brace_error")->Tuple[str,str]:
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(begin_brace,str) or not isinstance(end_brace,str):
        raise ValueError("begin_brace and end_brace must be strings")
    string = string.lstrip()
    if len(string) == 0:
        return error_replacement,string
    if string[0] != begin_brace:
        return error_replacement,string

    brace_count = 0
    out1 = ""
    for elem in string:
        out1 += elem
        if elem == begin_brace:
            brace_count = brace_count + 1
        if elem == end_brace:
            brace_count = brace_count - 1
        if brace_count == 0:
            break
    out2 = string[len(out1):]
    out1 = out1[1:-1]
    return out1, out2

def split_rename(string: str) -> Optional[Tuple[str, str]]:
    """
    Splits the input string into a name and the remaining string if the first character is a '['.

    Args:
        string (str): The input string.

    Returns:
        Optional[Tuple[str, str]]: A tuple containing the name and the remaining string, or None if the first character is not '['.
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    string = string.lstrip()
    if len(string) == 0:
        return None
    if string[0] == "[":
        name,post = split_on_first_brace(string,"[","]")
        return name,post
    else:
        return None


def split_on_next(string:str, split_on:str, save_split:bool = True)->Tuple[str,str]:
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(split_on,str):
        raise ValueError("split_on must be a string")
    
    if save_split:
        tmp = save_command_split(string,split_on)
    else:
        tmp = string.split(split_on)
    pre = tmp[0]
    post = string[len(pre + split_on):]
    return pre, post


def begin_end_split(string:str, begin_name:str, end_name:str, save_split:bool = False)->Tuple[str,str,str]:
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(begin_name,str):
        raise ValueError("begin_name must be a string")
    if not isinstance(end_name,str):
        raise ValueError("end_name must be a string")
    pre,xanda = split_on_next(string,begin_name,save_split)
    begin_num = 1
    middle = ""

    while True:
        posbegin = position_of(xanda,begin_name,save_split)
        posend = position_of(xanda,end_name,save_split)
        if posbegin!=-1 and posbegin < posend:
            ptmp,xtmp = split_on_next(xanda,begin_name,save_split)
            middle += ptmp + begin_name
            xanda = xtmp
            begin_num = begin_num + 1
        else:

            ptmp,xtmp = split_on_next(xanda,end_name,save_split)
            begin_num = begin_num - 1
            if begin_num == 0:
                middle += ptmp
                return pre,middle,xtmp
            else:
                middle += ptmp + end_name
                xanda = xtmp
    
def position_of(string:str, begin_name:str, save_split:bool = True)->int:
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(begin_name,str):
        raise ValueError("begin_name must be a string")
    if begin_name in string:
        if save_split:
            tmp = save_command_split(string,begin_name)
        else:
            tmp = string.split(begin_name)
        if len(tmp) == 1:
            return -1
        return len(tmp[0])
    else:
        return -1
