"""Sphinx documentation utilities for pytexmd.

This module provides functions to create Sphinx documentation structure and configuration files.
"""

__all__ = [
    "load_config_template",
    "create_config_file",
    "create_sphinx_documentation"
]

import os
import sys
from pathlib import Path
import subprocess
import time
from sphinx.cmd.quickstart import main as sphinx_quickstart
from sphinx.cmd.build import main as sphinx_build


def load_config_template() -> str:
    """Load the Sphinx configuration template.

    Returns:
        str: Contents of the configuration template file.
    """
    template_path = Path(__file__).parent / "templates" / "conf.txt"
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def create_config_file(output_dir: str, project_name: str, author: str, version: str) -> None:
    """Create a Sphinx conf.py configuration file in the source directory.

    Args:
        output_dir (str): Directory where the Sphinx documentation is located.
        project_name (str): Name of the project.
        author (str): Author name.
        version (str): Project version.

    Returns:
        None
    """
    try:
        source_dir = Path(output_dir) / "source"
        source_dir.mkdir(parents=True, exist_ok=True)
        config_path = source_dir / "conf.py"
        
        config_template = load_config_template()
        config_content = config_template.replace("XXPROJECTXX", project_name)\
                                        .replace("XXAUTHORSXX", author)\
                                        .replace("XXRELEASEXX", version)
        
        with open(config_path, 'w', encoding='utf-8') as file:
            file.write(config_content)
        
        print(f"Configuration file created at {config_path}")
    except Exception as e:
        print(f"An error occurred while creating the configuration file: {e}")

def create_sphinx_documentation(
    output_dir: str,
    project_name: str = "My Project",
    author: str = "Author",
    version: str = "1.0"
) -> None:
    """Create a Sphinx documentation structure with source and build folders.

    Args:
        output_dir (str): Directory where the Sphinx documentation will be created.
        project_name (str, optional): Name of the project. Defaults to "My Project".
        author (str, optional): Author name. Defaults to "Author".
        version (str, optional): Project version. Defaults to "1.0".

    Returns:
        None
    """
    
    # Run sphinx-quickstart with automated answers
    output_dir = os.path.abspath(output_dir)
    
    # The API takes a list of CLI-like args (without the program name)
    sphinx_quickstart([
        output_dir,
        "--release", version,
        "--sep",
        "--project", project_name,
        "--author", author,
        "--makefile",
        "--batchfile",
        "--language", "en",
    ])


    #cmd = f"sphinx-quickstart {output_dir} --sep --project={project_name.replace(" ","_")} --author={author.replace(" ","_")} --release={version.replace(" ","_")} --language=en"
    
    print("waiting 0.5 seconds to let the file system catch up")
    time.sleep(0.5)

    # Delete the auto-generated index.rst file
    try:
        index_rst_path = Path(output_dir) / "source" / "index.rst"
        if index_rst_path.exists():
            index_rst_path.unlink()
            print(f"Deleted auto-generated index.rst file at {index_rst_path}")
    except Exception as e:
        print(f"Warning: Could not delete index.rst: {e}")

    try:
        output_dir = os.path.abspath(output_dir)
        Path(output_dir).mkdir(parents=True)
    except:
        pass
    
    output_dir = os.path.abspath(output_dir)
    create_config_file(output_dir, project_name, author, version)


