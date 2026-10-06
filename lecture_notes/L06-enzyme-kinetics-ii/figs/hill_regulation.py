#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "matplotlib"]
# ///
"""L06 Figure -- Hill functions as regulation: cooperative competitive and non-competitive inhibitors.

If n inhibitor molecules bind together (strong cooperativity, Ingalls Exercise 3.3.3), the factor
(1 + i/Ki) of Section 3.2 becomes (1 + (i/Ki)^n):

    competitive:      v = Vmax s / (KM (1 + (i/Ki)^n) + s)
    non-competitive:  v = Vmax / (1 + (i/Ki)^n) * s / (KM + s)

A. The regulation factor 1/(1 + (i/Ki)^n), a decreasing Hill function, for n = 1, 2, 4.
B. Competitive, n = 4: activity v(i)/v(0) at three substrate levels. The half-inhibiting dose
   i50 = Ki (1 + s/KM)^(1/n) moves with substrate, but only by the n-th root.
C. Non-competitive, n = 4: the same three substrate levels give one curve; i50 = Ki always.
"""
import pathlib
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

OUT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "tools").is_dir()) / "course/build"

KM, KI = 0.5, 0.4                      # mM, mM
S_LEVELS = (0.05, 0.5, 5.0)            # mM: s/KM = 0.1, 1, 10


def frac_comp(i, s, n):
    return (KM + s) / (KM * (1 + (i / KI) ** n) + s)


def frac_noncomp(i, s, n):
    return 1 / (1 + (i / KI) ** n)


def i50_comp(s, n):
    return KI * (1 + s / KM) ** (1 / n)


def main():
    for n in (1, 4):
        for s in S_LEVELS:
            assert abs(frac_comp(i50_comp(s, n), s, n) - 0.5) < 1e-12
            assert abs(frac_noncomp(KI, s, n) - 0.5) < 1e-12

    figstyle.use(width=13.0, height=4.8)
    fig, (a, b, c) = plt.subplots(1, 3, sharey=True)
    fig.subplots_adjust(wspace=0.12)
    i = np.logspace(-2, 1, 600)                          # mM
    for n, col in zip((1, 2, 4), (figstyle.SERIES[0], figstyle.SERIES[2], figstyle.SERIES[1])):
        a.plot(i, frac_noncomp(i, 0, n), color=col, label=f"n = {n}")
    a.set_title("A  The regulation factor", pad=8)
    a.set_ylabel("activity  v(i) / v(0)")
    a.legend(loc="lower left", fontsize=9)
    a.text(0.011, 0.55, r"$\frac{1}{1+(i/K_i)^n}$", fontsize=14, color=figstyle.INK)

    cols = (figstyle.SERIES[0], figstyle.SERIES[2], figstyle.SERIES[3])
    for s, col in zip(S_LEVELS, cols):
        b.plot(i, frac_comp(i, s, 4), color=col, label=f"s = {s/KM:g} $K_M$:  $i_{{50}}$ = {i50_comp(s, 4):.2f} mM")
        c.plot(i, frac_noncomp(i, s, 4), color=col, linewidth=2.0 + 2.0 * (s == S_LEVELS[0]),
               alpha=0.9, label=f"s = {s/KM:g} $K_M$:  $i_{{50}}$ = {KI:.2f} mM")
    b.set_title("B  Competitive, n = 4", pad=8)
    c.set_title("C  Non-competitive, n = 4", pad=8)
    for ax in (a, b, c):
        ax.set_xscale("log")
        ax.set_xlabel("inhibitor i (mM, log scale)")
        ax.axhline(0.5, color=figstyle.MUTED, linestyle=":", linewidth=1.0)
        ax.set_ylim(0, 1.05)
    b.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), fontsize=9, title="substrate moves the switch", title_fontsize=9, frameon=False)
    c.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), fontsize=9, title="substrate cannot move it", title_fontsize=9, frameon=False)
    fig.savefig(OUT / "l06-hill-regulation.png")
    print(OUT / "l06-hill-regulation.png")
    for n in (1, 4):
        print(f"  competitive n={n}: i50 = " + ", ".join(f"{i50_comp(s, n):.3f}" for s in S_LEVELS)
              + f" mM at s/KM = 0.1, 1, 10  (ratio {i50_comp(S_LEVELS[2], n)/i50_comp(S_LEVELS[0], n):.2f})")


if __name__ == "__main__":
    main()
