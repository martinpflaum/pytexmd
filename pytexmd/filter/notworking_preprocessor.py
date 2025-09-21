__all__ = ["do_commands"]

import re
from typing import List, Dict, Tuple,Optional,Any,NamedTuple
from .splitting import first_char_brace,split_on_first_brace,split_on_next,begin_end_split,position_of,save_replace
from .core import Element

class DefinedCommand(NamedTuple):
    name: str
    content: str
    num_required_args: int
    default_arg1: str|None

class FoundCommand(NamedTuple):
    name: str
    required_args:List[str]
    optional_arg1: str|None



def do_command_internal(def_command:DefinedCommand,found_command:FoundCommand)->str:
        
    content = def_command.content
    if found_command.optional_arg1 is not None:
        content = content.replace("#1", def_command.default_arg1)
        
    offset = 1 if found_command.optional_arg1 is not None else 0

    for n in range(def_command.num_required_args):
        content = content.replace(f"#{n+1+offset}", found_command.required_args[n])
    return content

def do_commands(string:str)->str:
    out = ""
    while "\\newcommand{ " in string or "\\renewcommand{ " in string or "\\newcommand{\n" in string or "\\renewcommand{\n" in string:
        string = string.replace("\\newcommand{ ","\\newcommand{")
        string = string.replace("\\renewcommand{ ","\\renewcommand{")
        string = string.replace("\\newcommand{\n","\\newcommand{")
        string = string.replace("\\renewcommand{\n","\\renewcommand{")

    print("Processing commands...")
    print(string)
    while True:
        if "\\newcommand" not in string and "\\renewcommand" not in string:
            break
        pre, post = None,None
        if position_of(string,"\\newcommand") == -1:
            pre, post = split_on_next(string,"\\renewcommand")
        elif position_of(string,"\\renewcommand") == -1:
            pre, post = split_on_next(string,"\\newcommand")
        elif position_of(string,"\\newcommand") < position_of(string,"\\renewcommand"):
            pre, post = split_on_next(string,"\\newcommand")
        else:
            pre, post = split_on_next(string,"\\renewcommand")
        out += pre
        post = post.lstrip()

        name, post = split_on_first_brace(post,"{","}")
        name = name.strip()
        if name == "":
            string = post
            print("Empty command name in \\newcommand or \\renewcommand")
            continue
        else:
            print("Defining command: ",name)

        num_args_total = 0
        if post.startswith("["):
            brace_content,post = split_on_first_brace(post,"[","]")
            post = post.lstrip()
            try:
                num_args_total = int(brace_content.lstrip())
            except:
                pass
        
        default_arg1 = None
        if post.startswith("["):
            brace_content,post = split_on_first_brace(post,"[","]")
            post = post.lstrip()
            default_arg1 = brace_content.lstrip()
        
        content,post = split_on_first_brace(post,"{","}")
        content = content.lstrip()
        post = post.lstrip()

        placeholders = re.findall(r"#\d+", content.replace("\\\\","").replace("\\#",""))
        if len(placeholders) > 0:
            for elem in placeholders:
                num_args_total = max(num_args_total,int(elem[1:]))
        
        defined_command = DefinedCommand(name=name, content=content, num_required_args=num_args_total, default_arg1=default_arg1)
        post,none_editable = split_on_next(post,"\\renewcommand{"+name)
        none_editable = "\\renewcommand{"+name+none_editable
        
        if num_args_total == 0 and default_arg1 is None:
            print("Applying command without arguments: ",name)
            post = save_replace(post,name,content)
            string = post + none_editable
            continue

        while position_of(post,name) != -1:
            pre,post = split_on_next(post,name)
            out += pre
            post = post.lstrip()

            optional_arg = None
            if defined_command.default_arg1 is not None:
                if post.startswith("["):
                    brace_content,post = split_on_first_brace(post,"[","]")
                    post = post.lstrip()
                    optional_arg = brace_content.lstrip()
            
            required_args = []
            for k in range(defined_command.num_required_args):
                if post.startswith("{"):
                    brace_content,post = split_on_first_brace(post,"{","}")
                    post = post.lstrip()
                    required_args.append(brace_content.lstrip())
                else:
                    required_args.append("ERROR_MISSING_ARG")

            found_command = FoundCommand(name,required_args,optional_arg)
            finished_content = do_command_internal(defined_command,found_command)
            out += finished_content
        string = post + none_editable
    out += string
    return out



class DefinedEnvironment(NamedTuple):
    name: str
    begin_content: str
    end_content: str
    num_required_args: int
    default_arg1: str|None

class FoundEnvironment(NamedTuple):
    name: str
    required_args: List[str]
    optional_arg1: str|None
    body: str

