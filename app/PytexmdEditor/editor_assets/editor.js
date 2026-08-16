const state = {
  pages: [],
  page: null,
  elements: [],
  selection: null,
  pageLoadSequence: 0,
  previewPath: null,
  inspectorTab: "general",
  draggedPage: null,
  pageClipboard: null,
  contextPage: null,
  pendingEdits: new Map(),
  inspectorChanged: false,
  buildDirty: false,
  saveInProgress: false,
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

function pendingEditCount() {
  return [...state.pendingEdits.values()].reduce(
    (count, edits) => count + edits.size,
    0,
  );
}

function updatePendingStatus() {
  const count = pendingEditCount();
  const needsBuild = state.buildDirty || count > 0 || state.inspectorChanged;
  $("saveButton").textContent = count ? `Save (${count})` : "Save";
  $("buildButton").textContent = needsBuild ? "Rebuild *" : "Rebuild";
  $("buildButton").classList.toggle("dirty", needsBuild);
  $("buildButton").title = needsBuild
    ? "Changes have not been rebuilt"
    : "Rebuild the Sphinx project";
  if (count || state.inspectorChanged) {
    setStatus(`${count + (state.inspectorChanged ? 1 : 0)} unsaved change(s)`);
  } else if (state.buildDirty) {
    setStatus("Saved changes pending rebuild");
  }
}

function setInspectorChanged(value) {
  state.inspectorChanged = value;
  updatePendingStatus();
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

function comparableText(value) {
  return String(value || "")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/\{[^}]+\}`([^`]+)`/g, "$1")
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

function textSimilarity(first, second) {
  const firstWords = comparableText(first).split(" ").filter(Boolean);
  const secondWords = comparableText(second).split(" ").filter(Boolean);
  if (!firstWords.length || !secondWords.length) return 0;
  const remaining = new Map();
  firstWords.forEach((word) => remaining.set(word, (remaining.get(word) || 0) + 1));
  let matches = 0;
  secondWords.forEach((word) => {
    const count = remaining.get(word) || 0;
    if (!count) return;
    remaining.set(word, count - 1);
    matches += 1;
  });
  return (2 * matches) / (firstWords.length + secondWords.length);
}

function sourceDisplayText(source) {
  if (source.kind === "list" && source.metadata?.items) {
    return source.metadata.items
      .map((item) => `${item.label || ""} ${item.content || ""}`)
      .join(" ");
  }
  return source.value;
}

function resolveSourceElement(message) {
  const candidates = state.elements.filter((item) => item.kind === message.kind);
  const nestedSibling = candidates.find(
    (item) =>
      message.parentAdmonitionIndex !== null &&
      item.metadata?.nesting?.parent === message.parentAdmonitionIndex &&
      item.metadata?.nesting?.sibling === message.siblingIndex,
  );
  const rendered = comparableText(message.value);
  const matchesByText = [
    "heading",
    "paragraph",
    "directive_title",
    "rubric",
    "equation",
    "list",
  ].includes(message.kind);
  if (matchesByText) {
    const textMatches = candidates.filter(
      (item) => {
        const sourceText = comparableText(sourceDisplayText(item));
        return (
          sourceText === rendered ||
          (message.kind === "list" && sourceText.includes(rendered))
        );
      },
    );
    if (textMatches.length === 1) return textMatches[0];
    const nestedMatches = textMatches.filter(
      (item) => item.metadata?.nesting?.parent === message.parentAdmonitionIndex,
    );
    if (nestedMatches.length === 1) return nestedMatches[0];
    if (message.kind === "paragraph") {
      const sameParent = candidates.filter(
        (item) => item.metadata?.nesting?.parent === message.parentAdmonitionIndex,
      );
      const ranked = (sameParent.length ? sameParent : candidates)
        .map((item) => ({
          item,
          score: textSimilarity(sourceDisplayText(item), message.value),
        }))
        .sort((first, second) => second.score - first.score);
      if (
        ranked[0]?.score >= 0.72 &&
        ranked[0].score - (ranked[1]?.score || 0) >= 0.08
      ) return ranked[0].item;
    }
  }
  if (message.kind === "admonition" && message.admonitionTitle) {
    const titleMatches = candidates.filter(
      (item) => comparableText(item.metadata?.title) === comparableText(message.admonitionTitle),
    );
    if (titleMatches.length === 1) return titleMatches[0];
    const nestedTitleMatches = titleMatches.filter(
      (item) => item.metadata?.nesting?.parent === message.parentAdmonitionIndex,
    );
    if (nestedTitleMatches.length === 1) return nestedTitleMatches[0];
  }
  if (nestedSibling) return nestedSibling;
  const nestedCandidates = candidates.filter(
    (item) => item.metadata?.nesting?.parent === message.parentAdmonitionIndex,
  );
  if (matchesByText) {
    return nestedCandidates.length === 1 ? nestedCandidates[0] : undefined;
  }
  const indexed = currentSourceElement(message.kind, message.index);
  if (indexed && (!nestedCandidates.length || nestedCandidates.includes(indexed))) {
    return indexed;
  }
  return nestedCandidates[0] || indexed;
}

function updatePageActions() {
  return;
}

function hidePageContextMenu() {
  $("pageContextMenu").classList.add("hidden");
  state.contextPage = null;
}

function showPageContextMenu(page, x, y) {
  state.contextPage = page;
  const menu = $("pageContextMenu");
  const clipboardReady = Boolean(state.pageClipboard && page.parent);
  menu.querySelector('[data-page-action="copy"]').disabled = !page.parent;
  menu.querySelector('[data-page-action="cut"]').disabled =
    page.protected || !page.parent;
  menu.querySelector('[data-page-action="delete"]').disabled = page.protected;
  for (const action of ["paste-above", "paste-below"]) {
    menu.querySelector(`[data-page-action="${action}"]`).disabled =
      !clipboardReady ||
      (state.pageClipboard?.mode === "cut" && state.pageClipboard.path === page.path);
  }
  menu.classList.remove("hidden");
  const bounds = menu.getBoundingClientRect();
  menu.style.left = `${Math.min(x, window.innerWidth - bounds.width - 8)}px`;
  menu.style.top = `${Math.min(y, window.innerHeight - bounds.height - 8)}px`;
}

async function handlePageContextAction(action) {
  const page = state.contextPage;
  hidePageContextMenu();
  if (!page) return;
  if (action === "copy" || action === "cut") {
    state.pageClipboard = { mode: action, path: page.path, title: page.title };
    toast(`${action === "copy" ? "Copied" : "Cut"} ${page.title}.`);
    return;
  }
  if (action === "delete") {
    if (!confirm(`Delete "${page.title}"? A backup will be retained.`)) return;
    await managePage("/api/pages/delete", { path: page.path }, "index.md");
    return;
  }
  if (action.startsWith("paste-") && state.pageClipboard) {
    const clipboard = state.pageClipboard;
    const result = await managePage("/api/pages/paste", {
      source: clipboard.path,
      target: page.path,
      position: action.removeprefix("paste-"),
      mode: clipboard.mode,
    });
    if (result && clipboard.mode === "cut") state.pageClipboard = null;
  }
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
      button.oncontextmenu = (event) => {
        event.preventDefault();
        showPageContextMenu(page, event.clientX, event.clientY);
      };
      button.draggable = Boolean(page.parent && !page.protected);
      button.ondragstart = (event) => {
        state.draggedPage = page;
        button.classList.add("dragging");
        event.dataTransfer.effectAllowed = "move";
      };
      button.ondragend = () => {
        state.draggedPage = null;
        button.classList.remove("dragging");
        document.querySelectorAll(".drop-target").forEach((item) =>
          item.classList.remove("drop-target"),
        );
      };
      button.ondragover = (event) => {
        if (!state.draggedPage || state.draggedPage.parent !== page.parent) return;
        event.preventDefault();
        button.classList.add("drop-target");
      };
      button.ondragleave = () => button.classList.remove("drop-target");
      button.ondrop = (event) => {
        event.preventDefault();
        button.classList.remove("drop-target");
        const dragged = state.draggedPage;
        if (!dragged || dragged.path === page.path || dragged.parent !== page.parent) return;
        managePage(
          "/api/pages/reorder",
          { path: dragged.path, target: page.path },
          dragged.path,
        );
      };
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

async function openPage(page, navigatePreview = true) {
  if (state.inspectorChanged && !stageInspectorChange()) return;
  const loadSequence = ++state.pageLoadSequence;
  state.previewPath = null;
  state.selection = null;
  state.elements = [];
  let data = await request(`/api/page?path=${encodeURIComponent(page.path)}`);
  const pending = state.pendingEdits.get(page.path);
  if (pending?.size) {
    data = await post("/api/visual-preview", {
      path: page.path,
      changes: [...pending.values()].map((entry) => entry.change),
    });
  }
  if (loadSequence !== state.pageLoadSequence) return;
  state.page = page;
  state.elements = data.elements;
  $("pageTitle").textContent = page.title;
  state.previewPath = page.preview;
  if (navigatePreview) $("preview").src = `${page.preview}?v=${Date.now()}`;
  selectElement({ kind: "page", index: 0, value: data.markdown });
  renderPages($("pageSearch").value);
}

function escapeHtml(value) {
  return value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function highlightMyst(value) {
  return value.split("\n").map((line) => {
    let escaped = escapeHtml(line);
    if (/^\s*<!--/.test(line)) return `<span class="syn-comment">${escaped}</span>`;
    if (/^\s*#{1,6}\s/.test(line)) return `<span class="syn-heading">${escaped}</span>`;
    if (/^\s*[:`]{3,}\{/.test(line)) return `<span class="syn-directive">${escaped}</span>`;
    if (/^\s*:[\w-]+:/.test(line)) return `<span class="syn-option">${escaped}</span>`;
    escaped = escaped.replace(/(\{[\w:-]+\}`[^`]+`)/g, '<span class="syn-role">$1</span>');
    escaped = escaped.replace(/(\$[^$]+\$)/g, '<span class="syn-math">$1</span>');
    return escaped;
  }).join("\n");
}

function updateRawHighlight() {
  $("rawHighlight").innerHTML = highlightMyst($("elementValue").value);
}

function syncRawSource() {
  $("elementValue").value = $("rawHighlight").innerText.replace(/\r/g, "");
}

function setInspectorTab(tab) {
  state.inspectorTab = tab;
  $("generalTab").classList.toggle("hidden", tab !== "general");
  $("rawTab").classList.toggle("hidden", tab !== "raw");
  $("generalTabButton").classList.toggle("active", tab === "general");
  $("rawTabButton").classList.toggle("active", tab === "raw");
  if (tab === "raw") updateRawHighlight();
}

function parseEquation(value) {
  const match = value.match(/\\tag\{([^}]*)\}/);
  return {
    content: value.replace(/\s*\\tag\{[^}]*\}\s*/, "\n").trim(),
    number: match?.[1] || "",
  };
}

function selectElement(message) {
  const activeSource =
    message.dirty && state.selection?.kind === message.kind
      ? currentSourceElement(state.selection.kind, state.selection.index)
      : null;
  const source = activeSource || resolveSourceElement(message);
  if (!source) {
    state.selection = null;
    setInspectorChanged(false);
    $("elementType").value = "";
    $("elementValue").value = "";
    updateRawHighlight();
    $("inspectorForm").classList.add("hidden");
    $("emptyInspector").classList.remove("hidden");
    $("emptyInspector").innerHTML =
      "<strong>Generated Sphinx element</strong><span>This rendered element has no independent Markdown source block. Select its containing admonition or the page background.</span>";
    return;
  }
  state.selection = { kind: source.kind, index: source.index };
  $("emptyInspector").classList.add("hidden");
  $("emptyInspector").innerHTML = emptyInspectorDefault;
  $("inspectorForm").classList.remove("hidden");
  $("elementType").value = source.kind.replace("_", " ");
  const displayedValue = message.dirty ? message.value : source.value;
  $("elementValue").value =
    source.kind === "heading"
      ? `${source.metadata?.prefix || ""}${displayedValue}`
      : displayedValue;
  updateRawHighlight();

  const kind = source.kind;
  const structuredList = kind === "list" && source.metadata?.style !== "raw";
  const generalText = [
    "heading",
    "paragraph",
    "directive_title",
    "rubric",
  ].includes(kind);
  $("generalValueLabel").classList.toggle("hidden", !generalText);
  if (generalText) {
    $("generalValue").value = displayedValue;
    $("generalValueLabel").firstChild.textContent =
      kind === "paragraph"
          ? "Content "
          : "Title ";
  }
  $("admonitionEditor").classList.toggle("hidden", kind !== "admonition");
  if (kind === "admonition") {
    $("admonitionTitle").value =
      message.admonitionTitle ?? source.metadata?.title ?? "";
    $("admonitionColor").value = source.metadata?.color || "";
  }
  $("equationEditor").classList.toggle("hidden", kind !== "equation");
  if (kind === "equation") {
    const equation = parseEquation(source.value);
    $("equationValue").value = equation.content;
    $("equationNumber").value = equation.number;
  }
  $("tikzEditor").classList.toggle("hidden", kind !== "tikz");
  if (kind === "tikz") {
    $("tikzContent").value = source.metadata?.content || "";
    $("tikzScale").value = source.metadata?.scale || "1";
  }
  $("listEditor").classList.toggle("hidden", !structuredList);
  if (structuredList) renderListEditor(source.metadata);
  $("childTools").classList.toggle("hidden", kind !== "admonition");
  const hasGeneral =
    generalText ||
    kind === "admonition" ||
    kind === "equation" ||
    kind === "tikz" ||
    structuredList;
  $("generalUnavailable").classList.toggle("hidden", hasGeneral);

  const nesting = source.metadata?.nesting;
  const hasParent = kind !== "page";
  $("nestingContext").classList.toggle("hidden", !hasParent);
  if (hasParent) {
    const parentIndex = nesting?.parent;
    $("selectParentButton").dataset.parentKind =
      parentIndex === null || parentIndex === undefined ? "page" : "admonition";
    $("selectParentButton").dataset.parentIndex = parentIndex ?? 0;
    $("nestingLabel").textContent =
      parentIndex === null || parentIndex === undefined
        ? "Parent: whole page"
        : `Nested level ${nesting.depth}`;
  }
  const defaultTab = hasGeneral ? "general" : "raw";
  setInspectorTab(defaultTab);
  const help = {
    page: "Edit the complete page as MyST, then use Save, Rebuild, or Ctrl+S.",
    paragraph: "Edit paragraph content in General, or use Raw MyST for exact markup.",
    directive_title: "Edit here or type directly in the preview, then save from the toolbar.",
    rubric: "Edit the rubric title here or directly in the preview.",
    equation: "Set an optional displayed number using MathJax \\tag{...} functionality.",
    tikz: "Edit the TikZ source and rendered image scale, then save or rebuild.",
    admonition: "Edit the custom title and theme color, or use Raw for the complete block.",
    list: "Edit structured list items here or use Raw for exact MyST.",
  };
  $("fieldHelp").textContent = help[kind] || "Raw contains the exact selected MyST source.";
  setInspectorChanged(false);
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
  row.dataset.target = item.target || "";
  if (custom) {
    const label = document.createElement("input");
    label.className = "item-label";
    label.placeholder = "Item label";
    label.value = item.label;
    row.append(label);
  }
  const content = document.createElement(custom ? "textarea" : "input");
  content.className = "item-content";
  content.placeholder = "Item content";
  content.value = item.content;
  if (custom) content.rows = 2;
  row.append(content);
  const remove = document.createElement("button");
  remove.className = "remove-item";
  remove.type = "button";
  remove.title = "Remove item";
  remove.textContent = "x";
  remove.onclick = () => {
    row.remove();
    setInspectorChanged(true);
    stageInspectorChange();
  };
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
      const target = row.dataset.target ? `${row.dataset.target}\n` : "";
      const definition = content.replace(/\n/g, "\n   ");
      if (state.currentListStyle === "enumeration") {
        return `${target}${index + 1}.\n: ${definition}`;
      }
      const label = row.querySelector(".item-label").value.trim();
      if (!label) throw new Error(`Custom item ${index + 1} needs a label.`);
      return `${target}${label}\n: ${definition}`;
    })
    .join("\n");
}

function sourceAncestors(source) {
  const ancestors = [];
  let parent = source?.metadata?.nesting?.parent;
  while (parent !== null && parent !== undefined && !ancestors.includes(parent)) {
    ancestors.push(parent);
    parent = currentSourceElement("admonition", parent)?.metadata?.nesting?.parent;
  }
  return ancestors;
}

function editsOverlap(first, second) {
  if (first.change.kind === "page" || second.change.kind === "page") return true;
  if (
    first.change.kind === second.change.kind &&
    first.change.index === second.change.index
  ) return true;
  const firstContainsSecond =
    first.change.kind === "admonition" &&
    second.ancestors.includes(first.change.index);
  const secondContainsFirst =
    second.change.kind === "admonition" &&
    first.ancestors.includes(second.change.index);
  const firstIsStructured =
    "admonition_title" in first.change || "admonition_color" in first.change;
  const secondIsStructured =
    "admonition_title" in second.change || "admonition_color" in second.change;
  return (
    (firstContainsSecond && !firstIsStructured) ||
    (secondContainsFirst && !secondIsStructured)
  );
}

function stageVisualChange(change) {
  const pagePath = state.page?.path;
  if (!pagePath) return false;
  const source = currentSourceElement(change.kind, change.index);
  const entry = { change, ancestors: sourceAncestors(source) };
  const edits = state.pendingEdits.get(pagePath) || new Map();
  for (const [key, pending] of edits) {
    if (editsOverlap(entry, pending)) edits.delete(key);
  }
  edits.set(`${change.kind}:${change.index}`, entry);
  state.pendingEdits.set(pagePath, edits);
  updatePendingStatus();
  return true;
}

async function refreshDraftElements() {
  const pagePath = state.page?.path;
  const pending = pagePath ? state.pendingEdits.get(pagePath) : null;
  if (!pagePath || !pending?.size) return;
  const data = await post("/api/visual-preview", {
    path: pagePath,
    changes: [...pending.values()].map((entry) => entry.change),
  });
  if (state.page?.path !== pagePath) return;
  state.elements = data.elements;
}

async function refreshCurrentSource() {
  const pagePath = state.page?.path;
  if (!pagePath) return;
  const selection = state.selection ? { ...state.selection } : null;
  const data = await request(`/api/page?path=${encodeURIComponent(pagePath)}`);
  if (state.page?.path !== pagePath) return;
  state.elements = data.elements;
  if (!selection) return;
  const source = currentSourceElement(selection.kind, selection.index);
  if (source) {
    selectElement({
      kind: source.kind,
      index: source.index,
      value: source.value,
      parentAdmonitionIndex: source.metadata?.nesting?.parent ?? null,
      siblingIndex: source.metadata?.nesting?.sibling ?? 0,
      admonitionTitle: source.metadata?.title || null,
    });
  }
}

async function persistPending(rebuildAfter = false) {
  if (state.saveInProgress) return false;
  if (state.inspectorChanged && !stageInspectorChange()) return false;
  const pages = [...state.pendingEdits].map(([path, edits]) => ({
    path,
    changes: [...edits.values()].map((entry) => entry.change),
  }));
  if (!pages.length && !rebuildAfter) {
    toast("No unsaved changes.");
    return true;
  }
  state.saveInProgress = true;
  setBusy(true);
  setStatus(rebuildAfter ? "Saving changes and rebuilding..." : "Saving changes...");
  try {
    const result = pages.length
      ? await post("/api/visual-save-batch", { pages, rebuild: rebuildAfter })
      : await post("/api/build");
    state.pendingEdits.clear();
    state.buildDirty = rebuildAfter ? false : state.buildDirty || pages.length > 0;
    setInspectorChanged(false);
    $("preview").contentWindow?.postMessage(
      { type: "pytexmd-mark-saved" },
      location.origin,
    );
    showLog(result.log);
    if (rebuildAfter) {
      if (state.page) await loadProject(state.page.path);
      toast("Changes saved and build complete.");
    } else {
      await refreshCurrentSource();
      toast(pages.length ? "All changes saved." : "No unsaved changes.");
    }
    return true;
  } catch (error) {
    toast(error.message);
    setStatus(rebuildAfter ? "Build failed" : "Save failed");
    return false;
  } finally {
    state.saveInProgress = false;
    setBusy(false);
    updatePendingStatus();
  }
}

async function deleteBuild() {
  if (!confirm("Delete the generated Sphinx build folder? Source files are not affected.")) {
    return;
  }
  setBusy(true);
  setStatus("Deleting Sphinx build...");
  try {
    const result = await post("/api/build/delete");
    state.pages = result.pages;
    state.buildDirty = true;
    renderPages($("pageSearch").value);
    showLog(result.log);
    updatePendingStatus();
    setStatus("Sphinx build deleted; rebuild required");
    toast(result.log);
  } catch (error) {
    toast(error.message);
    setStatus("Could not delete Sphinx build");
  } finally {
    setBusy(false);
  }
}

async function rebuild() {
  await persistPending(true);
}

async function managePage(url, body, selectedPath) {
  if (
    (state.inspectorChanged || pendingEditCount()) &&
    !(await persistPending(false))
  ) return null;
  setBusy(true);
  setStatus("Updating navigation and rebuilding...");
  try {
    const result = await post(url, body);
    showLog(result.log);
    await loadProject(selectedPath || result.page);
    state.buildDirty = false;
    updatePendingStatus();
    toast("Page navigation updated.");
    return result;
  } catch (error) {
    toast(error.message);
    setStatus("Page update failed");
    return null;
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
    help: "Creates an editable MyST paragraph admonition.",
  },
  proof: {
    title: "Optional proof title",
    target: "Optional proof label",
    content: "Proof content",
    help: "Creates a semantic MyST proof admonition.",
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
    help: "Creates a standard MyST {ref} role.",
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

function requiredFenceLength(content) {
  const innerFences = [...content.matchAll(/^(:{3,})(?:\{|\s*$)/gm)]
    .map((match) => match[1].length);
  return Math.max(3, ...innerFences.map((length) => length + 1));
}

function directive(name, title, target, content, options = []) {
  const optionLines = [...options];
  if (target) optionLines.push(`:label: ${target}`);
  const optionBlock = optionLines.length ? `${optionLines.join("\n")}\n\n` : "";
  const fence = ":".repeat(requiredFenceLength(content));
  return `${fence}{${name}}${title ? ` ${title}` : ""}\n${optionBlock}${content}\n${fence}`;
}

function customAdmonition(title, cssClass, target, content) {
  const options = [`:class: pytexmd-admonition ${cssClass}`];
  if (target) options.push(`:name: ${target}`);
  return directive("admonition", title, "", content, options);
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
      return customAdmonition(`Paragraph ${title}`, "paragraph", target, content);
    case "proof":
      return customAdmonition(`Proof${title ? ` ${title}` : ""}`, "proof", target, content);
    case "theorem":
      return customAdmonition(`Theorem ${title}`, "theorem", target, content);
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
      return `{ref}\`${target}\``;
    case "label":
      return `(${target})=`;
    default:
      throw new Error("Unsupported insertion type.");
  }
}

