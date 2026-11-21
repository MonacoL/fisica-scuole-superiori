"""Controlli veloci sul sito prima del deploy. Solo libreria standard.

Uso: python3 tools/controlla.py   (esce con codice 1 se trova problemi)
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ESCLUSI = {"materiale_gravitazione", "figure", "tools", "docs", ".git"}
CDN_OK = ("https://cdn.jsdelivr.net/npm/mathjax@3.2.2/",)
# Tracce del piano di lezione per il docente che non devono finire nel sito per gli studenti.
VOCE_DOCENTE = re.compile(r"\b(ragazzo|fagli|chiedi|libro|scheda|venerd[iì]|sabato|marted[iì]|lavagna)\b|es\. \d", re.I)
VOID = {"meta", "link", "img", "br", "hr", "input", "source", "path", "circle", "line",
        "rect", "ellipse", "polygon", "polyline"}


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.stack, self.errori = set(), [], [], []
        self.ex_aperti = []  # [ris, sol] per ogni .ex aperto
        self.testo = []
        self.in_script = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for k in ("href", "src"):
            if k in a:
                self.refs.append((tag, a[k]))
        cls = (a.get("class") or "").split()
        if tag == "details" and self.ex_aperti:
            if "ris" in cls: self.ex_aperti[-1][0] = True
            if "sol" in cls: self.ex_aperti[-1][1] = True
        if tag == "script": self.in_script = True
        if tag in VOID or tag.startswith("mjx"):
            return
        self.stack.append((tag, "ex" in cls))
        if "ex" in cls:
            self.ex_aperti.append([False, False])

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        for k in ("href", "src"):
            if k in a:
                self.refs.append((tag, a[k]))

    def handle_endtag(self, tag):
        if tag == "script": self.in_script = False
        if tag in VOID:
            return
        if not self.stack or self.stack[-1][0] != tag:
            self.errori.append(f"tag </{tag}> non bilanciato (aperto: {self.stack[-1][0] if self.stack else '-'}) riga {self.getpos()[0]}")
            return
        _, is_ex = self.stack.pop()
        if is_ex:
            ris, sol = self.ex_aperti.pop()
            if not (ris and sol):
                self.errori.append(f"esercizio senza risultato o soluzione, riga {self.getpos()[0]}")

    def handle_data(self, d):
        if not self.in_script:
            self.testo.append(d)


def pagine():
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in ESCLUSI or rel.name.startswith("Gravitazione"):
            continue
        yield p


def main():
    problemi, parsed = [], {}
    for p in pagine():
        src = p.read_text(encoding="utf-8")
        pg = Pagina(); pg.feed(src); parsed[p] = pg
        rel = p.relative_to(ROOT)
        e = lambda m: problemi.append(f"{rel}: {m}")
        for m in pg.errori: e(m)
        if pg.stack: e(f"tag non chiusi: {[t for t, _ in pg.stack]}")
        if 'name="viewport"' not in src: e("manca il meta viewport")
        if "<title>" not in src: e("manca <title>")
        if 'lang="it"' not in src: e('manca lang="it"')
        testo = " ".join(pg.testo)
        for a, b in ((r"\(", r"\)"), (r"\[", r"\]")):
            if testo.count(a) != testo.count(b):
                e(f"formule non bilanciate: {testo.count(a)} '{a}' contro {testo.count(b)} '{b}'")
        for m in VOCE_DOCENTE.finditer(testo):
            e(f"testo da docente: «{testo[max(0, m.start()-30):m.end()+30].strip()}»")
    for p, pg in parsed.items():
        rel = p.relative_to(ROOT)
        for tag, ref in pg.refs:
            if ref.startswith(("http://", "https://")):
                if not ref.startswith(CDN_OK):
                    problemi.append(f"{rel}: risorsa esterna non prevista {ref}")
                continue
            if ref.startswith(("mailto:", "data:")):
                continue
            if ref.startswith("/"):
                problemi.append(f"{rel}: percorso assoluto {ref} (su GitHub Pages non funziona)")
                continue
            path, _, anchor = ref.partition("#")
            target = (p.parent / path).resolve() if path else p
            if not target.exists():
                problemi.append(f"{rel}: link rotto {ref}")
            elif anchor and target.suffix == ".html":
                tpg = parsed.get(target)
                if tpg and anchor not in tpg.ids:
                    problemi.append(f"{rel}: ancora inesistente {ref}")
    n = len(parsed)
    if problemi:
        print(f"✗ {len(problemi)} problemi in {n} pagine:")
        for x in problemi: print("  -", x)
        sys.exit(1)
    print(f"✓ {n} pagine controllate: link, immagini, ancore, tag, formule, viewport, testo da docente")


if __name__ == "__main__":
    main()
