#%%
import os
import sys
from pathlib import Path
import re
sys.path.append(str(Path(__file__).parent.parent))
import pytexmd as ptm

file_name = "../examples_tex/FANCyProject-master/FaNCyProject.tex"

latex_content = ptm.file_loader.load_tex_file(file_name)
file_string = latex_content.content
document_md = ptm.filter.string_to_tree(file_string)

# %%
from pathlib import Path
import re

# Constants from core.py
SEC_DEF_SPLITTER = "XXSEC_DEF_SPLITTERXX"
SEC_PREFIX_BEGIN = "XXSEC_PREFIX_BEGINXX"
SEC_PREFIX_END = "XXSEC_PREFIX_ENDXX"

SECTION_HIERARCHY = {
    "\\part": 0,
    "\\chapter": 1,
    "\\section": 2,
    "\\subsection": 3,
    "\\subsubsection": 4,
    "\\paragraph": 5,
    "\\subparagraph": 6,
    "\\part*": 0,
    "\\chapter*": 1,
    "\\section*": 2,
    "\\subsection*": 3,
    "\\subsubsection*": 4,
    "\\paragraph*": 5,
    "\\subparagraph*": 6,
}

def string_to_filename(name):
    """Convert section name to valid filename."""
    # Remove special characters and replace spaces with underscores
    filename = re.sub(r'[^\w\s-]', '', name.lower())
    filename = re.sub(r'[-\s]+', '_', filename)
    return filename.strip('_')

def split_by_sections(content_string, max_depth=2):
    """
    Split document string into hierarchical sections based on MyST comment markers.
    
    Args:
        content_string (str): The full document string with MyST markers
        max_depth (int): Maximum depth for splitting (0=part, 1=chapter, 2=section, etc.)
        
    Returns:
        dict: Hierarchical structure of sections with content
    """
    # Pattern to find section definitions
    def_pattern = f"<!-- {SEC_DEF_SPLITTER}(.*?){SEC_DEF_SPLITTER}(.*?){SEC_DEF_SPLITTER} -->"
    
    sections = []
    
    for match in re.finditer(def_pattern, content_string):
        command = match.group(1)
        name = match.group(2)
        level = SECTION_HIERARCHY.get(command, 999)
        
        # Find corresponding PREFIX_BEGIN and PREFIX_END
        begin_marker = f"<!-- {SEC_PREFIX_BEGIN}{command}{name} -->"
        end_marker = f"<!-- {SEC_PREFIX_END}{command}{name} -->"
        
        begin_pos = content_string.find(begin_marker, match.start())
        end_pos = content_string.find(end_marker, begin_pos)
        
        if begin_pos != -1 and end_pos != -1:
            # Extract full content from BEGIN to END (includes nested sections)
            full_content = content_string[begin_pos:end_pos + len(end_marker)]
            
            sections.append({
                'command': command,
                'name': name,
                'level': level,
                'content': full_content,
                'begin_pos': begin_pos,
                'end_pos': end_pos + len(end_marker),
                'children': []
            })
    
    # Handle preamble (content before first section)
    if sections:
        preamble = content_string[:sections[0]['begin_pos']]
        if preamble.strip():
            root = {
                'command': 'document',
                'name': 'index',
                'level': -1,
                'content': preamble,
                'children': [],
                'begin_pos': 0,
                'end_pos': sections[0]['begin_pos']
            }
        else:
            root = {'command': 'document', 'name': 'index', 'level': -1, 'content': '', 'children': []}
    else:
        root = {'command': 'document', 'name': 'index', 'level': -1, 'content': content_string, 'children': []}
    
    # Build hierarchy based on nesting (sections are already nested in the string)
    stack = [root]
    
    for section in sections:
        # Pop stack until we find the parent (whose end_pos is after this section's end_pos)
        while len(stack) > 1:
            parent = stack[-1]
            # If current section ends before parent ends, it's a child of parent
            if 'end_pos' in parent and section['end_pos'] <= parent['end_pos']:
                break
            stack.pop()
        
        # Add to parent's children
        stack[-1]['children'].append(section)
        stack.append(section)
    
    return root

def extract_section_content(section):
    """Extract section's own content (before children) from PREFIX_BEGIN to first child's PREFIX_BEGIN."""
    content = section['content']
    
    # If no children, return all content (from PREFIX_BEGIN to PREFIX_END)
    if not section['children']:
        return content, ''
    
    # Find the PREFIX_BEGIN marker for this section
    begin_marker = f"<!-- {SEC_PREFIX_BEGIN}"
    begin_pos = content.find(begin_marker)
    
    if begin_pos == -1:
        return content, ''
    
    # Find the first child's PREFIX_BEGIN marker
    # Look for the next PREFIX_BEGIN after the parent's BEGIN
    search_from = begin_pos + len(begin_marker)
    child_begin_pos = content.find(begin_marker, search_from)
    
    if child_begin_pos != -1:
        # Content from parent's BEGIN to first child's BEGIN
        own_content = content[:child_begin_pos]
        remaining = content[child_begin_pos:]
        return own_content, remaining
    
    # No child PREFIX_BEGIN found, return all content
    return content, ''

