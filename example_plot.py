import matplotlib.pyplot as plt
import numpy as np

from plot_template import apply_style, palette_colors


def main() -> None:
    apply_style(palette="bright", font_size=12)

    x = np.linspace(0, 2 * np.pi, 200)
    signals = [
        ("sine", np.sin(x)),
        ("cosine", np.cos(x)),
        ("sine*exp", np.sin(x) * np.exp(-0.3 * x)),
    ]

    fig, ax = plt.subplots()
    for (label, y), color in zip(signals, palette_colors("bright"), strict=False):
        ax.plot(x, y, label=label, color=color, linewidth=2.0)

    ax.set_title("Minimal Tol-styled plot")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend(loc="best")

    fig.savefig("example_plot.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
