"""
Public API for the python-plot-template package.
"""

from .styles import PAUL_TOL_PALETTES, apply_template, palette_colors, style_context
from .utils import save_plot, set_labels

__all__ = [
    "apply_template",
    "palette_colors",
    "style_context",
    "PAUL_TOL_PALETTES",
    "save_plot",
    "set_labels",
]
