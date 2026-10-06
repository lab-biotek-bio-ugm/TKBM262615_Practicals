#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "matplotlib"]
# ///
"""L06 Figure -- competitive against non-competitive inhibition (after Ingalls Figures 3.6, 3.8).

Same enzyme (Vmax = 10 mM/s, KM = 0.5 mM), same inhibitor affinity (Ki = 0.4 mM), same three
inhibitor levels (0, 0.4, 2 mM). Left: every competitive curve climbs to the same ceiling and bends
later. Right: every non-competitive curve bends at the same KM and stops at a lower ceiling.
The table values quoted in notes.md are asserted below.
"""
import pathlib
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

OUT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "tools").is_dir()) / "course/build"

VMAX, KM, KI = 10.0, 0.5, 0.4          # mM/s, mM, mM
LEVELS = (0.0, 0.4, 2.0)               # mM


def v_comp(s, i):
    return VMAX * s / (KM * (1 + i / KI) + s)


def v_noncomp(s, i):
    return VMAX / (1 + i / KI) * s / (KM + s)


def main():
    table = {(i, s): (v_comp(s, i), v_noncomp(s, i)) for i in LEVELS for s in (0.5, 50.0)}
    expect_c = {(0.0, 0.5): 5.00, (0.4, 0.5): 3.33, (2.0, 0.5): 1.43,
                (0.0, 50): 9.90, (0.4, 50): 9.80, (2.0, 50): 9.43}
    expect_n = {(0.0, 0.5): 5.00, (0.4, 0.5): 2.50, (2.0, 0.5): 0.83,
                (0.0, 50): 9.90, (0.4, 50): 4.95, (2.0, 50): 1.65}
    for key, val in expect_c.items():
        assert abs(table[key][0] - val) < 0.006, (key, table[key])
        assert abs(table[key][1] - expect_n[key]) < 0.006, (key, table[key])

    figstyle.use(width=11.0, height=4.0)
    fig, axes = plt.subplots(1, 2, sharey=True)
    s = np.linspace(0, 10, 600)
    cols = (figstyle.SERIES[0], figstyle.SERIES[3], figstyle.SERIES[1])
    for ax, fn, title in ((axes[0], v_comp, "A  Competitive: only $K_M$ moves"),
                          (axes[1], v_noncomp, "B  Non-competitive: only $V_{max}$ moves")):
        for i, col in zip(LEVELS, cols):
            y = fn(s, i)
            ax.plot(s, y, color=col, label=f"i = {i:g} mM")
            # mark the half-maximal point of each curve
            vmax_eff = VMAX if fn is v_comp else VMAX / (1 + i / KI)
            km_eff = KM * (1 + i / KI) if fn is v_comp else KM
            ax.plot([km_eff], [vmax_eff / 2], "o", color=col, markersize=6,
                    markeredgecolor="white", markeredgewidth=1.5, zorder=5)
        ax.axhline(VMAX, color=figstyle.MUTED, linestyle="--", linewidth=1.0)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 11)
        ax.set_xlabel("substrate s (mM)")
        ax.set_title(title, pad=8)
        ax.legend(loc="lower right", fontsize=9, title="dots: half-maximal point",
                  title_fontsize=8.5)
    axes[0].set_ylabel("rate v (mM/s)")
    axes[0].text(9.9, 10.2, "$V_{max}$ = 10", ha="right", fontsize=9, color=figstyle.MUTED)
    fig.savefig(OUT / "l06-inhibition.png")
    print(OUT / "l06-inhibition.png")
    for i in LEVELS:
        print(f"  i={i:<4g} comp: KM_eff={KM*(1+i/KI):.2f}  v(0.5)={v_comp(0.5,i):.2f} v(50)={v_comp(50,i):.2f}"
              f" | noncomp: Vmax_eff={VMAX/(1+i/KI):.2f} v(0.5)={v_noncomp(0.5,i):.2f} v(50)={v_noncomp(50,i):.2f}")


if __name__ == "__main__":
    main()
