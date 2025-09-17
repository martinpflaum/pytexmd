__all__ = ["do_commands","do_newenvironment"]

from .splitting import first_char_brace,split_on_first_brace,split_on_next,begin_end_split,position_of

def execute_on_pattern(string: str, arg_num: int, command_name: str, command_pattern: str) -> str:
    """
    Expands a LaTeX command pattern in the string.

    Args:
        string (str): The input string.
        arg_num (int): Number of arguments for the command.
        command_name (str): The command name to match.
        command_pattern (str): The pattern to replace.

    Returns:
        str: The string with expanded command patterns.

    Example:
        >>> s = r"\\foo{a}{b}"
        >>> execute_on_pattern(s, 2, "\\foo", "#1+#2")
        'a+b'
    """
    out = ""
    while(True):
        pattern_instance = command_pattern
        pre,post = split_on_next(string,command_name)
        if string == pre:    
            out += pre
            break
        for k in range(arg_num):
            
            content = ""
            if first_char_brace(post):  
                content,post = split_on_first_brace(post)
            elif first_char_brace(post,"["):
                content,post = split_on_first_brace(post,"[","]")
            pattern_instance = pattern_instance.replace("#"+str(k+1),content)

        string = post
        out += pre + pattern_instance

    return out

def do_commands(string: str) -> str:
    """
    Processes all LaTeX \\newcommand definitions and applies them.

    Args:
        string (str): The input string.

    Returns:
        str: The string with commands expanded.

    Example:
        >>> s = r"\\newcommand{\\foo}[2]{#1+#2} \\foo{a}{b}"
        >>> do_commands(s)
        'a+b'
    """
    toprocess = string
    out = ""
    all_commands = []
    while True:
        #
        pre,post = split_on_next(toprocess,"\\newcommand")
        out += pre 
        if toprocess == pre:    
            break
        
        command_name,post = split_on_first_brace(post)
        arg_num = 0
        if first_char_brace(post,"["):
            arg_num,post = split_on_first_brace(post,"[","]")
            arg_num = int(arg_num)
        command_pattern,post = split_on_first_brace(post)
        toprocess = post
        all_commands.append((arg_num,command_name,command_pattern))

    while True:
        tmp = string
        for arg_num,command_name,command_pattern in all_commands:
            tmp = execute_on_pattern(tmp,arg_num,command_name,command_pattern)
        if tmp == string:
            break
        string = tmp
    return string


def execute_enviroment_on_pattern(string: str, environment_name: str, arg_num: int, begin: str, end: str) -> str:
    """
    Expands a LaTeX environment pattern in the string.

    Args:
        string (str): The input string.
        environment_name (str): The environment name to match.
        arg_num (int): Number of arguments for the environment.
        begin (str): Begin pattern.
        end (str): End pattern.

    Returns:
        str: The string with expanded environment patterns.

    Example:
        >>> s = r"\\begin{foo}{a}{b}content\\end{foo}"
        >>> execute_enviroment_on_pattern(s, "foo", 2, "<b>#1 #2>", "</b>")
        '<b>a b>content</b>'
    """
    out = ""
    while(True):
        begin_instance = begin
        end_instance = end
        if not "\\begin{"+environment_name+"}" in string:    
            out += string
            break

        pre,content,post = begin_end_split(string,"\\begin{"+environment_name+"}","\\end{"+environment_name+"}")
        for k in range(arg_num):
            argument = ""
            if first_char_brace(content):  
                argument,content = split_on_first_brace(content)
            elif first_char_brace(content,"["):
                argument,content = split_on_first_brace(content,"[","]")
            end_instance = end_instance.replace("#"+str(k+1),argument)
            begin_instance = begin_instance.replace("#"+str(k+1),argument)
        string = post
        out += pre + begin_instance + content +  end_instance

    return out


def do_newenvironment(string: str) -> str:
    """
    Processes all LaTeX \\newenvironment definitions and applies them.

    Args:
        string (str): The input string.

    Returns:
        str: The string with environments expanded.

    Example:
        >>> s = r"\\newenvironment{foo}[2]{<b>#1 #2>}{</b>} \\begin{foo}{a}{b}content\\end{foo}"
        >>> do_newenvironment(s)
        '<b>a b>content</b>'
    """
    toprocess = string
    out = ""
    all_env = []
    while True:
        pre,post = split_on_next(toprocess,"\\newenvironment")
        out += pre 
        if toprocess == pre:    
            break
        
        environment_name,post = split_on_first_brace(post)
        arg_num = 0
        if first_char_brace(post,"["):
            arg_num,post = split_on_first_brace(post,"[","]")
            arg_num = int(arg_num)
        post = "{" + split_on_next(post,"{")[1]
        begin,post = split_on_first_brace(post)
        end,post = split_on_first_brace(post)
        toprocess = post
        all_env.append((environment_name,arg_num,begin,end))

    while True:
        tmp = string
        for environment_name,arg_num,begin,end in all_env:
            print("applying enviroment ",environment_name)
            tmp = execute_enviroment_on_pattern(tmp,environment_name,arg_num,begin,end)
        if tmp == string:
            break
        string = tmp
    return string



def clean_junk_safe(latex_content:str)->str:
    """
    Cleans up LaTeX content by removing unnecessary characters and formatting issues.

    Args:
        latex_content (str): The LaTeX content to be cleaned.
    
    Returns:
        str: The cleaned LaTeX content.

    Example:
        >>> clean_junk_safe("foo    bar\\n\\n\\n")
        'foo bar\\n\\n'
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


def run_preprocessor(string: str) -> str:
    """
    Runs the full preprocessor pipeline on the input string.

    Args:
        string (str): The input string.

    Returns:
        str: The processed string.

    Example:
        >>> s = r"\\newcommand{\\foo}[1]{#1!} \\foo{bar}"
        >>> run_preprocessor(s)
        'bar!'
    """
    string = clean_junk_safe(string)
    string = do_commands(string)
    string = do_newenvironment(string)
    return string