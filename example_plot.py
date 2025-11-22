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
