"""
Lightweight Matplotlib style helper using Paul Tol's color schemes.

Call apply_style() once at program start to set a clean "blank" theme with
densely dotted y-axis major grid lines and a discrete Tol palette.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Dict, Iterable, List

import matplotlib.pyplot as plt
from matplotlib import cycler

# Paul Tol's colorblind safe palettes (hex codes from Paul Tol's website)
PAUL_TOL_PALETTES: Dict[str, List[str]] = {
    "bright": [
        "#4477AA",
        "#EE6677",
        "#228833",
        "#CCBB44",
        "#66CCEE",
        "#AA3377",
        "#BBBBBB",
    ],
    "muted": [
        "#332288",
        "#88CCEE",
        "#44AA99",
        "#117733",
        "#999933",
        "#DDCC77",
        "#CC6677",
        "#882255",
        "#AA4499",
    ],
}


def apply_style(palette: str = "bright", font_size: int = 11) -> None:
    """
    Configure Matplotlib with a minimal theme and Tol color cycle.

    Parameters
    ----------
    palette : str
        Palette key from PAUL_TOL_PALETTES.
    font_size : int
        Base font size for text elements.
    """
    colors = PAUL_TOL_PALETTES.get(palette, PAUL_TOL_PALETTES["bright"])

    plt.style.use("default")  # start from a clean base
    plt.rcParams.update(
        {
            "axes.prop_cycle": cycler(color=colors),
            "axes.facecolor": "white",
            "figure.facecolor": "white",
            "axes.edgecolor": "#A0A0A0",
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.alpha": 0.8,
            "grid.color": "#B0B0B0",
            "grid.linewidth": 0.8,
            "grid.linestyle": (0, (1, 3)),  # densely dotted
            "axes.titlesize": font_size + 1,
            "axes.labelsize": font_size,
            "xtick.labelsize": font_size - 1,
            "ytick.labelsize": font_size - 1,
            "font.size": font_size,
            "legend.frameon": False,
            "legend.fontsize": font_size - 1,
            "figure.autolayout": True,
        }
    )


@contextmanager
def style_context(palette: str = "bright", font_size: int = 11):
    """
    Context manager to temporarily apply the template style.
    """
    with plt.rc_context():
        apply_style(palette=palette, font_size=font_size)
        yield


def palette_colors(name: str = "bright") -> Iterable[str]:
    """
    Return the list of hex colors for a given Tol palette.
    """
    return PAUL_TOL_PALETTES.get(name, PAUL_TOL_PALETTES["bright"])
