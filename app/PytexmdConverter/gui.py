"""Tk desktop application for generating PyTeXmd HTML sites."""

from contextlib import redirect_stderr, redirect_stdout
import json
from pathlib import Path
import queue
import threading
import traceback
import webbrowser

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    from tkinter.scrolledtext import ScrolledText
except ImportError:
    tk = None
    filedialog = messagebox = ttk = ScrolledText = None

from .cli import generate_html
from .file_detection import DetectionReport, detect_project_files
from pytexmd.sphinx_doc import DEFAULT_MATHJAX_MACROS


class _ToolTip:
    """Small hover tooltip for converter form controls."""

    def __init__(self, widget, text: str):
        self.widget = widget
        self.text = text
        self.window = None
        self.after_id = None
        widget.bind("<Enter>", self._schedule, add=True)
        widget.bind("<Leave>", self._hide, add=True)
        widget.bind("<Button-1>", self._show_dialog, add=True)

    def _schedule(self, _event=None) -> None:
        self._cancel()
        self.after_id = self.widget.after(350, self._show)

    def _cancel(self) -> None:
        if self.after_id is not None:
            self.widget.after_cancel(self.after_id)
            self.after_id = None

    def _show(self) -> None:
        self.after_id = None
        if self.window is not None:
            return
        self.window = tk.Toplevel(self.widget)
        self.window.wm_overrideredirect(True)
        x = self.widget.winfo_rootx() + self.widget.winfo_width() + 6
        y = self.widget.winfo_rooty() + 2
        self.window.wm_geometry(f"+{x}+{y}")
        ttk.Label(
            self.window,
            text=self.text,
            padding=10,
            relief="solid",
            borderwidth=1,
            wraplength=430,
            justify="left",
        ).pack()

    def _hide(self, _event=None) -> None:
        self._cancel()
        if self.window is not None:
            self.window.destroy()
            self.window = None

    def _show_dialog(self, _event=None) -> None:
        self._hide()
        messagebox.showinfo("External project folders", self.text)


def parse_mathjax_macros(text: str) -> dict:
    """Parse the editable MathJax macro JSON from the GUI."""
    macros = json.loads(text)
    if not isinstance(macros, dict):
        raise ValueError("MathJax macros must be a JSON object.")
    return macros


class _QueueWriter:
    def __init__(self, events: queue.Queue):
        self.events = events

    def write(self, text: str) -> int:
        if text:
            self.events.put(("log", text))
        return len(text)

    def flush(self) -> None:
        pass


