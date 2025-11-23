import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from python_plot_template import apply_template, palette_colors


def test_apply_template_sets_rcparams():
    apply_template(palette="bright", font_size=12)

    assert plt.rcParams["axes.grid"] is True
    assert plt.rcParams["axes.grid.axis"] == "y"
    assert plt.rcParams["grid.linestyle"] == (0, (1, 3))

    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    assert colors[: len(palette_colors("bright"))] == list(palette_colors("bright"))


def test_palette_colors_fallbacks():
    default_colors = list(palette_colors())
    missing_colors = list(palette_colors("not_a_palette"))
    assert default_colors == missing_colors
