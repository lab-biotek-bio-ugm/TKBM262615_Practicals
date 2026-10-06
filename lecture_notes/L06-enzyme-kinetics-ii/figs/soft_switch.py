#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""L06 Figure -- a sigmoid is a soft switch: sharp, but graded and without memory.

An illustrative model assembled from course pieces, in arbitrary units: an output y is produced at a
rate given by a Hill function of an input x, and decays first-order (production and decay, L03):

    dy/dt = alpha * x^n / (K^n + x^n) - delta * y,    alpha = 1 /time, delta = 1 /time, K = 1

The input ramps slowly up from 0 to 3 and back down (800 time units in all, against a response time
1/delta = 1). A: the time courses for n = 1 and n = 4. B: output against input, with the upward
and downward sweeps drawn separately. They lie on top of each other: the response is a function of
the present input only. Nothing is remembered, which is what separates this from the bistable
toggle switch of L01.
"""
from scipy.integrate import solve_ivp
import pathlib
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

OUT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "tools").is_dir()) / "course/build"

ALPHA, DELTA, K = 1.0, 1.0, 1.0
T_HALF, X_MAX = 400.0, 3.0


def x_in(t):
    return X_MAX * (t / T_HALF if t <= T_HALF else max(0.0, 2 - t / T_HALF))


def model(t, y, n):
    x = x_in(t)
    return [ALPHA * x**n / (K**n + x**n) - DELTA * y[0]]


def main():
    t = np.linspace(0, 2 * T_HALF, 8001)
    runs = {}
    for n in (1, 4):
        sol = solve_ivp(model, [0, 2 * T_HALF], [0.0], args=(n,), t_eval=t, rtol=1e-9,
                        atol=1e-12, max_step=1.0)
        runs[n] = sol.y[0]
    x = np.array([x_in(tt) for tt in t])
    up, down = t <= T_HALF, t >= T_HALF
    gaps = {}
    for n in (1, 4):
        grid = np.linspace(0.2, 2.8, 50)
        yu = np.interp(grid, x[up], runs[n][up])
        yd = np.interp(grid, x[down][::-1], runs[n][down][::-1])
        gaps[n] = np.max(np.abs(yu - yd))
    assert max(gaps.values()) < 0.02, f"up and down sweeps should nearly coincide: {gaps}"

    figstyle.use(width=11.5, height=4.0)
    fig, (a, b) = plt.subplots(1, 2, gridspec_kw={"width_ratios": [1.35, 1]})
    fig.subplots_adjust(wspace=0.25)
    a.plot(t, x / X_MAX, color=figstyle.MUTED, linewidth=1.4, label="input x / 3")
    a.plot(t, runs[1], color=figstyle.SERIES[0], label="output, n = 1")
    a.plot(t, runs[4], color=figstyle.SERIES[1], label="output, n = 4")
    a.set_xlabel("time (a.u.)")
    a.set_ylabel("level (a.u.)")
    a.set_xlim(0, 2 * T_HALF)
    a.set_ylim(0, 1.08)
    a.legend(loc="upper right", fontsize=9)
    a.set_title("A  Ramp the input up, then down", pad=8)

    for n, col in ((1, figstyle.SERIES[0]), (4, figstyle.SERIES[1])):
        b.plot(x[up], runs[n][up], color=col, label=f"n = {n}, input rising")
        b.plot(x[down], runs[n][down], color=col, linestyle=(0, (2, 2)), linewidth=2.6,
               label=f"n = {n}, input falling")
    b.axvline(K, color=figstyle.MUTED, linestyle=":", linewidth=1.0)
    b.text(K + 0.05, 0.05, "K", color=figstyle.MUTED, fontsize=9)
    b.set_xlabel("input x (a.u.)")
    b.set_ylabel("output y (a.u.)")
    b.set_xlim(0, X_MAX)
    b.set_ylim(0, 1.08)
    b.legend(loc="lower right", fontsize=8.5)
    b.set_title("B  Same path both ways: no memory", pad=8)
    fig.savefig(OUT / "l06-soft-switch.png")
    print(OUT / "l06-soft-switch.png")
    print(f"  largest up/down gap in y at equal x: n=1 {gaps[1]:.3f}, n=4 {gaps[4]:.3f}")
    for n in (1, 4):
        for xv in (0.5, 1.0, 2.0):
            print(f"  n={n} x={xv}: steady y = {xv**n/(1+xv**n):.3f}")


if __name__ == "__main__":
    main()
