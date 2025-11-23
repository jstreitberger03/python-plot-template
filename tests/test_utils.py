import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from python_plot_template import apply_template, save_plot, set_labels


def test_save_plot_creates_file(tmp_path):
    apply_template()
    fig, ax = plt.subplots()
    set_labels("Title", "X", "Y", ax=ax)

    out_path = tmp_path / "plot.png"
    saved = save_plot(out_path, dpi=150, fig=fig)

    assert saved == out_path
    assert out_path.exists()
    assert out_path.stat().st_size > 0
