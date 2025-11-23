"""
Public API for the python-plot-template package.
"""

from .styles import PAUL_TOL_PALETTES, apply_template, palette_colors, style_context
from .utils import (
    add_hline,
    add_vline,
    format_ticks,
    save_plot,
    set_labels,
    set_limits,
)

__all__ = [
    "apply_template",
    "palette_colors",
    "style_context",
    "PAUL_TOL_PALETTES",
    "set_limits",
    "format_ticks",
    "add_hline",
    "add_vline",
    "save_plot",
    "set_labels",
]
