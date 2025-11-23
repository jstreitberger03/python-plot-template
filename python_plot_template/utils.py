"""
Utility helpers for saving plots and setting labels.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt


def save_plot(filename: str, dpi: int = 300, fig: Optional[plt.Figure] = None) -> Path:
    """
    Save the given Matplotlib figure (or current figure) to disk.
    """
    target = Path(filename)
    target.parent.mkdir(parents=True, exist_ok=True)
    fig_to_save = fig if fig is not None else plt.gcf()
    fig_to_save.savefig(target, dpi=dpi)
    return target


def set_labels(
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    Set title and axis labels on the provided axes (defaults to current axes).
    """
    target_ax = ax if ax is not None else plt.gca()
    if title:
        target_ax.set_title(title)
    if xlabel:
        target_ax.set_xlabel(xlabel)
    if ylabel:
        target_ax.set_ylabel(ylabel)
