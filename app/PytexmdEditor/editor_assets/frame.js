(() => {
  const root = document.querySelector(
    '.article-container article,main article,[role="main"]',
  );
  if (!root) return;

  const counts = {
    heading: 0,
    paragraph: 0,
    directive_title: 0,
    rubric: 0,
    equation: 0,
    tikz: 0,
    admonition: 0,
    list: 0,
    page: 0,
  };

  const clean = (node) => {
    const clone = node.cloneNode(true);
    clone.querySelectorAll('.headerlink').forEach((link) => link.remove());
    return clone.textContent.trim();
  };
  const value = (node) => clean(node);
  const parentAdmonitionIndex = (node) => {
    const parentBlock = node.parentElement?.closest(
      '[data-pytexmd-kind="admonition"]',
    );
    return parentBlock ? Number(parentBlock.dataset.pytexmdIndex) : null;
  };
  const siblingIndex = (node) => {
    const kind = node.dataset.pytexmdKind;
    const parentIndex = parentAdmonitionIndex(node);
    return [...root.querySelectorAll(`[data-pytexmd-kind="${kind}"]`)]
      .filter((item) => parentAdmonitionIndex(item) === parentIndex)
      .indexOf(node);
  };
  const admonitionTitle = (node) => {
    if (node.dataset.pytexmdKind !== 'admonition') return null;
    const title = [...node.children].find((child) =>
      child.classList.contains('admonition-title'),
    );
    return title ? clean(title) : null;
  };
  const send = (node, dirty = false) =>
    parent.postMessage(
      {
        type: 'pytexmd-select',
        previewPath: location.pathname,
        kind: node.dataset.pytexmdKind,
        index: Number(node.dataset.pytexmdIndex),
        value: value(node),
        parentAdmonitionIndex: parentAdmonitionIndex(node),
        siblingIndex: siblingIndex(node),
        admonitionTitle: admonitionTitle(node),
        dirty,
      },
      location.origin,
    );
  const select = (node) => {
    [root, ...root.querySelectorAll('[data-pytexmd-kind]')]
      .forEach((item) => (item.style.outline = ''));
    node.style.outline = '2px solid #c65232';
    send(node);
  };
  const register = (node, kind, editable = false) => {
    node.dataset.pytexmdKind = kind;
    node.dataset.pytexmdIndex = counts[kind]++;
    if (editable) {
      node.contentEditable = 'true';
      node.spellcheck = true;
      node.dataset.pytexmdChanged = 'false';
      node.addEventListener('pointerdown', () => select(node));
    }
    node.style.outlineOffset = '4px';
    node.addEventListener('focus', () => select(node));
    node.addEventListener('click', (event) => {
      event.stopPropagation();
      select(node);
    });
    if (editable) {
      node.addEventListener('input', () => {
        node.dataset.pytexmdChanged = 'true';
        send(node, true);
      });
      node.addEventListener('blur', () => {
        if (node.dataset.pytexmdChanged !== 'true') return;
        node.dataset.pytexmdChanged = 'false';
        parent.postMessage(
          {
            type: 'pytexmd-commit',
            previewPath: location.pathname,
            kind: node.dataset.pytexmdKind,
            index: Number(node.dataset.pytexmdIndex),
            value: value(node),
            parentAdmonitionIndex: parentAdmonitionIndex(node),
            siblingIndex: siblingIndex(node),
            admonitionTitle: admonitionTitle(node),
          },
          location.origin,
        );
      });
    }
  };

  root
    .querySelectorAll('h1,h2,h3,h4,h5,h6')
    .forEach((node) => register(node, 'heading', true));
  root.querySelectorAll('p').forEach((node) => {
    if (
      node.closest(
        'nav,.sidebar,.math,.admonition-title,li,dd,dt,blockquote,figure,table,.topic',
      ) || node.classList.contains('admonition-title') || node.classList.contains('rubric')
    )
      return;
    register(node, 'paragraph', true);
  });
  [...root.querySelectorAll('.pytexmd-admonition > .admonition-title')]
    .forEach((node) => register(node, 'directive_title', true));
  root.querySelectorAll('.rubric').forEach((node) => register(node, 'rubric', true));
  root.querySelectorAll('div.math').forEach((node) => register(node, 'equation'));
  root.querySelectorAll('img,.tikz-fallback').forEach((node) => {
    if (
      !node.classList.contains('tikz-fallback') &&
      !/tikz-/i.test(node.getAttribute('src') || '')
    ) return;
    register(node, 'tikz');
  });
  [...new Set(root.querySelectorAll('.proof,.admonition'))]
    .filter((node) => !node.classList.contains('tikz-fallback'))
    .forEach((node) => {
      register(node, 'admonition');
      node.classList.add('pytexmd-editable-admonition');
      node.addEventListener(
        'click',
        (event) => {
          const nearestBlock = event.target.closest(
            '[data-pytexmd-kind="admonition"]',
          );
          const nearestEditable = event.target.closest('[data-pytexmd-kind]');
          if (
            nearestBlock !== node ||
            nearestEditable !== node ||
            event.target.closest('.admonition-title')
          )
            return;
          event.preventDefault();
          event.stopPropagation();
          select(node);
        },
        true,
      );
    });
  root.querySelectorAll('ul,ol,dl').forEach((node) => {
    if (
      node.closest('nav,.sidebar') ||
      node.parentElement?.closest('ul,ol,dl') ||
      node.classList.contains('field-list') ||
      node.classList.contains('citation-list')
    )
      return;
    register(node, 'list');
  });
  register(root, 'page');

  window.addEventListener('message', (event) => {
    if (event.origin !== location.origin) return;
    if (event.data?.type === 'pytexmd-mark-saved') {
      root.querySelectorAll('[data-pytexmd-changed]').forEach((node) => {
        node.dataset.pytexmdChanged = 'false';
      });
      return;
    }
    if (event.data?.type === 'pytexmd-select-element') {
      const selector =
        `[data-pytexmd-kind="${event.data.kind}"]` +
        `[data-pytexmd-index="${event.data.index}"]`;
      const selected = root.matches(selector)
        ? root
        : root.querySelector(selector);
      if (selected) select(selected);
      return;
    }
    if (event.data?.type !== 'pytexmd-update') return;
    const node = root.querySelector(
      `[data-pytexmd-kind="${event.data.kind}"][data-pytexmd-index="${event.data.index}"]`,
    );
    if (!node) return;
    if (event.data.kind === 'admonition' || event.data.kind === 'list') {
      node.innerHTML = `<pre style="white-space:pre-wrap"></pre>`;
      node.querySelector('pre').textContent = event.data.value;
    } else {
      node.textContent = event.data.value;
    }
    select(node);
  });

  window.addEventListener('keydown', (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 's') {
      event.preventDefault();
      parent.postMessage(
        { type: 'pytexmd-save-request', previewPath: location.pathname },
        location.origin,
      );
    }
  });

  parent.postMessage(
    { type: 'pytexmd-ready', previewPath: location.pathname },
    location.origin,
  );
})();
