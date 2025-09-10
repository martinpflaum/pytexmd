import os
import sys
from pathlib import Path
import subprocess

def create_sphinx_documentation(output_dir: str):
    """
    Create a Sphinx documentation structure with source and build folders.
    
    Args:
        output_dir (str): Directory where the Sphinx documentation will be created
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Change to output directory
    original_cwd = os.getcwd()
    os.chdir(output_path)
    
    try:
        # Run sphinx-quickstart with automated answers
        cmd = [
            "sphinx-quickstart",
            "--quiet",           # Suppress prompts
            "--sep",             # Separate source and build directories
            "--project=MyProject",
            "--author=Author",
            "--release=1.0",
            "--language=en",
            "--makefile",        # Create Makefile
            "--batchfile",       # Create batch file for Windows
            "."                  # Current directory
        ]
        
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        print(f"Sphinx documentation created successfully in: {output_path}")
        print(f"Source directory: {output_path / 'source'}")
        print(f"Build directory: {output_path / 'build'}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating Sphinx documentation: {e}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        raise
    
    finally:
        # Return to original directory
        os.chdir(original_cwd)

