"""Line and scatter demo using the bright palette with synthetic metrics."""

import matplotlib.pyplot as plt
import numpy as np

from python_plot_template import apply_template, palette_colors, save_plot, set_labels


def main() -> None:
    apply_template(palette="bright", font_size=12)

    months = np.array(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    )
    visits = (
        np.array([12, 13.5, 14.2, 15, 16.5, 17.2, 18.1, 17.5, 16.8, 16, 15.5, 17])
        * 1000
    )
    signups = (
        np.array(
            [0.62, 0.705, 0.78, 0.82, 0.91, 0.94, 0.98, 0.95, 0.905, 0.87, 0.84, 0.92]
        )
        * 1000
    )
    conv_rate = signups / visits
    fig, ax = plt.subplots()

    ax.plot(months, visits, label="Visits", linewidth=2.2)
    ax.plot(months, signups, label="Signups", linewidth=2.0)
    ax.scatter(
        months,
        conv_rate * visits,
        color=list(palette_colors("bright"))[1],
        label="Conv. rate x visits",
        zorder=3,
    )

    set_labels("Monthly traffic & signups", "Month", "Count", ax=ax)
    ax.legend(loc="upper left")
    ax.set_ylim(0, max(visits) * 1.1)

    save_plot("examples/line_and_scatter.png", dpi=200, fig=fig)
    plt.show()


if __name__ == "__main__":
    main()
