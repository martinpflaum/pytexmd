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
Sphinx preview, contextual inspector, and build log. It can
round-trip these visual changes back to Markdown before rebuilding the HTML:

- section headings and paragraphs
- theorem, definition, and proposition titles
- complete paragraph, proof, theorem, and custom admonition blocks
- displayed LaTeX equations, including labels and tags
- TikZ image sizing through the directive's `:xscale:` option
- complete bullet, numbered, custom-label, and definition lists

PyTeXmd converts `\para`, proofs, built-in theorems, and custom theorem types to
non-collapsible MyST `{admonition}` directives. Semantic classes distinguish the
block type, `:name:` creates link targets, and standard `{ref}` roles provide
cross-references. Both a whole block and its individual leaf content are editable;
the editor prevents overlapping edits from being saved together.

The inspector has **General** and **Raw** tabs. General presents contextual fields
for titles, custom-admonition colors, structured lists, TikZ scale, and displayed
equation numbers using `\tag{...}`. Raw provides a large syntax-highlighted editor
for the exact selected MyST block. Clicking the page background opens the complete
page source in Raw.

Pages can be created and reordered by dragging sibling entries. Right-clicking
opens an in-app menu for copy, cut, positional paste, and deletion; paste remains
disabled until a page is in the editor clipboard. The index and references pages
are protected. Navigation changes create backups and trigger a Sphinx rebuild.

Inspector and direct preview edits are staged by their associated Markdown page.
The toolbar's **Save** button and `Ctrl+S` write all staged pages, while
**Rebuild** saves all staged pages and then rebuilds the site once.

Lists use dedicated controls rather than a single raw-text field. Bullet and
normal enumeration items can be added, removed, and edited, while custom
enumerations expose every item label and multiline body. Whole admonitions
offer an **Add child element** control for nested paragraphs, lists, custom
enumerations, equations, proofs, theorems, and custom admonitions. Nested
objects can also be selected and edited independently in the preview; the
inspector shows their nesting depth and provides a shortcut through parent
elements up to the whole-page source.
The inspector exposes the admonition title and a persistent theme-color preset
(default, blue, green, amber, red, or purple) as structured fields.
Clicking an admonition body selects the complete block and its structured title
and color controls. Clicking the rendered title instead makes the title
directly editable in place; use Save, Rebuild, or `Ctrl+S` to persist the edit.

Generated HTML remains a build artifact: the editor writes changes to the
corresponding file under `source/`; Rebuild regenerates the HTML rather than
leaving edits there for the next build to overwrite. Each save creates an
automatic timestamped backup under `.pytexmd-editor/backups/`. Use the
inspector's Raw tab for complex inline markup or directive-level edits.

The repository keeps the reusable conversion library in `pytexmd/`. The two
applications are separated into `app/PytexmdConverter/` and
`app/PytexmdEditor/`.

A generated theorem block uses standard MyST syntax:

```md
:::{admonition} Theorem 2.7
:class: pytexmd-admonition theorem
:name: theorem-example

The theorem statement.
:::

See {ref}`theorem-example`.
```
