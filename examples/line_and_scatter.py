"""Line and scatter demo using the bright palette."""

import matplotlib.pyplot as plt
import numpy as np

from python_plot_template import apply_template, palette_colors, save_plot, set_labels


def main() -> None:
    apply_template(palette="bright", font_size=12)

    x = np.linspace(0, 10, 200)
    fig, ax = plt.subplots()

    ax.plot(x, np.sin(x), label="sin(x)", linewidth=2.2)
    ax.plot(x, np.cos(x), label="cos(x)", linewidth=2.0)
    ax.scatter(
        x[::15],
        np.sin(x[::15]) + 0.1,
        color=list(palette_colors("bright"))[1],
        label="samples",
        zorder=3,
    )

    set_labels("Line & Scatter (bright)", "x", "f(x)", ax=ax)
    ax.legend(loc="best")

    save_plot("examples/line_and_scatter.png", dpi=200, fig=fig)
    plt.show()


if __name__ == "__main__":
    main()
