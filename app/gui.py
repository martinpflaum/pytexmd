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
from pytexmd.sphinx_doc import DEFAULT_MATHJAX_MACROS


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

        root.title("PyTeXmd HTML Generator")
        root.geometry("820x760")
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
        root.after(100, self._drain_events)

    def _configure_style(self) -> None:
        style = ttk.Style(self.root)
        if "vista" in style.theme_names():
            style.theme_use("vista")
        style.configure("Title.TLabel", font=("Segoe UI Semibold", 18))
        style.configure("Subtitle.TLabel", foreground="#4b5563")
        style.configure("Action.TButton", font=("Segoe UI Semibold", 10), padding=(16, 8))

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=24)
        outer.pack(fill="both", expand=True)

        ttk.Label(outer, text="PyTeXmd HTML Generator", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            outer,
            text="Convert a LaTeX project into a searchable Furo/Sphinx website.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(2, 20))

        form = ttk.LabelFrame(outer, text="Project", padding=16)
        form.pack(fill="x")
        form.columnconfigure(1, weight=1)

        self._path_row(form, 0, "LaTeX entry file", self.input_var, self._browse_input)
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

        ttk.Label(form, text="MathJax macros").grid(row=5, column=0, sticky="nw", pady=7)
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
        ttk.Checkbutton(
            actions, text="Open when complete", variable=self.open_var
        ).pack(side="right")

        self.progress = ttk.Progressbar(outer, mode="indeterminate")
        self.progress.pack(fill="x")
        ttk.Label(outer, textvariable=self.status_var).pack(anchor="w", pady=(7, 10))

        log_frame = ttk.LabelFrame(outer, text="Build log", padding=8)
        log_frame.pack(fill="both", expand=True)
        self.log = ScrolledText(
            log_frame,
            height=12,
            wrap="word",
            font=("Cascadia Mono", 9),
            state="disabled",
        )
        self.log.pack(fill="both", expand=True)

    def _path_row(self, parent, row, label, variable, command) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=7)
        ttk.Entry(parent, textvariable=variable).grid(
            row=row, column=1, sticky="ew", padx=(14, 8), pady=7
        )
        ttk.Button(parent, text="Browse...", command=command).grid(
            row=row, column=2, pady=7
        )

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

    def _start_generation(self) -> None:
        input_file = self.input_var.get().strip()
        output_folder = self.output_var.get().strip()
        if not input_file or not output_folder:
            messagebox.showerror("Missing paths", "Choose an input file and output folder.")
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
        self, input_file, output_folder, depth, project_name, author, version,
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
        except queue.Empty:
            pass
        self.root.after(100, self._drain_events)

    def _generation_succeeded(self, index_path: Path) -> None:
        self.progress.stop()
        self.generate_button.configure(state="normal")
        self.open_button.configure(state="normal")
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
    root = tk.Tk()
    PyTeXmdGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
