__all__ = ["get_all_allchars_no_abc","save_command_split","first_char_brace","split_on_first_brace","split_rename","split_on_next","begin_end_split","position_of"]

from typing import Tuple, List, Optional, Union, Callable

def get_all_allchars_no_abc()->str:
    """
    Returns a string of non-alphabetic ASCII characters.

    Returns:
        str: String containing non-alphabetic ASCII characters.

    Example:
        >>> chars = get_all_allchars_no_abc()
        >>> isinstance(chars, str)
        True
    """
    return '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n ' # is removed

def save_command_split(string:str, split_on:str)->List[str]:
    """
    Splits a string on a given substring, preserving certain patterns.

    Args:
        string (str): The input string to split.
        split_on (str): The substring to split on.

    Returns:
        List[str]: List of split string segments.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> parts = save_command_split("foo$bar$baz", "$")
        >>> parts
        ['foo', 'bar', 'baz']
    """
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

def save_replace(string:str, old:str, new:str)->str:
    """
    Replaces occurrences of a substring in a string, preserving certain patterns.

    Args:
        string (str): The input string.
        old (str): The substring to be replaced.
        new (str): The substring to replace with.

    Returns:
        str: The modified string with replacements.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> result = save_replace("foo$bar$baz", "$", "#")
        >>> result
        'foo#bar#baz'
    """
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(old,str):
        raise ValueError("old must be a string")
    if not isinstance(new,str):
        raise ValueError("new must be a string")
    for appendix in get_all_allchars_no_abc():
        string = string.replace(old + appendix,"XXXsplit_meXXX"+appendix)
    string = string.replace("XXXsplit_meXXX",new)
    return string

def first_char_brace(string:str, begin_brace:str = "{")->bool:
    """
    Checks if the first non-whitespace character of a string is a given brace.

    Args:
        string (str): The input string.
        begin_brace (str, optional): The brace character to check. Defaults to "{".

    Returns:
        bool: True if first character is the brace, False otherwise.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> is_brace = first_char_brace(" {foo}")
        >>> is_brace
        True
    """
    if not isinstance(string,str):
        raise ValueError("Input must be a string")
    if not isinstance(begin_brace,str):
        raise ValueError("begin_brace must be a string")
    string = string.lstrip()
    if len(string) == 0:
        return False
    return string[0] == begin_brace

def split_on_first_brace(string:str, begin_brace = "{",end_brace = "}", error_replacement="brace_error")->Tuple[str,str]:
    """
    Splits a string on the first matching pair of braces.

    Args:
        string (str): The input string.
        begin_brace (str, optional): The opening brace. Defaults to "{".
        end_brace (str, optional): The closing brace. Defaults to "}".
        error_replacement (str, optional): Replacement string if brace not found. Defaults to "brace_error".

    Returns:
        Tuple[str, str]: Content inside braces, and the remaining string.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> inside, rest = split_on_first_brace("{foo}bar")
        >>> inside
        'foo'
        >>> rest
        'bar'
    """
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

    Raises:
        ValueError: If input is not a string.

    Example:
        >>> name, rest = split_rename("[foo]bar")
        >>> name
        'foo'
        >>> rest
        'bar'
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
    """
    Splits a string on the next occurrence of a substring.

    Args:
        string (str): The input string.
        split_on (str): The substring to split on.
        save_split (bool, optional): Whether to use save_command_split. Defaults to True.

    Returns:
        Tuple[str, str]: The part before and after the split.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> before, after = split_on_next("foo$bar$baz", "$")
        >>> before
        'foo'
        >>> after
        'bar$baz'
    """
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
    """
    Splits a string into three parts: before, between, and after given begin and end substrings.

    Args:
        string (str): The input string.
        begin_name (str): The substring marking the beginning.
        end_name (str): The substring marking the end.
        save_split (bool, optional): Whether to use save_command_split. Defaults to False.

    Returns:
        Tuple[str, str, str]: The parts before, between, and after the delimiters.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> pre, mid, post = begin_end_split("a\\begin{env}b\\end{env}c", "\\begin{env}", "\\end{env}")
        >>> pre
        'a'
        >>> mid
        'b'
        >>> post
        'c'
    """
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
    """
    Finds the position of a substring in a string.

    Args:
        string (str): The input string.
        begin_name (str): The substring to find.
        save_split (bool, optional): Whether to use save_command_split. Defaults to True.

    Returns:
        int: The position index, or -1 if not found.

    Raises:
        ValueError: If input types are incorrect.

    Example:
        >>> pos = position_of("foo$bar", "$")
        >>> pos
        3
    """
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
