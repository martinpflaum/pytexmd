__all__ = ["string_to_tree",
           "process_string",
           "element_to_file_whole",
           "element_to_file_only_begin",
           "split_document_to_files",
           "split_by_sections",
           "verify_content_integrity",
           "string_to_filename",
           ]

from . import preprocessor,enumitem,equations,antibugs,core,splitting, text

from typing import List
from pathlib import Path
import os
import re

NUM_FILES = 0

# Section hierarchy mapping for splitting
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

def string_to_tree(string:str)->core.Document:
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
    #all_expands += [[core.BackMatter()]]  #backmatter and appendix splitter
    all_expands += core.get_section_like_filters_top_lvl()
    theorem_searchers = text.get_theoremSearchers(string)
    para_searcher = text.ParaSearcher([s.theorem_env_name for s in theorem_searchers])
    all_expands += [theorem_searchers + [para_searcher]]+[[text.Proof]]+ [enumitem.get_all_filters()]
    all_expands += [equations.get_all_filters()]
    all_expands += [text.get_all_filters()] 
    all_expands += [[core.OneArgumentJunkSearcher(r"\hspace")]]
    junk_commands = ["\\sffamily","\\itshape","\\nonumber","\\noindent","\\indent","\\newpage","\\em"]
    #replace_mentdict = {"\\noindent":""}#"\\prerequisites ":"</p><h1 style=\"font-size:20px\">Prerequisites</h1><p>","\\N ":"\\mathbb{N}","\\id ":"id","\\GL ":"GL","\\Mat ":"\mathfrak{M}"}
    all_expands += [[core.JunkSearcher(elem) for elem in junk_commands]]

    #basic_expands += get_drawtex_searchers()
    
    #all_expands = [basic_expands]
    #all_expands.append([section.Label])
    all_expands.append([text.EqRef, text.Cref, text.Ref, text.Cite])

    
    number_within_equation = text.get_number_within_equation(string)
    
    pre_docmuent,document,post_document = text.Document.split_and_create(string,None)
    #document.globals.number_within_equation = number_within_equation
    
    for expand_on in all_expands:
        document.expand(expand_on)
    document.expand([core.JunkSearcher("{",save_split=False),core.JunkSearcher("}",save_split=False)])
    document.expand([core.JunkSearcher("\\ ",save_split=False)])
    
    
    #pre_content are just commands
    print("processing finished! now the final file will be created.")
    document._finish_up()
    
    
    return document


def element_to_file_whole(element:core.SectionLike,output_folder:str,file_name:str,output_suffix:str=".md"):
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

def element_to_file_only_begin(element:core.SectionLike,output_folder:str,file_name:str,file_names:List[str],output_suffix:str=".md"):
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
        if isinstance(child,core.SectionLike):
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


def string_to_filename(name):
    """Convert section name to valid filename.
    
    Args:
        name (str): Section name to convert
        
    Returns:
        str: Sanitized filename
    """
    # Remove special characters and replace spaces with underscores
    filename = re.sub(r'[^\w\s-]', '', name.lower())
    filename = re.sub(r'[-\s]+', '_', filename)
    return filename.strip('_') or 'section'

