from .filter import process_string
from .file_loader import load_file
from .sphinx_doc import create_sphinx_documentation


def process_file(input_file:str,output_folder:str,depth=3,output_suffix:str=".md"):
    file_string = load_file(input_file)
    create_sphinx_documentation(output_folder)
    
    process_string(output_folder+"\\"+"source",file_string,depth,output_suffix)

