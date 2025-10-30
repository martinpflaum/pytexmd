#%%
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytexmd as ptm

ptm.config.set_latex_replacements([(r"\widebar", r"\overline"),
                                 (r"\C", r"\mathbb{C}"),
                                 (r"\H", r"\mathbb{H}"),
                                 (r"\ltsbrak",r"\langle\langle"),
                                 (r"\rtsbrak",r"\rangle\rangle"),
                                 (r"\mathbbm",r"\mathbb"),])#works in mathjax
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
