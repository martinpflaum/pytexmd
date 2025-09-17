Welcome To Pytexmd'S Documentation!
===================================
Pytexmd is a Python designed to translate LaTeX documents to markdown myst and html. It provides utilities for filtering content, loading files, and integrating with Sphinx documentation. The aims to streamline workflows involving Markdown and LaTeX, making it easier to automate document generation, conversion, and integration with Python projects. 

Installation
------------

To install the required dependencies for pytexmd, run:

.. code-block:: bash

   pip install -r requirements.txt

This will install all necessarys for using pytexmd, including Sphinx and MyST support.

Python Usage Example
--------------------

If you want to use pytexmd from a Python script, make sure your script is in the same folder (or a subfolder) as the pytexmd, or add pytexmd to your Python path. The following example can also be found in the examples folder:

.. code-block:: python

   #%%
   import os
   import sys
   from pathlib import Path
   sys.path.append(str(Path(__file__).parent.parent))
   import pytexmd as ptm

   file_name = "../example_tex/FANCyProject/FaNCyProject.tex"
   ptm.process_file(file_name, "./my_docs", depth=3)

After running this script, you should find the generated markdown files in the my_docs folder. Now you need to run the command-line

.. code-block:: bash

   make html

in the my_docs folder to generate the HTML files.

.. toctree::
   :maxdepth: 2
   :caption: Package Contents
   
   pytexmd
