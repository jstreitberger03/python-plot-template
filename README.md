## Python Plot Template

A lightweight Matplotlib template package using Paul Tol color palettes. It sets a clean blank theme with reduced axes and densely dotted y-major gridlines.

### Features
- `apply_template()` sets the base Matplotlib style
- Paul Tol colorblind-safe palettes (`bright`, `muted`) via `palette_colors`
- Utils: `save_plot(filename, dpi=300)`, `set_labels(title, xlabel, ylabel)`
- `style_context` context manager for temporary styling

### Installation
```bash
pip install -e '.[dev]'  # for local development with Ruff
```
Runtime only:
```bash
pip install matplotlib numpy
```

### Usage
```python
import matplotlib.pyplot as plt
from python_plot_template import apply_template, palette_colors, save_plot, set_labels

apply_template(palette="bright", font_size=12)
fig, ax = plt.subplots()
for color in palette_colors("bright"):
    ax.plot([0, 1, 2], [0, 1, 0], color=color)

set_labels("Example plot", "x", "y", ax=ax)
save_plot("example.png", dpi=300, fig=fig)
plt.show()
```

Temporary style:
```python
import matplotlib.pyplot as plt
from python_plot_template import style_context

with style_context("muted"):
    plt.plot([0, 1], [0, 1])
    plt.show()
```

### Example script
```bash
python example_plot.py
```
This creates `example_plot.png` with the blank theme and Paul Tol colors.

Contents of `example_plot.py`:
```python
import matplotlib.pyplot as plt
import numpy as np

from python_plot_template import (
    apply_template,
    palette_colors,
    save_plot,
    set_labels,
)


def main() -> None:
    apply_template(palette="bright", font_size=12)

    x = np.linspace(0, 2 * np.pi, 200)
    signals = [
        ("sine", np.sin(x)),
        ("cosine", np.cos(x)),
        ("sine*exp", np.sin(x) * np.exp(-0.3 * x)),
    ]

    fig, ax = plt.subplots()
    for (label, y), color in zip(signals, palette_colors("bright"), strict=False):
        ax.plot(x, y, label=label, color=color, linewidth=2.0)

    set_labels("Minimal Tol-styled plot", "x", "f(x)", ax=ax)
    ax.legend(loc="best")

    save_plot("example_plot.png", dpi=200, fig=fig)
    plt.show()


if __name__ == "__main__":
    main()
```

### More examples
- `examples/line_and_scatter.py` → saves `examples/line_and_scatter.png` (bright palette)
- `examples/muted_bar_chart.py` → saves `examples/muted_bar_chart.png` (muted palette)

Run them with:
```bash
python examples/line_and_scatter.py
python examples/muted_bar_chart.py
```

### Tests
```bash
pytest
```
