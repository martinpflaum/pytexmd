Welcome To PyTeXmd'S Documentation!
===================================
PyTeXmd is a Python designed to translate LaTeX documents to markdown myst and html. It provides utilities for filtering content, loading files, and integrating with Sphinx documentation. The aims to streamline workflows involving Markdown and LaTeX, making it easier to automate document generation, conversion, and integration with Python projects. 

Installation
------------

To install the required dependencies for pytexmd, run:

.. code-block:: bash

   pip install -r requirements.txt

This will install all necessarys for using pytexmd, including Sphinx and MyST support. Also make sure to install texlive in ubuntu you can run the following command:
.. code-block:: bash

   sudo apt update && sudo apt install -y texlive-base texlive-binaries texlive-fonts-recommended texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-plain-generic
or visit the texlive website for other operating systems: https://www.tug.org/texlive/

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

Applications
------------

The package provides two applications: a converter (command line or desktop
interface) that turns a LaTeX project into a Sphinx HTML site, and a
browser-based project editor for the generated site. Each can be started either
through its installed command or directly with Python, without installing the
package.

Command-Line Converter
~~~~~~~~~~~~~~~~~~~~~~

Generate a complete Furo HTML site from a LaTeX entry file with:

.. code-block:: bash

   pytexmd-html path/to/main.tex output/site --depth 3 --project-name "My Project" --author "Author" --version "1.0" --open

Without installing the package, run the converter module directly from the
repository root:

.. code-block:: bash

   python -m app.PytexmdConverter.cli path/to/main.tex output/site --depth 3 --project-name "My Project"

The Markdown and Sphinx sources are written to ``output/site/source`` and the
HTML entry point is ``output/site/build/html/index.html``.

Desktop Converter
~~~~~~~~~~~~~~~~~

The desktop interface is started with:

.. code-block:: bash

   pytexmd-gui

or without installing the package, from the repository root:

.. code-block:: bash

   python -m app.PytexmdConverter.gui

Choose the main ``.tex`` file and output folder, enter the project metadata, and
select **Generate HTML**. The interface shows live build output and can open the
completed site automatically.

Project Editor
~~~~~~~~~~~~~~

Open the browser-based editor for a generated Sphinx project with:

.. code-block:: bash

   pytexmd-editor path/to/output/site

or without installing the package, from the repository root:

.. code-block:: bash

   python -m app.PytexmdEditor.editor path/to/output/site

Add ``--no-browser`` to start the editor server without opening a browser. The
editor provides a page navigator, editable preview, MyST source editor, and a
build log. Saved edits are written back to the Markdown sources under
``source/`` and the site is rebuilt.

.. toctree::
   :maxdepth: 2
   :caption: Package Contents
   
   pytexmd
