"""
Utility helpers for saving plots and setting labels.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

import matplotlib.pyplot as plt
from matplotlib import ticker


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


def set_limits(
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    ax: Optional[plt.Axes] = None,
) -> None:
    """Set axis limits if provided."""
    target_ax = ax if ax is not None else plt.gca()
    if xlim:
        target_ax.set_xlim(xlim)
    if ylim:
        target_ax.set_ylim(ylim)


def format_ticks(
    fmt: str = "{x:.2f}",
    axis: str = "both",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    Apply tick formatting using StrMethodFormatter to the given axis/axes.
    """
    target_ax = ax if ax is not None else plt.gca()
    formatter = ticker.StrMethodFormatter(fmt)
    if axis in ("x", "both"):
        target_ax.xaxis.set_major_formatter(formatter)
    if axis in ("y", "both"):
        target_ax.yaxis.set_major_formatter(formatter)


def add_hline(y: float, ax: Optional[plt.Axes] = None, **kwargs) -> None:
    """Add a horizontal reference line."""
    target_ax = ax if ax is not None else plt.gca()
    target_ax.axhline(y, **kwargs)


def add_vline(x: float, ax: Optional[plt.Axes] = None, **kwargs) -> None:
    """Add a vertical reference line."""
    target_ax = ax if ax is not None else plt.gca()
    target_ax.axvline(x, **kwargs)
