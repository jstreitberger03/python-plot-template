## Python Plot Template

Schnelles, schlichtes Matplotlib-Template mit Paul Tol Farbpaletten. Nutzt einen blanken Hintergrund, reduzierte Achsen, und dicht gepunktete Gitterlinien auf der y-Achse.

### Features
- Paul Tol colorblind-sichere Paletten (`bright`, `muted`)
- Weißer Hintergrund, reduzierte Achsen (keine Top/Right-Spines)
- Dicht gepunktete y-Majorgridlines, dezente Achsenfarbe
- Kontextmanager für temporären Stil

### Installation
Keine Abhängigkeiten außer `matplotlib` und `numpy` für das Beispiel.

```bash
pip install matplotlib numpy
```

### Nutzung
```python
from plot_template import apply_style, style_context, palette_colors
import matplotlib.pyplot as plt

apply_style(palette="bright", font_size=12)
fig, ax = plt.subplots()
for color in palette_colors("bright"):
    ax.plot([0, 1, 2], [0, 1, 0], color=color)
ax.set_ylabel("Beispiel")
plt.show()
```

Oder temporär:
```python
with style_context("muted"):
    plt.plot([0, 1], [0, 1])
    plt.show()
```

### Beispiel
Das mitgelieferte Beispiel zeigt ein erstes Beispiel:
```bash
python example_plot.py
```
Dies erzeugt `example_plot.png` mit dem Blank-Theme und Paul Tol Farben.
