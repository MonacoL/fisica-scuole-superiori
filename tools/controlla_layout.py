"""Controllo responsive: apre ogni pagina a larghezza telefono e tablet e cerca scroll orizzontale.

Uso: uv run --with playwright python tools/controlla_layout.py [--shots DIR]
Usa Chrome di sistema (/usr/bin/google-chrome) se c'è, altrimenti il Chromium di Playwright.
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PAGINE = ["index.html", "gravitazione/index.html", "gravitazione/1-keplero-newton.html",
          "gravitazione/2-satelliti-campo.html", "gravitazione/3-energia-fuga.html",
          "gravitazione/verifica.html", "gravitazione/formulario.html"]
LARGHEZZE = {"telefono": 360, "tablet": 768}
JS = """() => {
  document.querySelectorAll('details').forEach(d => d.open = true);
  const W = document.documentElement.clientWidth, out = [];
  document.querySelectorAll('main *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width && r.right > W + 1 && !el.closest('.tw, mjx-container[display="true"]'))
      out.push(el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '') + ' ' + Math.round(r.right) + 'px');
  });
  return {W, sw: document.documentElement.scrollWidth, out: out.slice(0, 5),
          mjerr: document.querySelectorAll('mjx-merror').length,
          imgrotte: [...document.images].filter(i => !i.naturalWidth).map(i => i.src)};
}"""


def main():
    shots = None
    if "--shots" in sys.argv:
        shots = Path(sys.argv[sys.argv.index("--shots") + 1]); shots.mkdir(parents=True, exist_ok=True)
    chrome = "/usr/bin/google-chrome" if os.path.exists("/usr/bin/google-chrome") else None
    problemi = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome)
        for nome, w in LARGHEZZE.items():
            page = browser.new_page(viewport={"width": w, "height": 900})
            for rel in PAGINE:
                page.goto((ROOT / rel).as_uri())
                page.wait_for_function("() => !window.MathJax || (MathJax.startup && MathJax.startup.promise)", timeout=15000)
                page.evaluate("() => window.MathJax && MathJax.startup ? MathJax.startup.promise : null")
                r = page.evaluate(JS)
                if r["sw"] > r["W"] + 1:
                    problemi.append(f"{rel} [{nome}]: scroll orizzontale ({r['sw']}px su {r['W']}px) {r['out']}")
                if r["mjerr"]:
                    problemi.append(f"{rel} [{nome}]: {r['mjerr']} errori MathJax")
                if r["imgrotte"]:
                    problemi.append(f"{rel} [{nome}]: immagini non caricate {r['imgrotte']}")
                if shots:
                    page.screenshot(path=str(shots / f"{nome}-{rel.replace('/', '_')}.png"), full_page=False)
            page.close()
        browser.close()
    if problemi:
        print(f"✗ {len(problemi)} problemi di layout:")
        for x in problemi: print("  -", x)
        sys.exit(1)
    print(f"✓ {len(PAGINE)} pagine × {len(LARGHEZZE)} larghezze: niente scroll orizzontale, formule e immagini ok")


if __name__ == "__main__":
    main()
