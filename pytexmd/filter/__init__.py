__all__ = ["string_to_tree",
           "tree_to_files",
           "process_string",
           "string_to_file_name",
           "element_to_file_whole",
           "element_to_file_only_begin"
           "preprocessor",
           "section",
           "enumitem",
           "equations",
           "antibugs",
           "core"
           "splitting"
           ]


from . import preprocessor,section,enumitem,equations,antibugs,core,splitting
from typing import List
NUM_FILES = 0

def string_to_tree(string:str):
    """
    Converts a string to a document tree structure.

    Args:
        string (str): The input string to process.

    Returns:
        Document: The processed document tree.

    Example:
        ```python
        latex = r\"""\\section{Intro}\\begin{equation}E=mc^2\\end{equation}\"""
        doc = string_to_tree(latex)
        print(doc.to_string())
        ```
    """
    string = antibugs.no_more_bugs_begin(string)
    
    string  = preprocessor.run_preprocessor(string)
    all_expands = []
    
    #basic_expands += junkSearcher+replaceSearcher
    all_expands += [section.get_all_filters()] 
    all_expands += [enumitem.get_all_filters()]
    all_expands += [equations.get_all_filters()]
    all_expands += [[core.OneArgumentJunkSearch(r"\hspace")]]
    junk_commands = ["\\sffamily","\\itshape","\\nonumber","\\noindent","\\indent","\\newpage"]
    #replace_mentdict = {"\\noindent":""}#"\\prerequisites ":"</p><h1 style=\"font-size:20px\">Prerequisites</h1><p>","\\N ":"\\mathbb{N}","\\id ":"id","\\GL ":"GL","\\Mat ":"\mathfrak{M}"}
    all_expands += [[core.JunkSearch(elem) for elem in junk_commands]]

    #basic_expands += get_drawtex_searchers()
    
    #all_expands = [basic_expands]
    #all_expands.append([section.Label])
    all_expands.append([section.EqRef,section.Ref,section.Cite])

    all_expands[0].extend(section.get_theoremSearchers(string))
    number_within_equation = section.get_number_within_equation(string)
    
    pre_docmuent,document,post_document = section.Document.split_and_create(string,None)
    document.globals.number_within_equation = number_within_equation
    
    for expand_on in all_expands:
        document.expand(expand_on)
    document.expand([core.JunkSearch("{",save_split=False),core.JunkSearch("}",save_split=False)])
    document.expand([core.JunkSearch("\\ ",save_split=False)])
    
    
    #pre_content are just commands
    print("processing finished! now the final file will be created.")
    document._finish_up()
    
    
    return document

def string_to_file_name(string: str):
    """
    Generates a file name from a string.

    Args:
        string (str): The input string.

    Returns:
        str: A sanitized file name.

    Example:
        ```python
        # Produces 'section_0' for empty string
        print(string_to_file_name(""))  
        # Produces 'my_section_1' for "My Section"
        print(string_to_file_name("My Section"))
        ```
    """
    global NUM_FILES
    file_name = string.strip()
    file_name = file_name.split("\n")[0]
    if file_name == "":
        file_name = "section"
    # Replace spaces and newlines with underscores
    file_name = file_name.replace(" ", "_").replace("\n", "")
    # Remove all non-alphanumeric and non-underscore characters, and make lowercase
    file_name = ''.join([c.lower() if c.isalpha() else c if c.isdigit() or c == '_' else '_' for c in file_name])
    file_name += "_" + str(NUM_FILES)
    return file_name

def element_to_file_whole(element:section.SectionEnumerate,output_folder:str,file_name:str,output_suffix:str=".md"):
    """
    Writes the whole element to a file.

    Args:
        element (SectionEnumerate): The element to write.
        output_folder (str): The output folder path.
        file_name (str): The file name.
        output_suffix (str, optional): The file suffix. Defaults to ".md".

    Returns:
        None

    Example:
        ```python
        # Save the entire document as 'output/index.md'
        doc = string_to_tree(r"\\section{Intro}")
        element_to_file_whole(doc, "output", "index")
        ```
    """
    global NUM_FILES
    NUM_FILES += 1

    file_name = output_folder+"/"+file_name+output_suffix
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(element.to_string())
    print(f"File {file_name} created.")
    return [file_name.replace(output_suffix,"")]

