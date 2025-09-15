import os
import sys
from pathlib import Path
import subprocess

def create_sphinx_documentation(output_dir: str,project_name:str="My Project",author:str="Author",version:str="1.0"):
    """
    Create a Sphinx documentation structure with source and build folders.
    
    Args:
        output_dir (str): Directory where the Sphinx documentation will be created
    """
    
    try:
        # Run sphinx-quickstart with automated answers
        output_dir = os.path.abspath(output_dir)
        Path(output_dir).mkdir(parents=True)
        cmd = [
                    "sphinx-quickstart",
                    "--quiet",           # Suppress prompts
                    "--sep",             # Separate source and build directories
                    f"--project={project_name}",
                    f"--author={author}",
                    f"--release={version}",
                    "--language=en",
                    "--makefile",        # Create Makefile
                    f"{output_dir}"                  # Current directory
                ]
                
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        
        
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        print(f"Sphinx documentation created in {output_dir}")
    except:
        print("An error occurred while creating Sphinx documentation. -- Maybe Quickstart is already run?")
        pass
