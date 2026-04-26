# PyTeXmd

Pytexmd is a Python package designed to translate LaTeX documents to Markdown MyST and HTML. It provides utilities for filtering content, loading files, and integrating with Sphinx documentation. 

## Documentation

- **Full Documentation**: [pytexmd.readthedocs.io](https://pytexmd.readthedocs.io/en/latest/index.html)
- **GitHub Repository**: [github.com/martinpflaum/pytexmd](https://github.com/martinpflaum/pytexmd)

## Installation

To install the required dependencies for pytexmd, run:

```bash
pip install -r requirements.txt
```

This will install all necessary packages for using pytexmd, including Sphinx and MyST support.

## Python Usage Example

If you want to use pytexmd from a Python script, make sure your script is in the same folder (or a subfolder) as the pytexmd package, or add pytexmd to your Python path. The following example can also be found in the examples folder:

```python
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytexmd as ptm

file_name = "../example_tex/FANCyProject/FaNCyProject.tex"
ptm.process_file(file_name, "./my_docs", depth=3)
```

After running this script, you should find the generated markdown files in the `my_docs` folder. Now you need to run the command-line:

```bash
make html
```

in the `my_docs` folder to generate the HTML files.
```
project = 'My Project'
copyright = '2025, Author'
author = 'Author'
release = '1.0'

extensions = ['myst_parser',
              "sphinx_proof"]

templates_path = ['_templates']
exclude_patterns = []

mathjax3_config = {
    "tex": {
        "macros": {
            "ltortoise": "\\unicode{x3014}",
            "rtortoise": "\\unicode{x3015}",
            "ltsbrak": ["\\mathopen{\\ltortoise\\mspace{1mu}}", 0],
            "rtsbrak": ["\\mathopen{\\mspace{1mu}\\rtortoise}", 0],
            "mathbbm": ["\\mathbb{#1}", 1],
            "widebar": ["\\overline{#1}", 1],
            "C": "\\mathbb{C}",
        }
    }
}


myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

math_number_all = True             # number *all* displayed equations
math_eqref_format = "({number})"   # how equation refs look
numfig = True                      # enable section-prefixed numbering
math_numfig = True                 # apply section prefix to equations
numfig_secnum_depth = 2            # use # and ## levels (e.g. 1.2.3)

html_theme = 'furo'
html_static_path = ['_static']
```