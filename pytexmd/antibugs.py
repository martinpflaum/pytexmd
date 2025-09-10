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

def clean_junk_safe(latex_content:str)->str:
    """Cleans up LaTeX content by removing unnecessary characters and formatting issues.

    Args:
        latex_content (str): The LaTeX content to be cleaned.
    
    Returns:
        str: The cleaned LaTeX content.
    """
    while "\\"*4 in latex_content:
        latex_content = latex_content.replace("\\"*4, "")
    while "\n\n\n" in latex_content:
        latex_content = latex_content.replace("\n\n\n","\n\n")
    while "  " in latex_content:
        latex_content = latex_content.replace("  "," ")
    while "\t" in latex_content:
        latex_content = latex_content.replace("\t"," ")
    while " \n" in latex_content:
        latex_content = latex_content.replace(" \n","\n")
    while "\n " in latex_content:
        latex_content = latex_content.replace("\n ","\n")
    return latex_content

def raw_remove_comments(input: str) -> str:
    """
    Removes comments (lines starting with %) from a raw string.

    Args:
        input (str): The input string to process.

    Returns:
        str: The string with comments removed.

    Example:
        >>> raw_remove_comments("Hello % comment\nWorld")
        'Hello \nWorld'
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
    r"""
    Fixes HTML bugs by adding spaces around '<' and '>' characters.

    Args:
        input (str): The input HTML string.

    Returns:
        str: The processed HTML string with spaces around '<' and '>'.

    Example:
        >>> no_more_html_bugs("<div>")
        ' < div > '
    """
    input = input.replace("<"," < ")
    input = input.replace(">"," > ")
    return input

def no_more_dolar_bugs_begin(input: str) -> str:
    r"""
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
        >>> remove_empty_at_begin("   \nHello")
        'Hello'
    """
    out = 0
    for k,elem in enumerate(input):
        if elem == " " or elem == "\n":
            out = k + 1
        else:
            break
    return input[out:]

def only_two_breaks(input: str) -> str:
    """
    Ensures that there are at most two consecutive <br> tags in the input string.

    Args:
        input (str): The input string.

    Returns:
        str: The processed string with at most two consecutive <br> tags.

    Example:
        >>> only_two_breaks("a<br><br><br>b")
        'a<br><br>b'
    """
    input += "  "
    input = input.split("<br>")
    out = ""
    for elem in input[:-1]:
        
        out += (remove_empty_at_begin(elem)) + "<br>"
    out += input[-1]

    while True:
        tmp = out.replace("<br><br><br>","<br><br>")
        if tmp == out:
            out.replace("<br>","\n<br>")
            return out
        else:
            out = tmp

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
