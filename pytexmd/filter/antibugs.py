#%%
__all__ = [
    "raw_remove_comments",
    "no_more_html_bugs",
    "no_more_dolar_bugs_begin",
    "no_more_dolar_bugs_end",
    "no_more_textup_bugs_begin",
    "remove_empty_at_begin",
    "only_two_breaks",
    "no_more_bugs_begin",
    "no_more_bugs_end"
]
from . import splitting
def raw_remove_comments(input: str) -> str:
    """
    Removes comments (lines starting with %) from a raw string.

    Args:
        input (str): The input string to process.

    Returns:
        str: The string with comments removed.

    Example:
        >>> raw_remove_comments("Hello % comment\\nWorld")
        'Hello \\nWorld'
    """
    comment = False
    out = ""
    empty = True 
    for elem in input:
        if comment == False:
            if elem == "%":
                comment = True
                empty = False
            else:
                out += elem
        else:
            if elem == "%":
                if empty == False:
                    comment = False
            else:
                empty = False
        if elem == "\n":
            comment = False
    return out

def no_more_html_bugs(input: str) -> str:
    """
    Fixes HTML bugs by adding spaces around '<' and '>' characters.

    Args:
        input (str): The input string.

    Returns:
        str: The processed string with spaces around '<' and '>'.

    Example:
        >>> no_more_html_bugs("<div>")
        ' < div > '
    """
    input = input.replace("<"," < ")
    input = input.replace(">"," > ")
    return input

def no_more_dolar_bugs_begin(input: str) -> str:
    """
    Replaces escaped dollar signs (\\$) with a placeholder.

    Args:
        input (str): The input string.

    Returns:
        str: The string with '\\$' replaced by 'BACKSLASHDOLLAR'.

    Example:
        >>> no_more_dolar_bugs_begin("Price is \\$5")
        'Price is BACKSLASHDOLLAR5'
    """
    input = input.replace("\\$","BACKSLASHDOLLAR")
    return input
    
def no_more_dolar_bugs_end(input: str) -> str:
    """
    Restores dollar signs by replacing the placeholder with '$'.

    Args:
        input (str): The input string.

    Returns:
        str: The string with 'BACKSLASHDOLLAR' replaced by '$'.

    Example:
        >>> no_more_dolar_bugs_end("Price is BACKSLASHDOLLAR5")
        'Price is $5'
    """
    input = input.replace("BACKSLASHDOLLAR","$")
    return input

def no_more_textup_bugs_begin(input: str) -> str:
    """
    Removes '\\textup' from the input string.

    Args:
        input (str): The input string.

    Returns:
        str: The string with '\\textup' removed.

    Example:
        >>> no_more_textup_bugs_begin("This is \\textup{important}")
        'This is {important}'
    """
    input = input.replace("\\textup","")
    return input
    

def remove_empty_at_begin(input: str) -> str:
    """
    Removes leading spaces and newlines from the input string.

    Args:
        input (str): The input string.

    Returns:
        str: The string with leading spaces and newlines removed.

    Example:
        >>> remove_empty_at_begin("   \\nHello")
        'Hello'
    """
    out = 0
    for k,elem in enumerate(input):
        if elem == " " or elem == "\n":
            out = k + 1
        else:
            break
    return input[out:]



def label_strip(string:str)->str:
    """
    Strips LaTeX label commands from the input string.

    Args:
        string (str): The input string containing LaTeX labels.
    """
    out = ""
    while splitting.position_of(string, "\\label{") != -1:
        pre,middle,post = splitting.begin_end_split(string,"\\label{","}")
        out += pre + "\\label{" + middle.strip() + "}" 
        string = post
    out += string
    return out

def ref_strip(string:str)->str:
    """
    Strips LaTeX reference commands from the input string.

    Args:
        string (str): The input string containing LaTeX references.
    """
    out = ""
    while splitting.position_of(string, "\\ref{") != -1:
        pre,middle,post = splitting.begin_end_split(string,"\\ref{","}")
        out += pre + "\\ref{" + middle.strip() + "}" 
        string = post
    out += string
    return out

def label_renamer(string: str) -> str:
    label_counter = {}
    string = label_strip(string)
    string = ref_strip(string)

    out = ""
    while splitting.position_of(string, "\\label{") != -1:
        pre,middle,post = splitting.begin_end_split(string,"\\label{","}")
        if not middle in label_counter.keys():
            label_counter[middle] = 0
        else:
            label_counter[middle] += 1
        out += pre
        out = out.replace("\\label{"+middle+"}","\\label{"+middle+"_duplicate_"+str(label_counter[middle])+"}") 
        out += "\\label{"+middle+"}"
        string = post
    out += string
    
    return out

def no_more_bugs_begin(input: str) -> str:
    """
    Applies a series of bug fixes to the input string at the beginning of processing.

    Args:
        input (str): The input string.

    Returns:
        str: The processed string after applying bug fixes.

    Example:
        >>> no_more_bugs_begin("Some \\$text <div> \\textup{here}")
        'Some BACKSLASHDOLLARtext  < div >  {here}'
    """
    input = raw_remove_comments(input)
    input = no_more_html_bugs(input)
    input = no_more_dolar_bugs_begin(input)
    input = no_more_textup_bugs_begin(input)
    input = label_renamer(input)
    
    return input

def no_more_bugs_end(input: str) -> str:
    """
    Applies a series of bug fixes to the input string at the end of processing.

    Args:
        input (str): The input string.

    Returns:
        str: The processed string after applying bug fixes.

    Example:
        >>> no_more_bugs_end("Some BACKSLASHDOLLARtext")
        'Some $text'
    """
    input = no_more_dolar_bugs_end(input)
    #input = only_two_breaks(input)
    return input
