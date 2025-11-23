"""Bar chart demo using the muted palette inside a style context."""

import matplotlib.pyplot as plt

from python_plot_template import palette_colors, save_plot, set_labels, style_context


def main() -> None:
    categories = ["A", "B", "C", "D"]
    values = [3.5, 5.0, 2.4, 4.1]
    colors = list(palette_colors("muted"))

    with style_context("muted", font_size=12):
        fig, ax = plt.subplots()
        ax.bar(categories, values, color=colors[: len(categories)])

        set_labels("Muted bar chart", "Category", "Value", ax=ax)
        save_plot("examples/muted_bar_chart.png", dpi=200, fig=fig)
        plt.show()


if __name__ == "__main__":
    main()
