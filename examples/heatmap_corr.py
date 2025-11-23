"""Correlation heatmap demo."""

import matplotlib.pyplot as plt
import numpy as np

from python_plot_template import apply_template, save_plot, set_labels


def main() -> None:
    rng = np.random.default_rng(21)
    apply_template(palette="muted", font_size=12)

    data = rng.normal(size=(200, 4))
    data[:, 1] += data[:, 0] * 0.5
    data[:, 2] -= data[:, 0] * 0.3
    corr = np.corrcoef(data, rowvar=False)
    labels = ["Feat1", "Feat2", "Feat3", "Feat4"]

    fig, ax = plt.subplots()
    cax = ax.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
    ax.set_xticks(range(len(labels)), labels=labels)
    ax.set_yticks(range(len(labels)), labels=labels)
    set_labels("Correlation heatmap", "Features", "Features", ax=ax)
    fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04, label="corr")

    save_plot("examples/heatmap_corr.png", dpi=200, fig=fig)
    plt.show()


if __name__ == "__main__":
    main()