def do_environment_internal(def_env:DefinedEnvironment,found_env:FoundEnvironment)->str:
    
    begin_content = def_env.begin_content
    end_content = def_env.end_content
    
    if found_env.optional_arg1 is not None:
        begin_content = begin_content.replace("#1", def_env.default_arg1)
        end_content = end_content.replace("#1", def_env.default_arg1)
        
    offset = 1 if found_env.optional_arg1 is not None else 0

    for n in range(def_env.num_required_args):
        begin_content = begin_content.replace(f"#{n+1+offset}", found_env.required_args[n])
        end_content = end_content.replace(f"#{n+1+offset}", found_env.required_args[n])
    
    replacement = begin_content + found_env.body + end_content
    return replacement

def new_do_environments(string:str)->str:
    out = ""
    while "\\newenvironment{ " in string or "\\renewenvironment{ " in string or "\\newenvironment{\n" in string or "\\renewenvironment{\n" in string:
        string = string.replace("\\newenvironment{ ","\\newenvironment{")
        string = string.replace("\\renewenvironment{ ","\\renewenvironment{")
        string = string.replace("\\newenvironment{\n","\\newenvironment{")
        string = string.replace("\\renewenvironment{\n","\\renewenvironment{")
     
    while True:
        if "\\newenvironment" not in string and "\\renewenvironment" not in string:
            break
        pre, post = None,None
        if position_of(string,"\\newenvironment") == -1:
            pre, post = split_on_next(string,"\\renewenvironment")
        elif position_of(string,"\\renewenvironment") == -1:
            pre, post = split_on_next(string,"\\newenvironment")
        elif position_of(string,"\\newenvironment") < position_of(string,"\\renewenvironment"):
            pre, post = split_on_next(string,"\\newenvironment")
        else:
            pre, post = split_on_next(string,"\\renewenvironment")
        out += pre
        post = post.lstrip()

        environment_name, post = split_on_first_brace(post,"{","}")
        num_args_total = 0

        if post.startswith("["):
            brace_content,post = split_on_first_brace(post,"[","]")
            post = post.lstrip()
            try:
                num_args_total = int(brace_content.lstrip())
            except:
                pass
        
        default_arg1 = None
        if post.startswith("["):
            brace_content,post = split_on_first_brace(post,"[","]")
            post = post.lstrip()
            default_arg1 = brace_content.lstrip()


        begin,post = split_on_first_brace(post,"{","}")
        begin = begin.lstrip()
        post = post.lstrip()
        
        end,post = split_on_first_brace(post,"{","}")
        end = end.lstrip()
        post = post.lstrip()

        defined_env = DefinedEnvironment(name=environment_name, begin_content=begin, end_content=end, num_required_args=num_args_total, default_arg1=default_arg1)
        post,none_editable = split_on_next(post,"\\renewenvironment{"+environment_name)
        none_editable = "\\renewenvironment{"+environment_name+none_editable
        





__all__ = ["do_commands","do_newenvironment"]

from .splitting import first_char_brace,split_on_first_brace,split_on_next,begin_end_split,position_of
from .core import Element



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


"""def do_commands(string: str) -> str:
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

"""
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
    while "\t" in latex_content:
        latex_content = latex_content.replace("\t"," ")
    while "  " in latex_content:
        latex_content = latex_content.replace("  "," ")
    while " \n" in latex_content:
        latex_content = latex_content.replace(" \n","\n")
    while "\n " in latex_content:
        latex_content = latex_content.replace("\n ","\n")
    while "\n\n\n" in latex_content:
        latex_content = latex_content.replace("\n\n\n","\n\n")
    
    XXDOUBLENEWLINEXX = "XXDOUBLENEWLINEXX"
    latex_content = latex_content.replace("\n\n",XXDOUBLENEWLINEXX)
    XXNEWLINECOMMANDXX = "XXNEWLINECOMMANDXX"
    latex_content = latex_content.replace("\n\\",XXNEWLINECOMMANDXX)
    XXBRACENEWLINEXX = "XXBRACENEWLINEXX"
    latex_content = latex_content.replace("}\n",XXBRACENEWLINEXX)
    XXBRACKETNEWLINEXX = "XXBRACKETNEWLINEXX"
    latex_content = latex_content.replace("]\n",XXBRACKETNEWLINEXX)
    XXKLAMMERNEWLINEXX = "XXKLAMMERNEWLINEXX"
    latex_content = latex_content.replace(")\n",XXKLAMMERNEWLINEXX)
    
    latex_content = latex_content.replace("\n"," ")

    latex_content = latex_content.replace(XXDOUBLENEWLINEXX,"\n\n")
    latex_content = latex_content.replace(XXNEWLINECOMMANDXX,"\n\\")
    latex_content = latex_content.replace(XXBRACENEWLINEXX,"}\n")
    latex_content = latex_content.replace(XXBRACKETNEWLINEXX,"]\n")
    latex_content = latex_content.replace(XXKLAMMERNEWLINEXX,")\n")
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