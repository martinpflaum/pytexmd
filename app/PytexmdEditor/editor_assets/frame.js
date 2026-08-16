(() => {
  const root = document.querySelector(
    '.article-container article,main article,[role="main"]',
  );
  if (!root) return;

  const counts = {
    heading: 0,
    paragraph: 0,
    directive_title: 0,
    equation: 0,
    tikz_scale: 0,
    admonition: 0,
    list: 0,
  };

  const clean = (node) => {
    const clone = node.cloneNode(true);
    clone.querySelectorAll('.headerlink').forEach((link) => link.remove());
    return clone.textContent.trim();
  };
  const value = (node) =>
    node.dataset.pytexmdKind === 'tikz_scale'
      ? node.dataset.pytexmdScale || '1'
      : clean(node);
  const send = (node, dirty = false) =>
    parent.postMessage(
      {
        type: 'pytexmd-select',
        kind: node.dataset.pytexmdKind,
        index: Number(node.dataset.pytexmdIndex),
        value: value(node),
        dirty,
      },
      location.origin,
    );
  const select = (node) => {
    root
      .querySelectorAll('[data-pytexmd-kind]')
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
    }
    node.style.outlineOffset = '4px';
    node.addEventListener('focus', () => select(node));
    node.addEventListener('click', (event) => {
      event.stopPropagation();
      select(node);
    });
    node.addEventListener('input', () => {
      node.dataset.pytexmdChanged = 'true';
    });
    node.addEventListener('blur', () => {
      if (node.dataset.pytexmdChanged !== 'true') return;
      node.dataset.pytexmdChanged = 'false';
      parent.postMessage(
        {
          type: 'pytexmd-commit',
          kind: node.dataset.pytexmdKind,
          index: Number(node.dataset.pytexmdIndex),
          value: value(node),
        },
        location.origin,
      );
    });
  };

  root
    .querySelectorAll('h1,h2,h3,h4,h5,h6')
    .forEach((node) => register(node, 'heading', true));
  root.querySelectorAll('p').forEach((node) => {
    if (
      node.closest(
        'nav,.sidebar,.math,.admonition-title,li,blockquote,figure,table,.topic',
      ) || node.classList.contains('admonition-title')
    )
      return;
    register(node, 'paragraph', true);
  });
  [...root.querySelectorAll('.proof .admonition-title,.prf .admonition-title')]
    .filter((node) => {
      const container = node.closest('.proof');
      return container && [...container.classList].some((name) => name !== 'proof');
    })
    .forEach((node) => register(node, 'directive_title'));
  root.querySelectorAll('div.math').forEach((node) => register(node, 'equation'));
  root.querySelectorAll('img').forEach((node) => {
    if (!/tikz-/i.test(node.getAttribute('src') || '')) return;
    node.dataset.pytexmdScale = '1';
    register(node, 'tikz_scale');
  });
  [...new Set(root.querySelectorAll('.proof,.admonition'))]
    .filter((node) => !node.classList.contains('tikz-fallback'))
    .forEach((node) => register(node, 'admonition'));
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

  window.addEventListener('message', (event) => {
    if (event.origin !== location.origin || event.data?.type !== 'pytexmd-update')
      return;
    const node = root.querySelector(
      `[data-pytexmd-kind="${event.data.kind}"][data-pytexmd-index="${event.data.index}"]`,
    );
    if (!node) return;
    if (event.data.kind === 'tikz_scale') {
      node.dataset.pytexmdScale = event.data.value;
      node.style.width = `${Number(event.data.value) * 100}%`;
      node.style.height = 'auto';
    } else if (event.data.kind === 'admonition' || event.data.kind === 'list') {
      node.innerHTML = `<pre style="white-space:pre-wrap"></pre>`;
      node.querySelector('pre').textContent = event.data.value;
    } else {
      node.textContent = event.data.value;
    }
    select(node);
  });

  parent.postMessage({ type: 'pytexmd-ready' }, location.origin);
})();