def split_by_sections(content_string, max_depth=2):
    """
    Split document string into hierarchical sections based on MyST comment markers.
    
    Args:
        content_string (str): The full document string with MyST markers
        max_depth (int): Maximum depth for splitting (0=part, 1=chapter, 2=section, etc.)
        
    Returns:
        dict: Hierarchical structure of sections with content and children tracking
    """
    # Pattern to find section definitions
    def_pattern = f"<!-- {core.SEC_DEF_SPLITTER}(.*?){core.SEC_DEF_SPLITTER}(.*?){core.SEC_DEF_SPLITTER} -->"
    
    sections = []
    
    for match in re.finditer(def_pattern, content_string):
        command = match.group(1).strip()
        name = match.group(2).strip()

        # Unnumbered sections are never split into their own file; their
        # content stays inside the preceding/parent numbered section.
        if command.endswith('*'):
            continue

        level = SECTION_HIERARCHY.get(command, 999)
        
        # Debug: warn if command not found in hierarchy
        if level == 999:
            print(f"Warning: Unknown section command '{command}' (repr: {repr(command)}) - treating as level 999")
            print(f"  Available commands: {list(SECTION_HIERARCHY.keys())}")
        
        # Find corresponding PREFIX_BEGIN and PREFIX_END
        begin_marker = f"<!-- {core.SEC_PREFIX_BEGIN}{command}{name} -->"
        end_marker = f"<!-- {core.SEC_PREFIX_END}{command}{name} -->"
        
        # Start searching from the DEF_SPLITTER position
        begin_pos = content_string.find(begin_marker, match.start())
        end_pos = content_string.find(end_marker, begin_pos)
        
        if begin_pos != -1 and end_pos != -1:
            # Extract full content from DEF_SPLITTER to END marker (includes all markers)
            full_content = content_string[match.start():end_pos + len(end_marker)]
            
            sections.append({
                'command': command,
                'name': name,
                'level': level,
                'content': full_content,
                'start_pos': match.start(),
                'begin_pos': begin_pos,
                'end_pos': end_pos + len(end_marker),
                'children': [],
                'child_files': []  # Track children file names
            })
    
    # Build hierarchy first
    root = {'command': 'document', 'name': 'index', 'level': -1, 'content': '', 'children': [], 'child_files': []}
    
    if not sections:
        root['content'] = content_string
        return root
    
    stack = [root]
    
    for section in sections:
        # Pop stack until we find the parent
        while len(stack) > 1:
            parent = stack[-1]
            if 'end_pos' in parent and section['end_pos'] <= parent['end_pos']:
                break
            stack.pop()
        
        # Add to parent's children
        stack[-1]['children'].append(section)
        stack.append(section)
    
    top_level_sections = root['children']

    if not top_level_sections:
        root['content'] = content_string
        return root

    # Preamble (content before first numbered top-level section, which may
    # include unnumbered sections like \chapter*{Authors}) goes to the
    # root/index file via root['content'].
    if top_level_sections[0]['start_pos'] > 0:
        root['content'] = content_string[:top_level_sections[0]['start_pos']]

    # Attach inter-section and epilogue content to the preceding numbered
    # section so it appears in that section's file rather than being lost.
    for i, section in enumerate(top_level_sections):
        if i + 1 < len(top_level_sections):
            inter = content_string[section['end_pos']:top_level_sections[i + 1]['start_pos']]
            if inter.strip():
                section['content'] += inter

    epilogue = content_string[top_level_sections[-1]['end_pos']:]
    if epilogue.strip():
        top_level_sections[-1]['content'] += epilogue

    # content_chunks used only by verify_content_integrity
    content_chunks = [('preamble', root['content'])] if root['content'] else []
    for section in top_level_sections:
        content_chunks.append(('section', section))
    root['content_chunks'] = content_chunks
    return root

def _get_section_own_content(section):
    """Return content before the first child's DEF marker."""
    content = section['content']
    children = section.get('children', [])
    if not children:
        return content
    first_child = children[0]
    def_marker = (f"<!-- {core.SEC_DEF_SPLITTER}{first_child['command']}"
                  f"{core.SEC_DEF_SPLITTER}{first_child['name']}{core.SEC_DEF_SPLITTER} -->")
    pos = content.find(def_marker)
    return content[:pos] if pos != -1 else content


def _get_inter_and_trailing_content(section):
    """Return content between/after children: unnumbered sections, post-child text."""
    content = section['content']
    children = section.get('children', [])
    if not children:
        return ''
    own_end = (f"<!-- {core.SEC_PREFIX_END}{section['command']}{section['name']} -->"
               if section.get('command') not in (None, 'document') else '')
    parts = []
    for i, child in enumerate(children):
        end_marker = f"<!-- {core.SEC_PREFIX_END}{child['command']}{child['name']} -->"
        end_pos = content.rfind(end_marker)
        if end_pos == -1:
            continue
        start = end_pos + len(end_marker)
        if i + 1 < len(children):
            next_child = children[i + 1]
            next_def = (f"<!-- {core.SEC_DEF_SPLITTER}{next_child['command']}"
                        f"{core.SEC_DEF_SPLITTER}{next_child['name']}{core.SEC_DEF_SPLITTER} -->")
            end = content.find(next_def, start)
            if end == -1:
                end = len(content)
        else:
            end = len(content)
        chunk = content[start:end]
        if own_end:
            chunk = chunk.replace(own_end, '')
        chunk = chunk.strip()
        if chunk:
            parts.append(chunk)
    return '\n\n'.join(parts)

