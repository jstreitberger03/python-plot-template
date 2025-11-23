"""Scatter plot with regression line."""

import matplotlib.pyplot as plt
import numpy as np

from python_plot_template import apply_template, save_plot, set_labels


def main() -> None:
    rng = np.random.default_rng(42)
    apply_template(palette="muted", font_size=12)

    x = rng.uniform(0, 10, size=120)
    y = 2.5 * x + rng.normal(0, 4, size=x.shape)

    slope, intercept = np.polyfit(x, y, 1)
    line_x = np.linspace(x.min(), x.max(), 100)
    line_y = slope * line_x + intercept

    fig, ax = plt.subplots()
    ax.scatter(x, y, alpha=0.6, label="Data")
    ax.plot(
        line_x,
        line_y,
        color="#332288",
        linewidth=2.5,
        label=f"y={slope:.2f}x+{intercept:.2f}",
    )

    set_labels("Scatter with regression line", "x", "y", ax=ax)
    ax.legend(loc="best")

    save_plot("examples/scatter_regression.png", dpi=200, fig=fig)
    plt.show()


if __name__ == "__main__":
    main()
