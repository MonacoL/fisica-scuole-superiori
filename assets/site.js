// Pulsante "apri/chiudi tutte le soluzioni" e tema chiaro/scuro.
(function () {
  var b = document.getElementById('tog');
  if (b) {
    var open = false;
    b.addEventListener('click', function () {
      open = !open;
      document.querySelectorAll('.ex details').forEach(function (d) { d.open = open; });
      b.textContent = open ? 'Chiudi tutte le soluzioni' : 'Apri tutte le soluzioni';
    });
  }
  var t = document.getElementById('theme');
  var root = document.documentElement;
  try { var s = localStorage.getItem('tema'); if (s) root.dataset.theme = s; } catch (e) {}
  // Icona: luna quando il tema è chiaro (clic per lo scuro), sole quando è scuro.
  var SOLE = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"/><path d="M12 1.5v2.5M12 20v2.5M1.5 12H4M20 12h2.5M4.6 4.6l1.8 1.8M17.6 17.6l1.8 1.8M4.6 19.4l1.8-1.8M17.6 6.4l1.8-1.8"/></svg>';
  var LUNA = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M20.5 14.5A8.5 8.5 0 1 1 9.5 3.5a7 7 0 0 0 11 11z"/></svg>';
  function scuro() {
    return root.dataset.theme ? root.dataset.theme === 'dark'
      : window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function icona() {
    if (!t) return;
    var d = scuro();
    t.innerHTML = d ? SOLE : LUNA;
    t.setAttribute('aria-label', d ? 'Passa al tema chiaro' : 'Passa al tema scuro');
    t.title = t.getAttribute('aria-label');
  }
  if (t) {
    icona();
    t.addEventListener('click', function () {
      root.dataset.theme = scuro() ? 'light' : 'dark';
      try { localStorage.setItem('tema', root.dataset.theme); } catch (e) {}
      icona();
    });
    try { window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', icona); } catch (e) {}
  }
})();

// Ingrandimento delle figure: clic sull'immagine, chiusura con clic, Esc o pulsante.
(function () {
  var figs = document.querySelectorAll('.fig > img, .fig > svg');
  if (!figs.length) return;
  var box = document.createElement('div');
  box.className = 'zoom'; box.hidden = true;
  box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-label', 'Figura ingrandita');
  box.innerHTML = '<button type="button">Chiudi</button><div class="zc"></div>';
  document.body.appendChild(box);
  var slot = box.querySelector('.zc'), last = null;
  function close() { box.hidden = true; slot.innerHTML = ''; document.body.classList.remove('zoom-on'); if (last) last.focus(); }
  function open(el) {
    last = el;
    var c = el.cloneNode(true);
    c.removeAttribute('width'); c.removeAttribute('height');
    slot.appendChild(c); box.hidden = false; document.body.classList.add('zoom-on');
    box.querySelector('button').focus();
  }
  figs.forEach(function (el) {
    el.setAttribute('tabindex', '0');
    el.setAttribute('title', 'Clicca per ingrandire');
    el.addEventListener('click', function () { open(el); });
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(el); } });
  });
  box.addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !box.hidden) close(); });
})();
