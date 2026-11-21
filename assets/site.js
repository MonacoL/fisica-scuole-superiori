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
