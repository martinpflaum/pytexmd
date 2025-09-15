
from . import preprocessor,section,enumitem,equations,antibugs,core
NUM_FILES = 0

def string_to_tree(string:str):
    string = antibugs.no_more_bugs_begin(string)
    
    string  = preprocessor.run_preprocessor(string)
    all_expands = []
    #basic_expands += junkSearcher+replaceSearcher
    all_expands += [section.get_all_filters()] 
    all_expands += [enumitem.get_all_filters()]
    all_expands += [equations.get_all_filters()]
    #basic_expands += get_drawtex_searchers()
    
    #all_expands = [basic_expands]
    all_expands.append([equations.Label])
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
    global NUM_FILES
    file_name = string.strip()
    if file_name == "":
        file_name = "section"
    # Replace spaces and newlines with underscores
    file_name = file_name.replace(" ", "_").replace("\n", "")
    # Remove all non-alphanumeric and non-underscore characters, and make lowercase
    file_name = ''.join([c.lower() if c.isalpha() else c if c.isdigit() or c == '_' else '_' for c in file_name])
    file_name += "_" + str(NUM_FILES)
    return file_name

def element_to_file_whole(element:section.SectionEnumerate,output_folder:str,file_name:str,output_suffix:str=".md"):
    global NUM_FILES
    NUM_FILES += 1

    file_name = output_folder+"/"+file_name+output_suffix
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(element.to_string())
    print(f"File {file_name} created.")

def element_to_file_only_begin(element:section.SectionEnumerate,output_folder:str,file_name:str,output_suffix:str=".md"):
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
    for child in element.children:
        if isinstance(child,section.SectionEnumerate):
            child_file_name = string_to_file_name(child.children[0].to_string())+"\n"
            out_str += core.TAB+f"{child_file_name}"
                
    out_str += "```\n"
    
    with open(file_name,"w",encoding="utf-8") as f:
        f.write(out_str)

    print(f"File {file_name} created.")
    
def tree_to_files(output_folder:str,element:section.SectionEnumerate,file_name:str,depth:int,output_suffix:str=".md"):
    if not isinstance(element,section.SectionEnumerate):
        raise ValueError("element must be a SectionEnumerate")
    if not isinstance(depth,int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if not isinstance(output_folder,str):
        raise ValueError("output_folder must be a string")
    
    global NUM_FILES
    if depth == 0:
        element_to_file_whole(element,output_folder,file_name,output_suffix)
        return 
    
    has_found_childs = False
    for child in element.children:
        if isinstance(child,section.SectionEnumerate):
            has_found_childs = True
            break

    if not has_found_childs:
        element_to_file_whole(element,output_folder,file_name,output_suffix)
        return
    element_to_file_only_begin(element,output_folder,file_name,output_suffix)

    for child in element.children:
        if isinstance(child,section.SectionEnumerate):
            child_file_name = string_to_file_name(child.children[0].to_string())
    
            tree_to_files(output_folder,child,child_file_name,depth-1,output_suffix)


def process_string(output_folder:str,string:str,depth=3,output_suffix:str=".md"):
    if not isinstance(depth,int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if not isinstance(output_folder,str):
        raise ValueError("output_folder must be a string")
    if not isinstance(string,str):
        raise ValueError("string must be a string")
    document = string_to_tree(string)
    element_to_file_whole(document,output_folder,"index",output_suffix)
    #tree_to_files(output_folder,document,"index",depth,output_suffix)
    