function buildInspectorChange() {
  const kind = state.selection.kind;
  if (state.inspectorTab === "raw") syncRawSource();
  let value = $("elementValue").value;
  if (state.inspectorTab === "general") {
    if (["heading", "paragraph", "directive_title", "rubric"].includes(kind)) {
      value = $("generalValue").value;
    } else if (kind === "list" && !$("listEditor").classList.contains("hidden")) {
      value = serializeListEditor();
    } else if (kind === "equation") {
      const number = $("equationNumber").value.trim();
      value = $("equationValue").value.trim();
      if (number) value += `\n\\tag{${number}}`;
    }
  }
  const change = { ...state.selection, value };
  if (kind === "heading" && state.inspectorTab === "raw") {
    change.raw_source = true;
  }
  if (kind === "admonition" && state.inspectorTab === "general") {
    change.admonition_title = $("admonitionTitle").value;
    change.admonition_color = $("admonitionColor").value;
  }
  if (kind === "tikz" && state.inspectorTab === "general") {
    change.tikz_content = $("tikzContent").value;
    change.tikz_scale = $("tikzScale").value;
  }
  return change;
}

function stageInspectorChange(refreshRaw = true) {
  if (!state.selection) return false;
  try {
    const change = buildInspectorChange();
    stageVisualChange(change);
    const source = currentSourceElement(change.kind, change.index);
    $("elementValue").value =
      change.kind === "heading" && !change.raw_source
        ? `${source?.metadata?.prefix || ""}${change.value}`
        : change.value;
    if (refreshRaw) updateRawHighlight();
    setInspectorChanged(false);
    return true;
  } catch (error) {
    toast(error.message);
    return false;
  }
}

