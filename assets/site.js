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
  if (t) {
    t.addEventListener('click', function () {
      var dark = root.dataset.theme ? root.dataset.theme === 'dark'
        : window.matchMedia('(prefers-color-scheme: dark)').matches;
      root.dataset.theme = dark ? 'light' : 'dark';
      try { localStorage.setItem('tema', root.dataset.theme); } catch (e) {}
    });
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
