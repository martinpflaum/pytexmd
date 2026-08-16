const state = {
  pages: [],
  page: null,
  elements: [],
  selection: null,
  sourceDirty: false,
};

const $ = (id) => document.getElementById(id);
const emptyInspectorDefault = $("emptyInspector").innerHTML;

function toast(message) {
  const node = $("toast");
  node.textContent = message;
  node.classList.add("show");
  setTimeout(() => node.classList.remove("show"), 2200);
}

function setBusy(value) {
  document.querySelectorAll("button").forEach((button) => {
    if (!button.closest("dialog")) button.disabled = value;
  });
  if (!value) updatePageActions();
}

function setStatus(text) {
  $("status").textContent = text;
}

function showLog(log) {
  $("buildLog").textContent = log || "Build completed.";
  $("buildLog").classList.add("visible");
  setStatus("Ready");
}

async function request(url, options) {
  const response = await fetch(url, options);
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || "Request failed");
  return data;
}

function post(url, body = {}) {
  return request(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

function currentSourceElement(kind, index) {
  return state.elements.find((item) => item.kind === kind && item.index === index);
}

function updatePageActions() {
  const selected = state.page;
  const canMove = Boolean(selected && selected.parent);
  $("moveUpButton").disabled = !canMove;
  $("moveDownButton").disabled = !canMove;
  $("deletePageButton").disabled = !selected || selected.protected;
}

function renderPages(filter = "") {
  const list = $("pageList");
  list.innerHTML = "";
  const query = filter.toLowerCase();
  state.pages
    .filter((page) => `${page.title} ${page.path}`.toLowerCase().includes(query))
    .forEach((page) => {
      const button = document.createElement("button");
      button.className =
        "page-item" +
        (page.parent ? " child" : "") +
        (state.page?.path === page.path ? " active" : "");
      button.innerHTML = "<strong></strong><small></small>";
      button.querySelector("strong").textContent = page.title;
      button.querySelector("small").textContent = page.path;
      button.onclick = () => openPage(page);
      list.append(button);
    });
  $("pageCount").textContent = state.pages.length;
  updatePageActions();
}

async function loadProject(selectedPath = null) {
  const project = await request("/api/project");
  state.pages = project.pages;
  $("projectPath").textContent = project.root;
  renderPages($("pageSearch").value);
  const selected =
    state.pages.find((page) => page.path === selectedPath) || state.pages[0];
  if (selected) await openPage(selected);
}

async function openPage(page) {
  if (state.sourceDirty) {
    toast("Save or discard current edits before reloading or changing pages.");
    return;
  }
  state.page = page;
  state.selection = null;
  state.sourceDirty = false;
  const data = await request(`/api/page?path=${encodeURIComponent(page.path)}`);
  state.elements = data.elements;
  $("sourceEditor").value = data.markdown;
  $("pageTitle").textContent = page.title;
  $("preview").src = `${page.preview}?v=${Date.now()}`;
  $("emptyInspector").classList.remove("hidden");
  $("emptyInspector").innerHTML = emptyInspectorDefault;
  $("inspectorForm").classList.add("hidden");
  renderPages($("pageSearch").value);
}

function selectElement(message) {
  const source = currentSourceElement(message.kind, message.index);
  if (!source) {
    state.selection = null;
    $("inspectorForm").classList.add("hidden");
    $("emptyInspector").classList.remove("hidden");
    $("emptyInspector").innerHTML =
      "<strong>Generated Sphinx element</strong><span>This rendered element has no independent Markdown source block. Select its parent admonition or use the MyST source panel.</span>";
    return;
  }
  state.selection = { kind: message.kind, index: message.index };
  $("emptyInspector").classList.add("hidden");
  $("emptyInspector").innerHTML = emptyInspectorDefault;
  $("inspectorForm").classList.remove("hidden");
  $("elementType").value = message.kind.replace("_", " ");
  $("elementValue").value =
    source?.value ?? message.value;
  const structuredList = message.kind === "list" && source?.metadata?.style !== "raw";
  $("valueLabel").classList.toggle("hidden", structuredList);
  $("listEditor").classList.toggle("hidden", !structuredList);
  $("childTools").classList.toggle("hidden", message.kind !== "admonition");
  if (structuredList) renderListEditor(source.metadata);
  const help = {
    heading: "Edit the section heading. Markdown heading depth is preserved.",
    paragraph:
      "Visual paragraph edits become plain MyST text. Use the source panel to preserve complex inline markup.",
    directive_title: "Edit the theorem, definition, or proposition title.",
    equation: "Edit the LaTeX equation source. Labels and tags may be included.",
    tikz_scale: "Scale the rendered TikZ image from 0.1 to 4.",
    admonition:
      "Edit the complete semantic MyST block, including its type, title, label, options, nested equations, and body.",
    list: "Add, remove, and edit items. Custom labels are editable only for custom enumerations.",
  };
  $("fieldHelp").textContent = help[message.kind] || "";
  $("valueLabel").firstChild.textContent =
    message.kind === "tikz_scale" ? "Scale " : "Content ";
}

function renderListEditor(metadata) {
  state.currentListStyle = metadata.style;
  const names = {
    bullet: "Bullet points",
    ordered: "Numbered enumeration",
    enumeration: "LaTeX enumeration",
    custom_enumeration: "Custom-label enumeration",
  };
  $("listStyleLabel").textContent = names[metadata.style] || "List items";
  $("listItems").innerHTML = "";
  metadata.items.forEach((item) => addListItemRow(item));
}

function addListItemRow(item = { label: "", content: "" }) {
  const custom = state.currentListStyle === "custom_enumeration";
  const row = document.createElement("div");
  row.className = `list-item-row${custom ? "" : " no-label"}`;
  if (custom) {
    const label = document.createElement("input");
    label.className = "item-label";
    label.placeholder = "Item label";
    label.value = item.label;
    row.append(label);
  }
  const content = document.createElement("input");
  content.className = "item-content";
  content.placeholder = "Item content";
  content.value = item.content;
  row.append(content);
  const remove = document.createElement("button");
  remove.className = "remove-item";
  remove.type = "button";
  remove.title = "Remove item";
  remove.textContent = "x";
  remove.onclick = () => row.remove();
  row.append(remove);
  $("listItems").append(row);
}

function serializeListEditor() {
  const rows = [...$("listItems").querySelectorAll(".list-item-row")];
  if (!rows.length) throw new Error("A list must contain at least one item.");
  return rows
    .map((row, index) => {
      const content = row.querySelector(".item-content").value.trim();
      if (!content) throw new Error(`List item ${index + 1} cannot be empty.`);
      if (state.currentListStyle === "bullet") return `- ${content}`;
      if (state.currentListStyle === "ordered") return `${index + 1}. ${content}`;
      if (state.currentListStyle === "enumeration") return `${index + 1}.\n: ${content}`;
      const label = row.querySelector(".item-label").value.trim();
      if (!label) throw new Error(`Custom item ${index + 1} needs a label.`);
      return `${label}\n: ${content}`;
    })
    .join("\n");
}

async function saveSingleVisual(change) {
  if (state.sourceDirty) {
    toast("Save or discard MyST source changes before editing the preview.");
    return false;
  }
  const pagePath = state.page?.path;
  if (!pagePath) return false;
  setBusy(true);
  setStatus("Saving change to Markdown and rebuilding...");
  try {
    const result = await post("/api/visual-save", {
      path: pagePath,
      changes: [change],
    });
    showLog(result.log);
    await loadProject(pagePath);
    toast("Change saved to Markdown.");
    return true;
  } catch (error) {
    toast(error.message);
    setStatus("Save failed");
    return false;
  } finally {
    setBusy(false);
  }
}

async function saveSource() {
  if (!state.page) return;
  setBusy(true);
  setStatus("Saving MyST source and rebuilding...");
  try {
    const result = await post("/api/save", {
      path: state.page.path,
      markdown: $("sourceEditor").value,
      rebuild: true,
    });
    showLog(result.log);
    state.sourceDirty = false;
    await loadProject(state.page.path);
    toast("MyST source saved.");
  } catch (error) {
    toast(error.message);
    setStatus("Save failed");
  } finally {
    setBusy(false);
  }
}

async function rebuild(discardSource = false) {
  if (state.sourceDirty && !discardSource) {
    $("rebuildDialogTitle").textContent = "Unsaved MyST source";
    $("rebuildDialogText").textContent =
      "The MyST source panel contains changes that have not been written to the current Markdown file.";
    $("saveAndRebuildButton").textContent = "Save MyST source and rebuild";
    $("rebuildDialog").showModal();
    return;
  }
  setBusy(true);
  setStatus("Building Sphinx project...");
  try {
    const result = await post("/api/build");
    showLog(result.log);
    state.sourceDirty = false;
    if (state.page) await loadProject(state.page.path);
    toast(discardSource ? "Unsaved source edits discarded." : "Build complete.");
  } catch (error) {
    toast(error.message);
    setStatus("Build failed");
  } finally {
    setBusy(false);
  }
}

async function managePage(url, body, selectedPath) {
  if (state.sourceDirty) {
    toast("Save or discard current edits before changing page navigation.");
    return;
  }
  setBusy(true);
  setStatus("Updating navigation and rebuilding...");
  try {
    const result = await post(url, body);
    showLog(result.log);
    await loadProject(selectedPath || result.page);
    toast("Page navigation updated.");
  } catch (error) {
    toast(error.message);
    setStatus("Page update failed");
  } finally {
    setBusy(false);
  }
}

const insertConfiguration = {
  section: {
    title: "Section title",
    target: "Optional section label",
    content: "Optional introductory content",
    help: "Creates a level-two section and an optional MyST label.",
  },
  subsection: {
    title: "Subsection title",
    target: "Optional subsection label",
    content: "Optional introductory content",
    help: "Creates a level-three subsection and an optional MyST label.",
  },
  paragraph: {
    title: "Paragraph title",
    target: "Optional paragraph label",
    content: "Paragraph content",
    help: "Creates an editable prf:paragraph custom admonition.",
  },
  proof: {
    title: "Optional proof title",
    target: "Optional proof label",
    content: "Proof content",
    help: "Creates a semantic prf:proof admonition.",
  },
  theorem: {
    title: "Theorem title or manual number",
    target: "Optional theorem label",
    content: "Theorem statement",
    help: "Creates an unnumbered semantic theorem with a manual title.",
  },
  admonition: {
    title: "Admonition title",
    target: "Optional CSS class",
    content: "Admonition content",
    help: "Creates a generic custom MyST admonition.",
  },
  bullet_list: {
    title: null,
    target: null,
    content: "One item per line",
    help: "Each non-empty line becomes a bullet item.",
  },
  numbered_list: {
    title: null,
    target: null,
    content: "One item per line",
    help: "Each non-empty line becomes a numbered Markdown item.",
  },
  custom_enumeration: {
    title: null,
    target: null,
    content: "One 'custom label | item text' pair per line",
    help: "Creates a MyST definition list for custom enumeration labels.",
  },
  equation: {
    title: null,
    target: "Optional equation label",
    content: "LaTeX equation",
    help: "Creates a MyST math directive with an optional label.",
  },
  link: {
    title: "Link text",
    target: "URL",
    content: null,
    help: "Creates a Markdown link that renders as an HTML anchor.",
  },
  citation: {
    title: "Optional display text",
    target: "Citation key or comma-separated keys",
    content: null,
    help: "Creates a sphinxcontrib-bibtex citation role.",
  },
  reference: {
    title: "Optional display text",
    target: "Section, equation, or generic label",
    content: null,
    help: "Creates a Sphinx {ref} role.",
  },
  proof_reference: {
    title: null,
    target: "Theorem, proof, or paragraph label",
    content: null,
    help: "Creates a sphinx-proof {prf:ref} role.",
  },
  label: {
    title: null,
    target: "New label name",
    content: null,
    help: "Creates a standalone MyST target for sections or nearby content.",
  },
};

function configureInsertDialog() {
  const kind = $("insertKind").value;
  const config = insertConfiguration[kind];
  const sourcePanel = $("sourceEditor").closest("details");
  state.insertionPosition = sourcePanel.open
    ? $("sourceEditor").selectionStart
    : $("sourceEditor").value.length;
  $("insertDialogTitle").textContent =
    `Insert ${$("insertKind").selectedOptions[0].textContent}`;
  for (const [field, label] of [
    ["Title", config.title],
    ["Target", config.target],
    ["Content", config.content],
  ]) {
    const labelNode = $(`insert${field}Label`);
    const input = $(`insert${field}`);
    labelNode.classList.toggle("hidden", label === null);
    if (label !== null) labelNode.firstChild.textContent = `${label} `;
    input.value = "";
  }
  $("insertHelp").textContent = config.help;
  $("insertDialog").showModal();
}

function directive(name, title, target, content, options = []) {
  const optionLines = [...options];
  if (target) optionLines.push(`:label: ${target}`);
  const optionBlock = optionLines.length ? `${optionLines.join("\n")}\n\n` : "";
  return `:::{${name}}${title ? ` ${title}` : ""}\n${optionBlock}${content}\n:::`;
}

function buildInsertion(kind, title, target, content) {
  const items = content.split(/\r?\n/).map((item) => item.trim()).filter(Boolean);
  if (["section", "subsection", "paragraph", "theorem", "admonition", "link"].includes(kind) && !title) {
    throw new Error("A title or display text is required.");
  }
  if (["link", "citation", "reference", "proof_reference", "label"].includes(kind) && !target) {
    throw new Error("A target, URL, citation key, or label is required.");
  }
  if (target && !["link", "citation", "admonition"].includes(kind) && !/^[A-Za-z0-9_.:-]+$/.test(target)) {
    throw new Error("Labels may contain letters, numbers, underscores, dots, colons, and hyphens.");
  }
  switch (kind) {
    case "section":
      return `${target ? `(${target})=\n` : ""}## ${title}${content ? `\n\n${content}` : ""}`;
    case "subsection":
      return `${target ? `(${target})=\n` : ""}### ${title}${content ? `\n\n${content}` : ""}`;
    case "paragraph":
      return directive("prf:paragraph", title, target, content, [":nonumber:"]);
    case "proof":
      return directive("prf:proof", title, target, content);
    case "theorem":
      return directive("prf:theorem", title, target, content, [":nonumber:"]);
    case "admonition":
      return directive("admonition", title, "", content, target ? [`:class: ${target}`] : []);
    case "bullet_list":
      return items.map((item) => `- ${item}`).join("\n");
    case "numbered_list":
      return items.map((item, index) => `${index + 1}. ${item}`).join("\n");
    case "custom_enumeration":
      return items
        .map((item, index) => {
          const [label, ...body] = item.split("|");
          return `${body.length ? label.trim() : `Item ${index + 1}`}\n: ${body.length ? body.join("|").trim() : label.trim()}`;
        })
        .join("\n");
    case "equation":
      return directive("math", "", target, content);
    case "link":
      return `[${title}](${target})`;
    case "citation":
      return title ? `{cite}\`${title} <${target}>\`` : `{cite}\`${target}\``;
    case "reference":
      return title ? `{ref}\`${title} <${target}>\`` : `{ref}\`${target}\``;
    case "proof_reference":
      return `{prf:ref}\`${target}\``;
    case "label":
      return `(${target})=`;
    default:
      throw new Error("Unsupported insertion type.");
  }
}

$("inspectorForm").onsubmit = async (event) => {
  event.preventDefault();
  if (!state.selection) return;
  try {
    const value = state.selection.kind === "list" && !$("listEditor").classList.contains("hidden")
      ? serializeListEditor()
      : $("elementValue").value;
    await saveSingleVisual({ ...state.selection, value });
  } catch (error) {
    toast(error.message);
  }
};

$("addListItemButton").onclick = () => addListItemRow();

$("newPageForm").onsubmit = async (event) => {
  event.preventDefault();
  $("newPageDialog").close();
  await managePage("/api/pages/create", {
    title: $("newPageTitle").value,
    slug: $("newPageSlug").value,
  });
  event.target.reset();
};

$("openInsertButton").onclick = () => {
  if (!state.page) return;
  state.insertionMode = "source";
  configureInsertDialog();
};
$("addChildButton").onclick = () => {
  if (!state.selection || state.selection.kind !== "admonition") return;
  state.insertionMode = "child";
  $("insertKind").value = $("childKind").value;
  configureInsertDialog();
};
$("insertForm").onsubmit = async (event) => {
  event.preventDefault();
  try {
    const kind = $("insertKind").value;
    const insertion = buildInsertion(
      kind,
      $("insertTitle").value.trim(),
      $("insertTarget").value.trim(),
      $("insertContent").value.trim(),
    );
    if (state.insertionMode === "child") {
      let parent = $("elementValue").value.trim();
      const opener = parent.match(/^(:{3,})(\{[^\n]+\})/);
      const closer = parent.match(/\n(:{3,})\s*$/);
      if (!closer) throw new Error("The selected admonition has no closing fence.");
      if (opener && opener[1].length < 4) {
        const expanded = ":".repeat(4);
        parent = expanded + parent.slice(opener[1].length);
        parent = parent.replace(/\n:{3}\s*$/, `\n${expanded}`);
      }
      const closing = parent.match(/\n(:{3,})\s*$/);
      const value = parent.slice(0, closing.index) + `\n\n${insertion}\n` + closing[0];
      $("insertDialog").close();
      await saveSingleVisual({ ...state.selection, value });
      return;
    }
    const inline = [
      "link",
      "citation",
      "reference",
      "proof_reference",
    ].includes(kind);
    const source = $("sourceEditor");
    const position = state.insertionPosition ?? source.value.length;
    const prefix = inline || position === 0 || source.value.slice(0, position).endsWith("\n\n")
      ? ""
      : "\n\n";
    const suffix = inline || source.value.slice(position).startsWith("\n\n")
      ? ""
      : "\n\n";
    const text = `${prefix}${insertion}${suffix}`;
    source.setRangeText(text, position, position, "end");
    source.closest("details").open = true;
    source.focus();
    state.sourceDirty = true;
    setStatus("Unsaved MyST source changes");
    $("insertDialog").close();
    toast('Structure inserted. Select "Save MyST source" to save it.');
  } catch (error) {
    toast(error.message);
  }
};

$("newPageButton").onclick = () => $("newPageDialog").showModal();
$("moveUpButton").onclick = () =>
  managePage("/api/pages/move", { path: state.page.path, direction: "up" }, state.page.path);
$("moveDownButton").onclick = () =>
  managePage("/api/pages/move", { path: state.page.path, direction: "down" }, state.page.path);
$("deletePageButton").onclick = () => {
  if (!state.page || state.page.protected) return;
  if (!confirm(`Delete "${state.page.title}"? A backup will be retained.`)) return;
  managePage("/api/pages/delete", { path: state.page.path }, "index.md");
};
$("saveSourceButton").onclick = saveSource;
$("buildButton").onclick = () => rebuild(false);
$("reloadButton").onclick = () => state.page && openPage(state.page);
$("pageSearch").oninput = (event) => renderPages(event.target.value);
$("sourceEditor").oninput = () => {
  state.sourceDirty = true;
  setStatus("Unsaved MyST source changes");
};
$("saveAndRebuildButton").onclick = async () => {
  $("rebuildDialog").close();
  await saveSource();
};
$("discardAndRebuildButton").onclick = async () => {
  $("rebuildDialog").close();
  await rebuild(true);
};
document.querySelectorAll("[data-close]").forEach((button) => {
  button.onclick = () => $(button.dataset.close).close();
});

window.addEventListener("message", (event) => {
  if (event.origin !== location.origin || event.source !== $("preview").contentWindow)
    return;
  if (event.data?.type === "pytexmd-select") selectElement(event.data);
  if (event.data?.type === "pytexmd-commit") {
    const source = currentSourceElement(event.data.kind, event.data.index);
    if (!source) {
      toast("This generated element is not independently editable. Select its parent block.");
      return;
    }
    saveSingleVisual({
      kind: event.data.kind,
      index: event.data.index,
      value: event.data.value,
    });
  }
  if (event.data?.type === "pytexmd-ready") {
    setStatus("Click page content to edit; changes save immediately");
  }
});

loadProject().catch((error) => toast(error.message));