$("inspectorForm").onsubmit = (event) => {
  event.preventDefault();
};
$("inspectorForm").addEventListener("input", () => setInspectorChanged(true));
$("inspectorForm").addEventListener("change", () => stageInspectorChange());

$("addListItemButton").onclick = () => {
  addListItemRow();
  setInspectorChanged(true);
};
$("generalTabButton").onclick = () => {
  if (!state.inspectorChanged || stageInspectorChange()) setInspectorTab("general");
};
$("rawTabButton").onclick = () => {
  if (!state.inspectorChanged || stageInspectorChange()) setInspectorTab("raw");
};
$("rawHighlight").oninput = (event) => {
  event.stopPropagation();
  syncRawSource();
  setInspectorChanged(true);
  stageInspectorChange(false);
};
$("selectParentButton").onclick = () => {
  const kind = $("selectParentButton").dataset.parentKind;
  const index = Number($("selectParentButton").dataset.parentIndex);
  $("preview").contentWindow?.postMessage(
    { type: "pytexmd-select-element", kind, index },
    location.origin,
  );
};

$("newPageForm").onsubmit = async (event) => {
  event.preventDefault();
  $("newPageDialog").close();
  await managePage("/api/pages/create", {
    title: $("newPageTitle").value,
    slug: $("newPageSlug").value,
  });
  event.target.reset();
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
      if (!opener || !closer) {
        throw new Error("Nested insertion requires a colon-fenced admonition.");
      }
      const requiredLength = requiredFenceLength(insertion);
      if (opener[1].length < requiredLength) {
        const expanded = ":".repeat(requiredLength);
        parent = expanded + parent.slice(opener[1].length);
        parent = parent.replace(/\n:{3,}\s*$/, `\n${expanded}`);
      }
      const closing = parent.match(/\n(:{3,})\s*$/);
      const value = parent.slice(0, closing.index) + `\n\n${insertion}\n` + closing[0];
      $("insertDialog").close();
      const change = { ...state.selection, value };
      selectElement({ ...change, dirty: true });
      stageVisualChange(change);
      toast("Child element staged. Use Save or Rebuild to write it.");
      return;
    }
    throw new Error("Structures can only be inserted into a selected admonition.");
  } catch (error) {
    toast(error.message);
  }
};