def write_section_files(section, output_folder, max_depth, current_depth=0, output_suffix=".md", append_toc=None):
    """
    Recursively write section and its children to files.
    
    Args:
        section (dict): Section structure
        output_folder (str): Output directory
        max_depth (int): Maximum splitting depth
        current_depth (int): Current recursion depth
        output_suffix (str): File extension
        append_toc (list): Extra filenames to append to this section's toctree
        
    Returns:
        str: Filename of created file (without extension)
    """
    os.makedirs(output_folder, exist_ok=True)
    
    filename = string_to_filename(section['name'])
    filepath = os.path.join(output_folder, filename + output_suffix)
    
    should_split = current_depth < max_depth and len(section['children']) > 1
    extra_toc = append_toc or []

    with open(filepath, 'w', encoding='utf-8') as f:
        if should_split or extra_toc:
            # Own content: for root use its content (preamble); for sections
            # use content before the first child's DEF marker.
            if section.get('command') == 'document':
                own_content = section.get('content', '')
            else:
                own_content = _get_section_own_content(section)
            if own_content.strip():
                f.write(own_content.strip() + "\n\n")

            # Toctree navigation must not add implicit section numbers.
            f.write("```{toctree}\n")
            f.write(":maxdepth: 2\n")
            f.write("\n")

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

            section['child_files'] = child_files

            for child_file in child_files:
                f.write(f"{child_file}\n")
            for extra in extra_toc:
                f.write(f"{extra}\n")
            f.write("```\n")

            # Write content that lives between/after numbered children:
            # unnumbered sections (\section*), trailing text, appended
            # inter-section content from split_by_sections.
            if section.get('command') != 'document':
                trailing = _get_inter_and_trailing_content(section)
                if trailing.strip():
                    f.write("\n" + trailing.strip() + "\n")
        else:
            # Leaf section — write full content.
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
    if section.get('command') == 'document' and 'content_chunks' in section:
        reconstructed = ''
        for chunk_type, chunk_data in section['content_chunks']:
            if chunk_type == 'section':
                reconstructed += chunk_data['content']
            else:
                reconstructed += chunk_data
        return reconstructed
    
    return section.get('content', '')

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
    
    stats = {
        'original_length': len(original_content),
        'reconstructed_length': len(reconstructed),
        'difference': len(original_content) - len(reconstructed),
        'match': original_content == reconstructed
    }
    
    if stats['match']:
        message = "Content integrity verified: All content preserved!"
        is_valid = True
    else:
        message = f"Content mismatch: {stats['difference']} character difference"
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
    
    Each section file will know its child files through the structure.
    
    Args:
        document_md: Document tree object (from string_to_tree)
        output_folder (str): Output directory path
        depth (int): Splitting depth (0=no split, 1=chapter, 2=section, etc.)
        output_suffix (str): File extension
        verify (bool): Verify content integrity after parsing
        
    Returns:
        dict: Root structure with child_files tracking for all sections
        
    Example:
        ```python
        # Convert and split a document
        doc = string_to_tree(latex_string)
        structure = split_document_to_files(doc, "./output", depth=2, verify=True)
        # Each section in structure has 'child_files' list
        ```
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
            print("\nWarning: Proceeding with file creation despite content mismatch")
    
    # Write files
    write_section_files(root, output_folder, depth, 0, output_suffix,
                        append_toc=["references"])

    # Create a dedicated references page so sphinxcontrib.bibtex renders the
    # bibliography list.
    refs_path = os.path.join(output_folder, "references" + output_suffix)
    with open(refs_path, 'w', encoding='utf-8') as f:
        f.write("# References\n\n")
        f.write("```{bibliography}\n")
        f.write(":style: unsrt\n")
        f.write("```\n")
    print(f"Created: {refs_path}")

    print(f"\nDocument split into files in: {output_folder}")
    return root

def process_string(output_folder:str, string:str, depth=2, output_suffix:str=".md", verify=True):
    """
    Processes a LaTeX string and writes the document to hierarchical MyST files.
    
    This function converts LaTeX to a document tree, then splits it into multiple
    files based on section hierarchy with automatic content verification.

    Args:
        output_folder (str): The output folder path.
        string (str): The input LaTeX string.
        depth (int, optional): Splitting depth (0=no split, 1=chapter, 2=section, etc.). Defaults to 2.
        output_suffix (str, optional): The file suffix. Defaults to ".md".
        verify (bool, optional): Verify content integrity after parsing. Defaults to True.

    Returns:
        dict: Root structure with child_files tracking for all sections

    Example:
        ```python
        # Process a LaTeX string and split into hierarchical files
        latex = r\"""\\chapter{Intro}\\section{Background}\\subsection{Details}\"""
        structure = process_string("output", latex, depth=2)
        # Creates: output/intro.md with toctree to output/background.md
        ```
    """
    if not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if not isinstance(output_folder, str):
        raise ValueError("output_folder must be a string")
    if not isinstance(string, str):
        raise ValueError("string must be a string")
    
    # Convert LaTeX to document tree
    document = string_to_tree(string)
    
    # Split document into hierarchical files with verification
    structure = split_document_to_files(
        document, 
        output_folder, 
        depth=depth, 
        output_suffix=output_suffix,
        verify=verify
    )
    
    return structure