def element_to_file_only_begin(element:section.SectionEnumerate,output_folder:str,file_name:str,file_names:List[str],output_suffix:str=".md"):
    """
    Writes only the beginning part of the element to a file, with a toctree.

    Args:
        element (SectionEnumerate): The element to write.
        output_folder (str): The output folder path.
        file_name (str): The file name.
        output_suffix (str, optional): The file suffix. Defaults to ".md".

    Returns:
        None

    Example:
        ```python
        # Save only the introduction and generate a toctree for subsections
        doc = string_to_tree(r"\\section{Intro}\\section{Background}")
        element_to_file_only_begin(doc, "output", "index")
        ```
    """
    global NUM_FILES
    NUM_FILES += 1

    file_name = output_folder+"/"+file_name+output_suffix
    out_str = ""
    for child in element.children:
        if isinstance(child,section.SectionEnumerate):
            break
        out_str += child.to_string()
    
    out_str += "\n\n"
    out_str += "\n```{toctree}\n"
    for child_file_name in file_names:
        out_str += core.TAB+f"{child_file_name}"
                
    out_str += "```\n"
    
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(out_str)

    print(f"File {file_name} created.")
    return [file_name.replace(output_suffix,"")]

def tree_to_files(output_folder:str,element:section.SectionEnumerate,file_name:str,depth:int,output_suffix:str=".md"):
    """
    Recursively writes tree elements to files up to a given depth.

    Args:
        output_folder (str): The output folder path.
        element (SectionEnumerate): The root element.
        file_name (str): The base file name.
        depth (int): The recursion depth.
        output_suffix (str, optional): The file suffix. Defaults to ".md".

    Returns:
        None

    Example:
        ```python
        # Recursively split document into files for each section up to depth 2
        doc = string_to_tree(r"\\section{Intro}\\section{Background}")
        tree_to_files("output", doc, "index", 2)
        ```
    """
    if not isinstance(element,section.SectionEnumerate):
        has_found_childs = False
        for child in element.children:
            if isinstance(child,section.SectionEnumerate):
                has_found_childs = True
                break
        if not has_found_childs:
            return []
        else:
            child_file_names = []
    
            for child in element.children:
                if isinstance(child,section.SectionEnumerate):
                    child_file_name = string_to_file_name(child.children[0].to_string())
                    child_file_names.extend(tree_to_files(output_folder,child,None,depth-1,output_suffix))
                else:
                    child_file_names.extend(tree_to_files(output_folder,child,None,depth-1,output_suffix))
            
            return child_file_names
    else:
        if file_name is None:
            file_name = string_to_file_name(element.children[0].to_string())
    if not isinstance(depth,int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if not isinstance(output_folder,str):
        raise ValueError("output_folder must be a string")
    
    global NUM_FILES
    if depth == 0:
        return element_to_file_whole(element,output_folder,file_name,output_suffix)
         
    
    has_found_childs = False
    for child in element.children:
        if isinstance(child,section.SectionEnumerate):
            has_found_childs = True
            break

    if not has_found_childs:
        return element_to_file_whole(element,output_folder,file_name,output_suffix)
        
    child_file_names = []
    for child in element.children:
        if isinstance(child,section.SectionEnumerate):
            child_file_names.extend(tree_to_files(output_folder,child,None,depth-1,output_suffix))
        else:
            pass
    return element_to_file_only_begin(element,output_folder,file_name,child_file_names,output_suffix)

def process_string(output_folder:str,string:str,depth=3,output_suffix:str=".md"):
    """
    Processes a string and writes the document to files.

    Args:
        output_folder (str): The output folder path.
        string (str): The input string.
        depth (int, optional): The recursion depth. Defaults to 3.
        output_suffix (str, optional): The file suffix. Defaults to ".md".

    Returns:
        None

    Example:
        ```python
        # Process a LaTeX string and write the main file to 'output/index.md'
        latex = r\"""\\section{Intro}\\begin{equation}E=mc^2\\end{equation}\"""
        process_string("output", latex)
        ```
    """
    if not isinstance(depth,int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if not isinstance(output_folder,str):
        raise ValueError("output_folder must be a string")
    if not isinstance(string,str):
        raise ValueError("string must be a string")
    document = string_to_tree(string)
    element_to_file_whole(document,output_folder,"index",output_suffix)
    #tree_to_files(output_folder,document,"index",depth,output_suffix)
