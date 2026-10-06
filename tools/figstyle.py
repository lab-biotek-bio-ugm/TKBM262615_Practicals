"""Minimal shared style for the lecture-note figure scripts (lecture_notes/*/figs/*.py)."""
import matplotlib.pyplot as plt

NAVY = "#1f3a5f"
INK = "#222222"
MUTED = "#6b7280"
GRID = "#e5e7eb"
SERIES = ["#1f77b4", "#d95f02", "#1b9e77", "#7570b3", "#e6ab02", "#a6761d"]


def use(width=7.0, height=4.0):
    plt.rcParams.update({
        "figure.figsize": (width, height), "figure.dpi": 110, "savefig.dpi": 160,
        "savefig.bbox": "tight", "axes.edgecolor": MUTED, "axes.labelcolor": INK,
        "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
        "grid.color": GRID, "text.color": INK, "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.prop_cycle": plt.cycler(color=SERIES),
    })
