# PyTeXmd

Pytexmd is a Python package designed to translate LaTeX documents to Markdown MyST and HTML. It provides utilities for filtering content, loading files, and integrating with Sphinx documentation. 

## Numbering

PyTeXmd does not automatically number theorems, displayed equations, or sections. Write any desired numbers explicitly:

```latex
\section{2 Background}
\begin{theorem}[2.3]
The statement.
\end{theorem}
\begin{equation}
x = 1 \tag{2.4}
\end{equation}
```

The theorem's optional title, the equation's `\tag`, and the section title are preserved verbatim.

## Documentation

- **Full Documentation**: [pytexmd.readthedocs.io](https://pytexmd.readthedocs.io/en/latest/index.html)
- **GitHub Repository**: [github.com/martinpflaum/pytexmd](https://github.com/martinpflaum/pytexmd)

## Installation

To install the required dependencies for pytexmd, run:

```bash
pip install -r requirements.txt
```

TikZ image generation also requires external TeX tools:

- Linux: install TeX Live with TikZ and one supported converter, for example
  `texlive-latex-extra texlive-pictures ghostscript`.
- Windows: install MiKTeX with TikZ. PyTeXmd detects standard MiKTeX user and
  system installations and can use MiKTeX's `mgs.exe` converter.

The desktop UI uses Tkinter. It is included with standard Windows Python
installations. On Debian/Ubuntu, install it with `sudo apt install python3-tk`.

## Windows And Linux Compatibility

PyTeXmd, PytexmdConverter, and PytexmdEditor use canonical absolute filesystem
paths internally and POSIX document paths for Sphinx navigation and browser
URLs. Project paths may contain spaces or Unicode and may be supplied with `~`
on Linux. Editor projects can be opened by selecting the project root,
`source/`, or `build/html/`; roots named `source` or `html` are supported.

- Windows: standard MiKTeX user/system locations and Ghostscript/MiKTeX
  converters are detected in addition to normal `PATH` lookup.
- Linux: TeX Live, Ghostscript, `pdf2svg`, and Netpbm tools are discovered from
  `PATH`. Tk applications require a graphical display and the distribution's
  Tkinter package.
- Headless systems can use `pytexmd-html` and `pytexmd-editor PROJECT
  --no-browser` without starting the converter GUI.

GitHub Actions runs the test suite and distribution build on Windows and Ubuntu
with Python 3.11 and 3.13. Generated section filenames avoid Windows device
names, while metadata and bibliography filenames are emitted as safe Python
literals in Sphinx configuration.

## Python Usage Example

Generate a complete Furo HTML site from a LaTeX entry file with the application:

```bash
pytexmd-html path/to/main.tex output/site --depth 3 --project-name "My Project" --author "Author" --version "1.0" --open
```

If pytexmd is not installed, you can run the converter directly from the
repository root without installing the package:

```bash
python -m app.PytexmdConverter.cli path/to/main.tex output/site --depth 3 --project-name "My Project"
```

The Markdown and Sphinx sources are written to `output/site/source`. The HTML
entry point is `output/site/build/html/index.html`. TikZ diagrams are rendered
through `sphinxcontrib-tikz` when a supported TeX installation and converter are
available.

For the desktop interface, run:

```bash
pytexmd-gui
```

If pytexmd is not installed, you can start the desktop interface directly from
the repository root without installing the package:

```bash
python -m app.PytexmdConverter.gui
```

Choose the main `.tex` file and output folder, enter the project metadata, and
select **Generate HTML**. The interface shows live build output and can open the
completed site automatically.

### Detected Project Files

After an entry file is selected, PytexmdConverter scans it in the background and
lists every detected file in the **Detected project files** tab. The table shows
the file category, canonical absolute path, and exact detection mechanism. The
converter switches to this tab automatically when scanning completes so missing
dependencies and name collisions are immediately visible.

PyTeXmd recursively inventories these extensions below the entry file's folder:

- LaTeX inventory: `.tex`, `.sty`, `.cls`
- Bibliographies: `.bib`, `.bbl`, `.bibtex`, `.biblatex`
- Image inventory: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.tiff`, `.svg`,
  `.pdf`, `.eps`

Only exact `\input{filename}` commands cause source files to be read and expanded.
Nested inputs are supported, but their relative paths are resolved from the main
entry file's folder. If an input resolves outside that folder, bibliography files
beside that external input are also scanned recursively. The converter reports
unresolved inputs and bare-filename collisions.

Hover over or select the **?** beside **LaTeX entry file** for the external-folder
rule and an example such as `\input{../shared/chapter}`. External folders are not
configured as a separate search path: they become available when an exact input
path resolves from the main entry file's folder.

The inventory is intentionally broader than the files consumed downstream. For
example, images and style files appear because the loader recognizes them, but
they are not currently copied merely because they were found. Commands such as
`\include`, `\includegraphics`, `\bibliography`, and `\addbibresource` are not
parsed as dependency declarations; matching files can still appear because of
the recursive extension scan.

## Project Editor

`PytexmdConverter` includes an **Open in PytexmdEditor** button. It becomes
available after the Sphinx project has been generated. You can also launch the
editor directly:

```bash
pytexmd-editor path/to/output/site
```

If the path is omitted, PytexmdEditor opens a native folder chooser:

```bash
pytexmd-editor
```

If pytexmd is not installed, you can launch the editor directly from the
repository root without installing the package:

```bash
python -m app.PytexmdEditor.editor path/to/output/site
```

The editor opens locally in your browser and provides a page navigator, editable
Sphinx preview, structured inspector, MyST source editor, and build log. It can
round-trip these visual changes back to Markdown before rebuilding the HTML:

- section headings and paragraphs
- theorem, definition, and proposition titles
- complete paragraph, proof, theorem, and custom admonition blocks
- displayed LaTeX equations, including labels and tags
- TikZ image sizing through the directive's `:xscale:` option
- complete bullet, numbered, custom-label, and definition lists

PyTeXmd already converts `\para`, proofs, built-in theorems, and custom theorem
types to semantic `prf:*` directives. PytexmdEditor treats these rendered
admonition-style blocks as editable custom admonitions while preserving
sphinx-proof numbering, labels, and cross-references. Both a whole block and its
individual leaf content are editable; the editor prevents overlapping edits from
being saved together.

The **Add Structure** panel inserts correctly formed MyST at the current source
cursor. It supports sections, subsections, paragraph/proof/theorem admonitions,
generic custom admonitions, bullet and numbered lists, custom enumerations,
equations, web links, bibliography citations, generic references, proof
references, and standalone labels. Inserted structures remain pending in the
MyST source panel until **Save MyST source** is selected.

Pages can be created, deleted, and moved up or down within their real Sphinx
toctree. The index and references pages are protected. Navigation changes create
backups and trigger a Sphinx rebuild.

Visual inspector changes write directly back to Markdown and rebuild the site;
there is no staging step. Direct heading and paragraph edits save when the
edited element loses focus. **Save MyST source** is only for changes made in the
advanced source panel. If **Rebuild** is selected while source edits are pending,
the editor asks whether to save them first and warns that rebuilding without
saving will discard them.

Lists use dedicated controls rather than a single raw-text field. Bullet and
normal enumeration items can be added, removed, and edited, while custom
enumerations additionally expose each editable item label. Whole admonitions
offer an **Add child element** control for nested paragraphs, lists, custom
enumerations, equations, proofs, theorems, and custom admonitions.

Generated HTML remains a build artifact: the editor writes changes to the
corresponding file under `source/` and rebuilds Sphinx rather than leaving edits
in HTML that the next build would overwrite. Each save creates an automatic
timestamped backup under `.pytexmd-editor/backups/`. Use the MyST source panel
for complex inline markup or directive-level edits that are not exposed by the
visual inspector.

The repository keeps the reusable conversion library in `pytexmd/`. The two
applications are separated into `app/PytexmdConverter/` and
`app/PytexmdEditor/`.

If you want to use pytexmd from a Python script, make sure your script is in the same folder (or a subfolder) as the pytexmd package, or add pytexmd to your Python path. The following example can also be found in the examples folder:

```project = 'My Project'
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


prf_realtyp_to_countertyp = {
    "axiom": "theorem",
    "theorem": "theorem",
    "lemma": "theorem",
    "algorithm": "theorem",
    "definition": "theorem",
    "remark": "theorem",
    "conjecture": "theorem",
    "corollary": "theorem",
    "criterion": "theorem",
    "example": "theorem",
    "property": "theorem",
    "observation": "theorem",
    "proposition": "theorem",
    "assumption": "theorem",
    "notation": "theorem",
}

#math_number_all = True             # number *all* displayed equations
math_eqref_format = "({number})"   # how equation refs look

html_theme = 'furo'
html_static_path = ['_static']


math_number_all = False
numfig = False
math_numfig = False

html_theme = 'furo'
html_static_path = ['_static']
# Custom theorem types (auto-generated by pytexmd)
import sphinx_proof.nodes
import sphinx_proof.proof_type
import sphinx_proof.directive
import sphinx_proof.domain
from docutils import nodes
from sphinx_proof.directive import ElementDirective

class theorem_and_definition_node(nodes.Admonition, nodes.Element):
    pass

class TheoremAndDefinitionDirective(ElementDirective):
    name = "theorem_and_definition"

class proposition_and_definition_node(nodes.Admonition, nodes.Element):
    pass

class PropositionAndDefinitionDirective(ElementDirective):
    name = "proposition_and_definition"

_CUSTOM_TYPES = {
    "theorem_and_definition": (theorem_and_definition_node, TheoremAndDefinitionDirective),
    "proposition_and_definition": (proposition_and_definition_node, PropositionAndDefinitionDirective),
}

for _name, (_node_cls, _directive_cls) in _CUSTOM_TYPES.items():
    sphinx_proof.nodes.NODE_TYPES[_name] = _node_cls
    sphinx_proof.proof_type.PROOF_TYPES[_name] = _directive_cls
    sphinx_proof.directive.DEFAULT_REALTYP_TO_COUNTERTYP[_name] = _name
    sphinx_proof.domain.ProofDomain.directives[_name] = _directive_cls
    prf_realtyp_to_countertyp[_name] = "theorem"

# PyTeXmd generates the remaining renderer registration. It delegates HTML
# structure to sphinx-proof and only substitutes the custom display names.

numfig_format = {
    "theorem_and_definition": "Theorem and Definition %s",
    "proposition_and_definition": "Proposition and Definition %s",
}
```


also in the file loader make sure that all .bib files are found also in folder mentioned in the \input thingies than concatenate these .bib file but eliminate duplicated entries also copy this thing to the created sphinx project also use of sphinxcontrib-bibtex
