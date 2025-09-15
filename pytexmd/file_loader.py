#%%
__all__ = ["load_tex_file", "LatexFile"]

import os
import regex
from typing import List, Dict, Tuple,Optional,Any,NamedTuple

class LatexFile(NamedTuple):
    content:str
    tex_files:Dict[str,str]
    bib_files:Dict[str,str]
    image_files:Dict[str,str]
    all_files:Dict[str,str]


def load_tex_file(file_name:str)->LatexFile:
    def load_file(file_name:str)->str:
        data = None
        with open(file_name, 'r') as f:
            data = f.read()
        return data
    
    # Get the folder where file_name resides
    #folder_path = os.path.dirname(file_name)
    absolute_folder = os.path.dirname(os.path.abspath(file_name))

    # Get all image files, .bib files, and .tex files in the folder (recursively)
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.pdf', '.eps']
    tex_extensions = [ '.tex', '.sty', '.cls']
    bib_extensions = ['.bib', '.bbl',".bibtex", '.biblatex']
    target_extensions = tex_extensions + image_extensions + bib_extensions

    all_files = []
    tex_files = []
    bib_files = []
    image_files = []

    if os.path.exists(absolute_folder):
        # Walk through all subdirectories recursively
        for root, dirs, files in os.walk(absolute_folder):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.abspath(file_path)
                file_ext = os.path.splitext(file)[1].lower()
                
                if file_ext in tex_extensions:
                    tex_files.append(relative_path)
                elif file_ext in bib_extensions:
                    bib_files.append(relative_path)
                elif file_ext in image_extensions:
                    image_files.append(relative_path)

    print(f"Folder (recursive): {absolute_folder}")
    print(f"TEX files: {tex_files}")
    print(f"BIB files: {bib_files}")
    print(f"Image files: {image_files}")

    content = load_file(file_name)

    def remove_extensions(file_name):
        for ext in target_extensions:
            file_name = file_name.replace(ext, "")
        return file_name
        
    _tex_files = { remove_extensions(file.split("\\")[-1].split("/")[-1]):file for file in tex_files}
    _bib_files = {remove_extensions(file.split("\\")[-1].split("/")[-1]): file for file in bib_files}
    _image_files = {remove_extensions(file.split("\\")[-1].split("/")[-1]): file for file in image_files}
    all_files = {**_tex_files, **_bib_files, **_image_files}

    def input_to_filename(input_name):
        input_name = remove_extensions(input_name)
        input_name = input_name.split("\\")[-1]
        input_name = input_name.split("/")[-1]
        return all_files[input_name]

    def get_input_file(input_name):
        try:
            filename = input_to_filename(input_name)
        #    print(filename)
            return load_file(filename)
        except KeyError:
            print(f"File not found for input: {input_name}")
            return ""
    # Search for \input{filename} patterns in the content
    input_pattern = r'\\input\{([^}]+)\}'
    content_old = content
    done_matches = []

    while True:
        matches = regex.findall(input_pattern, content)
        for match in matches:
            if match in done_matches:
                continue
            content = content.replace(r"\input{"+match+"}", get_input_file(match))
            done_matches.append(match)
        if content == content_old:
            break
        content_old = content
    out = {"content": content, "tex_files": _tex_files, "bib_files": _bib_files, "image_files": _image_files, "all_files": all_files}
    return LatexFile(**out)