$("newPageButton").onclick = () => $("newPageDialog").showModal();
$("saveButton").onclick = () => persistPending(false);
$("buildButton").onclick = rebuild;
$("deleteBuildButton").onclick = deleteBuild;
$("pageSearch").oninput = (event) => renderPages(event.target.value);
$("pageContextMenu").querySelectorAll("[data-page-action]").forEach((button) => {
  button.onclick = () => handlePageContextAction(button.dataset.pageAction);
});
document.addEventListener("pointerdown", (event) => {
  if (!event.target.closest("#pageContextMenu")) hidePageContextMenu();
});
document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s") {
    event.preventDefault();
    persistPending(false);
    return;
  }
  if (event.key === "Escape") hidePageContextMenu();
});
document.querySelectorAll("[data-close]").forEach((button) => {
  button.onclick = () => $(button.dataset.close).close();
});

window.addEventListener("message", async (event) => {
  if (event.origin !== location.origin || event.source !== $("preview").contentWindow)
    return;
  if (
    event.data?.type === "pytexmd-ready" &&
    event.data.previewPath !== state.previewPath
  ) {
    const previewPage = state.pages.find(
      (page) => page.preview === event.data.previewPath,
    );
    if (!previewPage) return;
    await openPage(previewPage, false);
  }
  if (event.data?.previewPath !== state.previewPath) return;
  if (event.data?.type === "pytexmd-select") {
    if (state.inspectorChanged && !stageInspectorChange()) return;
    if (!event.data.dirty) await refreshDraftElements();
    selectElement(event.data);
    if (event.data.dirty && state.selection) {
      stageVisualChange({
        ...state.selection,
        value: event.data.value,
      });
    }
  }
  if (event.data?.type === "pytexmd-save-request") persistPending(false);
  if (event.data?.type === "pytexmd-commit") {
    const source =
      state.selection?.kind === event.data.kind
        ? currentSourceElement(state.selection.kind, state.selection.index)
        : resolveSourceElement(event.data);
    if (!source) {
      toast("This generated element is not independently editable. Select its parent block.");
      return;
    }
    stageVisualChange({
      kind: source.kind,
      index: source.index,
      value: event.data.value,
    });
  }
  if (event.data?.type === "pytexmd-ready") {
    setStatus("Edit content, then use Save, Rebuild, or Ctrl+S");
  }
});

loadProject().catch((error) => toast(error.message));
