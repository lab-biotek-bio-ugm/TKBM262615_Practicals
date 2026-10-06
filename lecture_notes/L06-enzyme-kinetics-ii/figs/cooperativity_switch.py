#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "matplotlib"]
# ///
"""L06 Figure -- why a sigmoid is a switch, in three readings of the Hill function.

A. The five-fold window. Fractional saturation Y for n = 1 (hyperbolic, myoglobin-like) and n = 3
   (near the top of Hill's fits for haemoglobin), across a five-fold range of ligand centred on K.
   The window's centring is an illustration, not a physiological measurement: Ingalls gives the
   five-fold span, not where it sits relative to K.
B. The 10%-90% span, 9^(2/n)-fold, marked on n = 1, 2, 4 (log axis).
C. The kinetic order (log-gain) of the Hill function, (x/Y)dY/dx = n(1 - Y): it starts at n and
   falls to 0. A hyperbola never exceeds 1. This is the number that makes "switch-like" precise.
"""
import pathlib
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

OUT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "tools").is_dir()) / "course/build"

NS = (1, 2, 4)


def hill(x, n, K=1.0):
    return x**n / (K**n + x**n)


def log_gain(x, n, K=1.0):
    """Kinetic order of the Hill function, computed from its definition by finite differences."""
    h = 1e-6
    return x / hill(x, n, K) * (hill(x + h, n, K) - hill(x - h, n, K)) / (2 * h)


def main():
    lo, hi = 1 / np.sqrt(5), np.sqrt(5)
    dY = {n: hill(hi, n) - hill(lo, n) for n in (1, 3)}
    assert abs(dY[1] - 0.382) < 0.001 and abs(dY[3] - 0.836) < 0.001, dY
    spans = {n: 9 ** (2 / n) for n in NS}
    for n in NS:
        x10, x90 = (1 / 9) ** (1 / n), 9 ** (1 / n)
        assert abs(hill(x10, n) - 0.1) < 1e-12 and abs(hill(x90, n) - 0.9) < 1e-12
        assert abs(x90 / x10 - spans[n]) < 1e-9
        x = np.logspace(-2, 2, 50)
        assert np.allclose(log_gain(x, n), n * (1 - hill(x, n)), atol=1e-5)
    assert abs(log_gain(1.0, 4) - 2.0) < 1e-6          # n/2 at half-saturation
    # slope at half saturation, Ingalls Exercise 3.3.2: n / (4K)
    for n in NS:
        slope = (hill(1 + 1e-6, n) - hill(1 - 1e-6, n)) / 2e-6
        assert abs(slope - n / 4) < 1e-6

    figstyle.use(width=13.0, height=4.0)
    fig, (a, b, c) = plt.subplots(1, 3)
    fig.subplots_adjust(wspace=0.32)
    x = np.linspace(0, 4, 500)
    for n, col, name in ((1, figstyle.SERIES[0], "n = 1  hyperbolic"),
                         (3, figstyle.SERIES[1], "n = 3  sigmoidal")):
        a.plot(x, hill(x, n), color=col, label=f"{name}:  ΔY = {dY[n]:.2f}")
        a.plot([lo, hi], [hill(lo, n), hill(hi, n)], "o", color=col, markersize=6,
               markeredgecolor="white", markeredgewidth=1.5, zorder=5)
    a.axvspan(lo, hi, color=figstyle.GRID, alpha=0.6)
    a.text((lo + hi) / 2, 0.03, "five-fold\nwindow", ha="center", fontsize=9, color=figstyle.INK)
    a.set_xlabel("ligand [X] / K")
    a.set_ylabel("fractional saturation Y")
    a.set_xlim(0, 4)
    a.set_ylim(0, 1.05)
    a.legend(loc="upper left", fontsize=8.5, title="unloaded across the window",
             title_fontsize=8.5)
    a.set_title("A  Same window, different delivery", pad=8)

    xl = np.logspace(-2, 2, 600)
    for n, col in zip(NS, (figstyle.SERIES[0], figstyle.SERIES[2], figstyle.SERIES[1])):
        b.plot(xl, hill(xl, n), color=col, label=f"n = {n}: {spans[n]:.0f}-fold")
        x10, x90 = (1 / 9) ** (1 / n), 9 ** (1 / n)
        yoff = {1: 0.0, 2: 0.0, 4: 0.0}[n]
        b.plot([x10, x90], [0.1, 0.9], "o", color=col, markersize=5,
               markeredgecolor="white", markeredgewidth=1.2, zorder=5)
        c.plot(xl, n * (1 - hill(xl, n)), color=col, label=f"n = {n}")
    for yy in (0.1, 0.9):
        b.axhline(yy, color=figstyle.MUTED, linestyle=":", linewidth=1.0)
    b.set_xscale("log")
    b.set_xlabel("[X] / K  (log scale)")
    b.set_ylabel("Y")
    b.set_ylim(0, 1.05)
    b.legend(loc="upper left", fontsize=8.5, title="10% to 90% needs", title_fontsize=8.5)
    b.set_title("B  How far the input must move", pad=8)

    c.axhline(1, color=figstyle.MUTED, linestyle="--", linewidth=1.0)
    c.text(0.012, 1.08, "a hyperbola never exceeds 1", fontsize=8.5, color=figstyle.MUTED)
    c.set_xscale("log")
    c.set_xlabel("[X] / K  (log scale)")
    c.set_ylabel("kinetic order  (X/Y)·dY/dX")
    c.set_ylim(0, 4.3)
    c.legend(loc="upper right", fontsize=8.5)
    c.set_title("C  Sensitivity: % out per % in", pad=8)
    fig.savefig(OUT / "l06-cooperativity-switch.png")
    print(OUT / "l06-cooperativity-switch.png")
    print(f"  five-fold window centred on K: dY(n=1)={dY[1]:.3f}  dY(n=3)={dY[3]:.3f}")
    print("  10-90% spans: " + ", ".join(f"n={n}: {spans[n]:.2f}" for n in NS))
    print(f"  Y at window edges n=1: {hill(lo,1):.3f}-{hill(hi,1):.3f};  n=3: {hill(lo,3):.3f}-{hill(hi,3):.3f}")


if __name__ == "__main__":
    main()
