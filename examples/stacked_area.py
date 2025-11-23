"""Stacked area chart for category composition over time."""

import matplotlib.pyplot as plt
import numpy as np

from python_plot_template import apply_template, palette_colors, save_plot, set_labels


def main() -> None:
    apply_template(palette="bright", font_size=12)
    rng = np.random.default_rng(7)

    periods = np.arange(1, 9)
    categories = ["A", "B", "C"]
    base = rng.uniform(20, 50, size=(len(categories), len(periods)))
    trend = np.linspace(0, 15, len(periods))
    values = base + trend  # ensure positive

    fig, ax = plt.subplots()
    ax.stackplot(
        periods,
        values,
        labels=categories,
        colors=list(palette_colors("bright"))[:3],
    )

    set_labels("Stacked area composition", "Period", "Value", ax=ax)
    ax.legend(loc="upper left")

    save_plot("examples/stacked_area.png", dpi=200, fig=fig)
    plt.show()


if __name__ == "__main__":
    main()
