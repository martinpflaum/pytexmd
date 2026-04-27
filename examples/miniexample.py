#%%
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytexmd as ptm

"""ptm.config.set_latex_replacements([(r"\widebar", r"\overline"),
                                 (r"\C", r"\mathbb{C}"),
                                 (r"\H", r"\mathbb{H}"),
                                 (r"\ltsbrak",r"\langle\langle"),
                                 (r"\rtsbrak",r"\rangle\rangle"),
                                 (r"\mathbbm",r"\mathbb"),])#works in mathjax
"""
file_name = "../examples_tex/FANCyProject/FaNCyProject.tex"
ptm.process_file(file_name,"./my_docs3",depth=3)

# %%
"""from sphinx.cmd.quickstart import main as sphinx_quickstart

# The API takes a list of CLI-like args (without the program name)
sphinx_quickstart([
    "my_docs",
    "--release", "0.1",
    "--sep",
    "--project", "My Project",
    "--author", "Martin Pflaum",
    "--makefile",
    "--batchfile",
    "--language", "en",
])

from sphinx.cmd.build import main as sphinx_build

sphinx_build([
    "-M",
    "html",
    "my_docs/source",
    "my_docs/build"
])
"""
#%%
"""file_name = "../examples_tex/FANCyProject/FaNCyProject.tex"

latex_content = ptm.file_loader.load_tex_file(file_name)
file_string = latex_content.content
document_md = ptm.filter.string_to_tree(file_string)
document_md
# Write the full document string to a single file
output_file = "./output_full_document.md"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(document_md.to_string())

print(f"✓ Full document written to: {output_file}")
"""