class PyTeXmdGui:
    """Responsive Tk interface around :func:`generate_html`."""

    def __init__(self, root):
        self.root = root
        self.events = queue.Queue()
        self.generated_index = None
        self.editor_server = None
        self.editor_thread = None
        self.editor_project = None
        self.detection_after = None

        root.title("PytexmdConverter")
        root.geometry("900x800")
        root.minsize(680, 620)

        self.input_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.project_var = tk.StringVar(value="My Project")
        self.author_var = tk.StringVar(value="Author")
        self.version_var = tk.StringVar(value="1.0")
        self.depth_var = tk.IntVar(value=3)
        self.open_var = tk.BooleanVar(value=True)
        self.status_var = tk.StringVar(value="Choose a LaTeX entry file to begin.")

        self._configure_style()
        self._build_ui()
        self.input_var.trace_add("write", self._input_path_changed)
        self.output_var.trace_add("write", self._update_editor_button)
        root.protocol("WM_DELETE_WINDOW", self._close)
        root.after(100, self._drain_events)

    def _configure_style(self) -> None:
        style = ttk.Style(self.root)
        if "vista" in style.theme_names():
            style.theme_use("vista")
        style.configure("Title.TLabel", font=("Segoe UI Semibold", 18))
        style.configure("Subtitle.TLabel", foreground="#4b5563")
        style.configure(
            "Action.TButton", font=("Segoe UI Semibold", 10), padding=(16, 8)
        )

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=24)
        outer.pack(fill="both", expand=True)

        ttk.Label(outer, text="PytexmdConverter", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            outer,
            text="Convert a LaTeX project into a searchable Furo/Sphinx website.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(2, 20))

        form = ttk.LabelFrame(outer, text="Project", padding=16)
        form.pack(fill="x")
        form.columnconfigure(1, weight=1)

        self._path_row(
            form,
            0,
            "LaTeX entry file",
            self.input_var,
            self._browse_input,
            tooltip=(
                r"External folders are discovered through exact \input{...} "
                "references. Place the folder anywhere reachable from the entry "
                r"file and use a relative path such as \input{../shared/chapter}. "
                "All input paths, including nested inputs, resolve from the main "
                "entry file's folder. After an external input resolves, PyTeXmd "
                "also scans its folder recursively for .bib, .bbl, .bibtex, and "
                ".biblatex files."
            ),
        )
        self._path_row(form, 1, "Output folder", self.output_var, self._browse_output)

        ttk.Label(form, text="Project name").grid(row=2, column=0, sticky="w", pady=7)
        ttk.Entry(form, textvariable=self.project_var).grid(
            row=2, column=1, columnspan=2, sticky="ew", padx=(14, 0), pady=7
        )
        ttk.Label(form, text="Author").grid(row=3, column=0, sticky="w", pady=7)
        ttk.Entry(form, textvariable=self.author_var).grid(
            row=3, column=1, columnspan=2, sticky="ew", padx=(14, 0), pady=7
        )

        options = ttk.Frame(form)
        options.grid(row=4, column=1, columnspan=2, sticky="w", padx=(14, 0), pady=7)
        ttk.Label(form, text="Build options").grid(row=4, column=0, sticky="w", pady=7)
        ttk.Label(options, text="Version").pack(side="left")
        ttk.Entry(options, textvariable=self.version_var, width=10).pack(
            side="left", padx=(7, 20)
        )
        ttk.Label(options, text="Split depth").pack(side="left")
        ttk.Spinbox(options, from_=0, to=10, textvariable=self.depth_var, width=5).pack(
            side="left", padx=(7, 0)
        )

        ttk.Label(form, text="MathJax macros").grid(
            row=5, column=0, sticky="nw", pady=7
        )
        self.macros = ScrolledText(
            form,
            height=9,
            wrap="none",
            font=("Cascadia Mono", 9),
        )
        self.macros.grid(
            row=5, column=1, columnspan=2, sticky="ew", padx=(14, 0), pady=7
        )
        self.macros.insert("1.0", json.dumps(DEFAULT_MATHJAX_MACROS, indent=4))

        actions = ttk.Frame(outer)
        actions.pack(fill="x", pady=16)
        self.generate_button = ttk.Button(
            actions,
            text="Generate HTML",
            style="Action.TButton",
            command=self._start_generation,
        )
        self.generate_button.pack(side="left")
        self.open_button = ttk.Button(
            actions, text="Open Site", command=self._open_site, state="disabled"
        )
        self.open_button.pack(side="left", padx=10)
        self.editor_button = ttk.Button(
            actions,
            text="Open in PytexmdEditor",
            command=self._open_editor,
            state="disabled",
        )
        self.editor_button.pack(side="left")
        ttk.Checkbutton(
            actions, text="Open when complete", variable=self.open_var
        ).pack(side="right")

        self.progress = ttk.Progressbar(outer, mode="indeterminate")
        self.progress.pack(fill="x")
        ttk.Label(outer, textvariable=self.status_var).pack(anchor="w", pady=(7, 10))

        self.notebook = ttk.Notebook(outer)
        self.notebook.pack(fill="both", expand=True)

        log_frame = ttk.Frame(self.notebook, padding=8)
        self.notebook.add(log_frame, text="Build log")
        self.log = ScrolledText(
            log_frame,
            height=12,
            wrap="word",
            font=("Cascadia Mono", 9),
            state="disabled",
        )
        self.log.pack(fill="both", expand=True)

        self.files_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.files_frame, text="Detected project files")
        ttk.Label(
            self.files_frame,
            text=(
                "PyTeXmd inventories supported extensions recursively. Only exact "
                "\\input{...} commands expand source files; inventory does not mean "
                "that an image or style file is copied into the generated project."
            ),
            style="Subtitle.TLabel",
            wraplength=790,
            justify="left",
        ).pack(fill="x", pady=(0, 8))
        self.files_summary_var = tk.StringVar(
            value="Choose a LaTeX entry file to scan."
        )
        ttk.Label(self.files_frame, textvariable=self.files_summary_var).pack(
            fill="x", pady=(0, 8)
        )
        tree_frame = ttk.Frame(self.files_frame)
        tree_frame.pack(fill="both", expand=True)
        tree_frame.rowconfigure(0, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        self.files_tree = ttk.Treeview(
            tree_frame,
            columns=("category", "file", "method"),
            show="headings",
            height=10,
        )
        self.files_tree.heading("category", text="Type")
        self.files_tree.heading("file", text="File")
        self.files_tree.heading("method", text="How PyTeXmd detects it")
        self.files_tree.column("category", width=125, stretch=False)
        self.files_tree.column("file", width=290)
        self.files_tree.column("method", width=330)
        self.files_tree.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self.files_tree.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.files_tree.configure(yscrollcommand=scrollbar.set)
        ttk.Label(
            self.files_frame,
            text=(
                "Recognized inventory: .tex .sty .cls | .bib .bbl .bibtex "
                ".biblatex | .png .jpg .jpeg .gif .bmp .tiff .svg .pdf .eps. "
                "Commands such as \\include, \\includegraphics, \\bibliography, "
                "and \\addbibresource are not parsed as dependency declarations."
            ),
            wraplength=790,
            justify="left",
        ).pack(fill="x", pady=(8, 0))

    def _path_row(
        self, parent, row, label, variable, command, tooltip: str | None = None
    ) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=7)
        ttk.Entry(parent, textvariable=variable).grid(
            row=row, column=1, sticky="ew", padx=(14, 8), pady=7
        )
        controls = ttk.Frame(parent)
        controls.grid(row=row, column=2, pady=7)
        ttk.Button(controls, text="Browse...", command=command).pack(side="left")
        if tooltip:
            help_label = ttk.Label(
                controls,
                text="?",
                width=2,
                anchor="center",
                cursor="question_arrow",
                relief="solid",
            )
            help_label.pack(side="left", padx=(5, 0))
            _ToolTip(help_label, tooltip)

    def _browse_input(self) -> None:
        filename = filedialog.askopenfilename(
            title="Select the main LaTeX file",
            filetypes=(("LaTeX files", "*.tex"), ("All files", "*.*")),
        )
        if not filename:
            return
        self.input_var.set(filename)
        if self.project_var.get() == "My Project":
            self.project_var.set(Path(filename).stem)
        if not self.output_var.get():
            self.output_var.set(str(Path(filename).parent / "pytexmd-output"))

    def _browse_output(self) -> None:
        directory = filedialog.askdirectory(title="Select the output folder")
        if directory:
            self.output_var.set(directory)

    def _input_path_changed(self, *_args) -> None:
        if self.detection_after is not None:
            self.root.after_cancel(self.detection_after)
        self.detection_after = self.root.after(350, self._start_file_detection)

    def _start_file_detection(self) -> None:
        self.detection_after = None
        input_file = self.input_var.get().strip()
        if not input_file or not Path(input_file).expanduser().is_file():
            self._clear_detected_files("Choose an existing LaTeX entry file to scan.")
            return
        self._clear_detected_files("Scanning the LaTeX project...")
        threading.Thread(
            target=self._detect_files_worker, args=(input_file,), daemon=True
        ).start()

    def _detect_files_worker(self, input_file: str) -> None:
        try:
            report = detect_project_files(input_file)
        except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
            self.events.put(("files_error", (input_file, str(exc))))
        else:
            self.events.put(("files", (input_file, report)))

    def _clear_detected_files(self, message: str) -> None:
        children = self.files_tree.get_children()
        if children:
            self.files_tree.delete(*children)
        self.files_summary_var.set(message)

    def _show_detected_files(self, input_file: str, report: DetectionReport) -> None:
        current = self.input_var.get().strip()
        if (
            not current
            or Path(current).expanduser().resolve()
            != Path(input_file).expanduser().resolve()
        ):
            return
        children = self.files_tree.get_children()
        if children:
            self.files_tree.delete(*children)
        for detected in report.files:
            self.files_tree.insert(
                "",
                "end",
                values=(
                    detected.category,
                    str(detected.path.resolve()),
                    "; ".join(detected.mechanisms),
                ),
            )
        for argument in report.missing_inputs:
            self.files_tree.insert(
                "", "end", values=("Missing input", argument, "unresolved \\input")
            )
        for collision in report.collisions:
            self.files_tree.insert(
                "",
                "end",
                values=("Name collision", collision, "same bare-basename lookup key"),
            )
        for warning in report.warnings:
            self.files_tree.insert("", "end", values=("Read warning", warning, ""))
        self.files_summary_var.set(
            f"{len(report.files)} files detected from {report.root}. "
            f"{len(report.missing_inputs)} unresolved inputs; "
            f"{len(report.collisions)} basename collisions."
        )
        self.notebook.select(self.files_frame)

    def _update_editor_button(self, *_args) -> None:
        output = self.output_var.get().strip()
        available = bool(
            output and (Path(output).expanduser() / "source" / "conf.py").is_file()
        )
        self.editor_button.configure(state="normal" if available else "disabled")

    def _start_generation(self) -> None:
        input_file = self.input_var.get().strip()
        output_folder = self.output_var.get().strip()
        if not input_file or not output_folder:
            messagebox.showerror(
                "Missing paths", "Choose an input file and output folder."
            )
            return

        try:
            depth = int(self.depth_var.get())
        except (TypeError, ValueError):
            messagebox.showerror("Invalid depth", "Split depth must be an integer.")
            return

        try:
            mathjax_macros = parse_mathjax_macros(self.macros.get("1.0", "end"))
        except (json.JSONDecodeError, ValueError) as exc:
            messagebox.showerror("Invalid macros", str(exc))
            return

        self.generated_index = None
        self.open_button.configure(state="disabled")
        self.generate_button.configure(state="disabled")
        self.progress.start(12)
        self.status_var.set("Generating Markdown and building Sphinx HTML...")
        self._clear_log()

        arguments = (
            input_file,
            output_folder,
            depth,
            self.project_var.get().strip() or "My Project",
            self.author_var.get().strip() or "Author",
            self.version_var.get().strip() or "1.0",
            mathjax_macros,
        )
        threading.Thread(
            target=self._generate_worker, args=arguments, daemon=True
        ).start()

    def _generate_worker(
        self,
        input_file,
        output_folder,
        depth,
        project_name,
        author,
        version,
        mathjax_macros,
    ) -> None:
        writer = _QueueWriter(self.events)
        try:
            with redirect_stdout(writer), redirect_stderr(writer):
                index_path = generate_html(
                    input_file,
                    output_folder,
                    depth=depth,
                    project_name=project_name,
                    author=author,
                    version=version,
                    mathjax_macros=mathjax_macros,
                )
        except Exception as exc:
            self.events.put(("log", traceback.format_exc()))
            self.events.put(("error", str(exc)))
        else:
            self.events.put(("success", index_path))

    def _drain_events(self) -> None:
        try:
            while True:
                event, value = self.events.get_nowait()
                if event == "log":
                    self._append_log(value)
                elif event == "success":
                    self._generation_succeeded(value)
                elif event == "error":
                    self._generation_failed(value)
                elif event == "files":
                    self._show_detected_files(*value)
                elif event == "files_error":
                    input_file, error = value
                    if self.input_var.get().strip() == input_file:
                        self._clear_detected_files(f"Could not scan project: {error}")
        except queue.Empty:
            pass
        self.root.after(100, self._drain_events)

    def _generation_succeeded(self, index_path: Path) -> None:
        self.progress.stop()
        self.generate_button.configure(state="normal")
        self.open_button.configure(state="normal")
        self.editor_button.configure(state="normal")
        self.generated_index = index_path
        self.status_var.set(f"HTML site generated at {index_path}")
        if self.open_var.get():
            self._open_site()

    def _generation_failed(self, error: str) -> None:
        self.progress.stop()
        self.generate_button.configure(state="normal")
        self.status_var.set("Generation failed. See the build log for details.")
        messagebox.showerror("Generation failed", error)

    def _open_site(self) -> None:
        if self.generated_index is not None:
            webbrowser.open(self.generated_index.as_uri())

    def _open_editor(self) -> None:
        project = self.output_var.get().strip()
        if not project:
            messagebox.showerror(
                "Missing project", "Choose a Sphinx output folder first."
            )
            return
        project_path = Path(project).expanduser().resolve()
        if not (project_path / "source" / "conf.py").is_file():
            messagebox.showerror(
                "Project not generated",
                "Generate the Sphinx project before opening the project editor.",
            )
            return
        if (
            self.editor_server is not None
            and self.editor_project == project_path
            and self.editor_thread is not None
            and self.editor_thread.is_alive()
        ):
            webbrowser.open(self.editor_server.editor_url)
            return
        if self.editor_server is not None:
            if self.editor_thread is not None and self.editor_thread.is_alive():
                self.editor_server.shutdown()
                self.editor_thread.join(timeout=2)
            self.editor_server.server_close()
        from app.PytexmdEditor.editor import launch_editor

        try:
            self.editor_server = launch_editor(project_path, open_browser=False)
        except (OSError, ValueError) as exc:
            messagebox.showerror("Could not open editor", str(exc))
            return
        self.editor_project = project_path
        self.editor_thread = threading.Thread(
            target=self.editor_server.serve_forever, daemon=True
        )
        self.editor_thread.start()
        webbrowser.open(self.editor_server.editor_url)

    def _close(self) -> None:
        if self.editor_server is not None:
            if self.editor_thread is not None and self.editor_thread.is_alive():
                self.editor_server.shutdown()
                self.editor_thread.join(timeout=2)
            self.editor_server.server_close()
        self.root.destroy()

    def _append_log(self, text: str) -> None:
        self.log.configure(state="normal")
        self.log.insert("end", text)
        self.log.see("end")
        self.log.configure(state="disabled")

    def _clear_log(self) -> None:
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")


def main() -> None:
    if tk is None:
        raise SystemExit(
            "Tkinter is required for pytexmd-gui. On Debian/Ubuntu install "
            "it with: sudo apt install python3-tk"
        )
    try:
        root = tk.Tk()
    except tk.TclError as exc:
        raise SystemExit(
            "PytexmdConverter requires a graphical display. On headless Linux, "
            "run pytexmd-html instead."
        ) from exc
    PyTeXmdGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
