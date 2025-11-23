import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from python_plot_template import (
    add_hline,
    add_vline,
    apply_template,
    format_ticks,
    save_plot,
    set_labels,
    set_limits,
)


def test_save_plot_creates_file(tmp_path):
    apply_template()
    fig, ax = plt.subplots()
    set_labels("Title", "X", "Y", ax=ax)

    out_path = tmp_path / "plot.png"
    saved = save_plot(out_path, dpi=150, fig=fig)

    assert saved == out_path
    assert out_path.exists()
    assert out_path.stat().st_size > 0


def test_smoke_helpers_and_save(tmp_path):
    apply_template()
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0.1, 0.5, 0.2], label="line")
    add_hline(0.3, ax=ax, color="gray", linestyle="--")
    add_vline(1.0, ax=ax, color="gray", linestyle=":")
    set_limits((0, 2), (0, 0.6), ax=ax)
    format_ticks("{x:.1f}", axis="both", ax=ax)
    ax.legend()

    out_path = tmp_path / "helpers.png"
    save_plot(out_path, dpi=100, fig=fig)

    assert out_path.exists()
    assert out_path.stat().st_size > 0
