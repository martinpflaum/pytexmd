#%%
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytexmd as ptm



file_name = "../example_tex/FANCyProject/FaNCyProject.tex"
ptm.process_file(file_name,"./my_docs2",depth=3)



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
