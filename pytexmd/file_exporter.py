from .structure import FileStructure
import os
from pathlib import Path
from typing import Dict
from .filter.core import TAB

def export_myst(file_structure: FileStructure, output_folder: str):
    """
    Export FileStructure to MyST files in the specified output folder.
    
    Args:
        file_structure (FileStructure): The structure to export
        output_folder (str): Path to the output directory
    """
    
    # Create the output folder if it doesn't exist
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    def write_structure_recursive(structure: FileStructure, current_path: Path):
        """Recursively write structure to files."""
        
        # Create file for current structure
        file_path = current_path / f"{structure.file_name}.md"
        
        # Write content to file
        with open(file_path, 'w', encoding='utf-8') as f:
            content_parts = []
            
            # Add the prefix content
            if structure.prefix:
                print("structure.prefix",structure.prefix)
                content_parts.append(structure.prefix.strip())
            
            # Add toctree if there are children
            if structure.childs:
                content_parts.append("\n```{toctree}")
                #content_parts.append(":maxdepth: 2")
                #content_parts.append(":numbered:")
                #content_parts.append("")
                
                for child in structure.childs:
                    # Add relative path to child file
                    content_parts.append(TAB+f"{child.file_name}")
                
                content_parts.append("```\n")
            
            f.write('\n'.join(content_parts))
        
        # Process children
        if structure.childs:
            for child in structure.childs:
                write_structure_recursive(child, current_path)
    
    # Start recursive writing
    write_structure_recursive(file_structure, output_path)
