
from .filter.core import SECTION_COMMANDS
from .filter.core import masked_begin_end_split

from typing import List, Tuple, Dict, Optional,NamedTuple
import regex


class FileStructure(NamedTuple):
    file_name:str
    prefix:str
    childs:List["FileStructure"]|None

NUM_FILES = 0

def file_name_raw_myst(latex_section: str) -> str:
    global NUM_FILES
    if not isinstance(latex_section, str):
        raise ValueError("latex_section must be a string")
    
    # Remove all non-alphabetic characters and convert to lowercase
    clean_name = ''.join(char.lower() for char in latex_section if char.isalpha())
    
    # If the result is empty, provide a default name
    if not clean_name:
        clean_name = "section"
    
    clean_name += f"_{NUM_FILES}"
    NUM_FILES += 1
    return clean_name + ".md"

def recursive_structure_myst(file_name:str,latex_content:str,depth:int,max_depth:int,num_hashtags:int)->FileStructure:
    if not isinstance(latex_content,str):
        raise ValueError("latex_content must be a string")
    if not isinstance(file_name,str):
        raise ValueError("file_name must be a string")
    if not isinstance(depth,int):
        raise ValueError("depth must be an integer")
    if not isinstance(max_depth,int):
        raise ValueError("max_depth must be an integer")
    
    if depth >= max_depth:
        return FileStructure(file_name,latex_content,None)
    section_command = SECTION_COMMANDS[depth]
    if section_command not in latex_content:
        return recursive_structure_myst(file_name,latex_content,depth+1,max_depth,num_hashtags+1)
    sections,sections_mask = masked_begin_end_split(latex_content, begin=section_command+"{", end="}", apply_mask=False)
    
    prefix = ""
    childs = []
    prefix_end = False
    for k in range(len(sections)):
        if (not prefix_end) and sections_mask[k] == False:
            prefix += sections[k]
            continue
        else:
            prefix_end = True

        if sections_mask[k] == False:
            continue        

        if k + 1 >= len(sections):
            break
        section_title = sections[k].replace(section_command+"{","").replace("}","")
        section_title = '#' * num_hashtags + ' ' + section_title + '\n\n'
        child_content = section_title+sections[k+1]
        childs.append(recursive_structure_myst(file_name_raw_myst(sections[k]),child_content,depth+1,max_depth,num_hashtags+1))
    return FileStructure(file_name,prefix,childs)
        

        
def get_min_depth(latex_content:str)->int:
    if not isinstance(latex_content,str):
        print("latex_content",type(latex_content))
        raise ValueError("latex_content must be a string")
    depth = 0
    for elem in SECTION_COMMANDS:
        if elem in latex_content:
            return depth
        depth += 1
    return depth

def structure_myst(file_name:str,latex_content:str,max_depth:int=4)->FileStructure:
    if not isinstance(latex_content,str):
        raise ValueError("latex_content must be a string")
    if not isinstance(file_name,str):
        raise ValueError("file_name must be a string")
    if not isinstance(max_depth,int):
        raise ValueError("max_depth must be an integer")
    
    content = masked_begin_end_split(string=latex_content,begin=r"\begin{document}",end=r"\end{document}",apply_mask=True)
    latex_content = content[0]
    latex_content = latex_content.replace(r"\end{document}","")
    latex_content = latex_content.replace(r"\begin{document}","")
    
    #latex_content = content[1]

    depth = get_min_depth(latex_content)
    return recursive_structure_myst(file_name,latex_content,depth,max_depth,1)


def apply_function_to_structure(fs:FileStructure,func)->FileStructure:
    if not isinstance(fs,FileStructure):
        raise ValueError("fs must be a FileStructure")
    if not callable(func):
        raise ValueError("func must be a callable function")
    
    new_prefix = func(fs.prefix)
    if fs.childs is None:
        return FileStructure(fs.file_name,new_prefix,None)
    new_childs = []
    for child in fs.childs:
        new_childs.append(apply_function_to_structure(child,func))
    return FileStructure(fs.file_name,new_prefix,new_childs)