def write_section_files(section, output_folder, max_depth, current_depth=0, output_suffix=".md"):
    """
    Recursively write section and its children to files.
    
    Args:
        section (dict): Section structure
        output_folder (str): Output directory
        max_depth (int): Maximum splitting depth
        current_depth (int): Current recursion depth
        output_suffix (str): File extension
        
    Returns:
        str: Filename of created file (without extension)
    """
    os.makedirs(output_folder, exist_ok=True)
    
    filename = string_to_filename(section['name'])
    filepath = os.path.join(output_folder, filename + output_suffix)
    
    # Determine if we should split children into separate files
    should_split = current_depth < max_depth and section['children']
    
    with open(filepath, 'w', encoding='utf-8') as f:
        if should_split:
            # Extract only this section's own content (before children)
            own_content, remaining = extract_section_content(section)
            f.write(own_content.strip() + "\n\n")
            
            # Create toctree for children
            f.write("```{toctree}\n")
            f.write(":maxdepth: 2\n\n")
            
            child_files = []
            for child in section['children']:
                child_filename = write_section_files(
                    child, 
                    output_folder, 
                    max_depth, 
                    current_depth + 1,
                    output_suffix
                )
                child_files.append(child_filename)
            
            for child_file in child_files:
                f.write(f"{child_file}\n")
            
            f.write("```\n")
        else:
            # Include all content (parent + all descendants)
            f.write(section['content'].strip() + "\n")
    
    print(f"Created: {filepath}")
    return filename

def reconstruct_content_from_structure(section):
    """
    Recursively reconstruct the full content from a section structure.
    
    Args:
        section (dict): Section structure with content and children
        
    Returns:
        str: Reconstructed content
    """
    # For leaf sections (no children), return content as-is
    if not section['children']:
        return section['content']
    
    # For sections with children, combine parent content + all child content
    # Extract parent's own content (before first child)
    own_content, _ = extract_section_content(section)
    
    # Add all children's content
    full_content = own_content
    for child in section['children']:
        full_content += reconstruct_content_from_structure(child)
    
    # Add the PREFIX_END if this section has one
    if section.get('command') != 'document':
        end_marker = f"<!-- {SEC_PREFIX_END}{section['command']}{section['name']} -->"
        if end_marker not in full_content:
            full_content += "\n" + end_marker
    
    return full_content

def verify_content_integrity(original_content, structure):
    """
    Verify that the split structure contains all original content.
    
    Args:
        original_content (str): Original document string
        structure (dict): Parsed section structure
        
    Returns:
        tuple: (is_valid, message, stats)
    """
    reconstructed = reconstruct_content_from_structure(structure)
    
    # Calculate statistics
    stats = {
        'original_length': len(original_content),
        'reconstructed_length': len(reconstructed),
        'difference': len(original_content) - len(reconstructed),
        'match': original_content == reconstructed
    }
    
    if stats['match']:
        message = "✓ Content integrity verified: All content preserved!"
        is_valid = True
    else:
        message = f"✗ Content mismatch: {stats['difference']} character difference"
        is_valid = False
        
        # Find where they differ
        for i, (c1, c2) in enumerate(zip(original_content, reconstructed)):
            if c1 != c2:
                start = max(0, i - 50)
                end = min(len(original_content), i + 50)
                message += f"\n  First difference at position {i}:"
                message += f"\n  Original: ...{original_content[start:end]}..."
                message += f"\n  Reconstructed: ...{reconstructed[start:end]}..."
                break
    
    return is_valid, message, stats

def split_document_to_files(document_md, output_folder, depth=2, output_suffix=".md", verify=True):
    """
    Main function to split document tree into hierarchical MyST files.
    
    Args:
        document_md: Document tree object
        output_folder (str): Output directory path
        depth (int): Splitting depth (0=no split, 1=chapter, 2=section, etc.)
        output_suffix (str): File extension
        verify (bool): Verify content integrity after parsing
    """
    # Convert document to string
    content_string = document_md.to_string()
    
    # Parse hierarchical structure
    root = split_by_sections(content_string, depth)
    
    # Verify content integrity if requested
    if verify:
        is_valid, message, stats = verify_content_integrity(content_string, root)
        print(f"\n{message}")
        print(f"  Original: {stats['original_length']:,} chars")
        print(f"  Reconstructed: {stats['reconstructed_length']:,} chars")
        if not is_valid:
            print("\n⚠ Warning: Proceeding with file creation despite content mismatch")
    
    # Write files
    write_section_files(root, output_folder, depth, 0, output_suffix)
    
    print(f"\n✓ Document split into files in: {output_folder}")

# %%
# Example usage with automatic verification
output_folder = "./my_split_docs"
split_document_to_files(document_md, output_folder, depth=2, verify=True)

# %%
# Manual verification - compare original with structure
content_string = document_md.to_string()
structure = split_by_sections(content_string, max_depth=2)

is_valid, message, stats = verify_content_integrity(content_string, structure)
print(message)
print(f"\nStatistics:")
print(f"  Original length: {stats['original_length']:,} characters")
print(f"  Reconstructed length: {stats['reconstructed_length']:,} characters")
print(f"  Content match: {stats['match']}")

# %%
# You can also inspect the hierarchy structure
def print_structure(node, indent=0):
    """Helper to visualize the structure"""
    content_preview = node.get('content', '')[:50].replace('\n', ' ')
    print("  " * indent + f"[{node['level']}] {node['command']}: {node['name']} ({len(node.get('content', ''))} chars)")
    for child in node.get('children', []):
        print_structure(child, indent + 1)

print("\nDocument Structure:")
print_structure(structure)
# %%
# %%
# Write the full document string to a single file
output_file = "./output_full_document.md"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(document_md.to_string())

print(f"✓ Full document written to: {output_file}")
# %%
