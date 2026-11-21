# Fisica per le superiori

Sito statico con teoria ed esercizi svolti, pubblicato con GitHub Pages.

- `index.html`: home del corso; `gravitazione/`: lezioni, verifica e formulario.
- `assets/style.css`: stile comune, con i colori dei riquadri del corso di Fisica per Medicina.
- `figure/src/figure.tex`: figure e grafici in TikZ/pgfplots, convertiti in SVG in `assets/fig/`.
- `tools/numeri.py`: calcola tutti i risultati degli esercizi.

## Figure

```
cd figure && pdflatex -output-directory build src/figure.tex
for i in $(seq 1 12); do pdftocairo -svg -f $i -l $i build/figure.pdf ../assets/fig/f$(printf %02d $i).svg; done
```

## Controlli prima del deploy

```
python3 tools/controlla.py                                   # link, ancore, tag, formule, testo da docente (1 s)
uv run --with playwright python tools/controlla_layout.py    # niente scroll orizzontale a 360 e 768 px
```

Gli stessi controlli girano in GitHub Actions a ogni push su `main`: il sito si pubblica solo se passano.
