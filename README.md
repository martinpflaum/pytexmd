# Pytexmd

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
