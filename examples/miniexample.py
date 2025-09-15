#%%
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytexmd as ptm



file_name = "../example_tex/FANCyProject/FaNCyProject.tex"
ptm.process_file(file_name,"./my_docs",depth=3)


# %%
