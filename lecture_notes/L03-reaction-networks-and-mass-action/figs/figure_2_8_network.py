#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""L03 Figure — Ingalls' Figure 2.8/2.9 network, regenerated from the model.

Five reactions, four species (A, B, C, D), all starting from zero and filling up. The point of
reproducing this rather than describing it: A visibly overshoots its own steady state before
settling back down, because C and D's formation needs both A and B, and B has to accumulate first.
That overshoot is a real consequence of the network's structure, not an artifact of the plot.

The peak value and timing, and all four steady states, are computed here and asserted against the
values worked out by hand in notes.md (Exercise 2.1.10's algebra) rather than eyeballed.
"""
import pathlib
import sys

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

K1, K2, K3, K4, K5 = 3.0, 2.0, 2.5, 3.0, 4.0   # mM/s, /s, /mM/s, /s, /s


def network(t, y):
    a, b, c, d = y
    v1, v2, v3, v4, v5 = K1, K2 * a, K3 * a * b, K4 * c, K5 * d
    return [v1 - v2 - v3, v2 - v3, v3 - v4, v3 - v5]


def main():
    figstyle.use(width=6.8, height=4.2)
    sol = solve_ivp(network, [0, 4], [0, 0, 0, 0], dense_output=True, rtol=1e-10, atol=1e-12)
    t = np.linspace(0, 4, 800)
    a, b, c, d = sol.sol(t)

    peak_a, peak_t = a.max(), t[a.argmax()]
    ss = sol.sol(4)
    assert abs(peak_a - 0.8884) < 0.001, f"expected peak [A]=0.8884, got {peak_a:.4f}"
    assert abs(peak_t - 0.734) < 0.01, f"expected peak at t=0.734, got {peak_t:.4f}"
    expected_ss = np.array([0.75, 0.8, 0.5, 0.375])   # from the hand algebra in notes.md
    assert np.allclose(ss, expected_ss, atol=0.001), f"expected ss {expected_ss}, got {ss}"

    fig, ax = plt.subplots()
    for name, series, color in zip("ABCD", (a, b, c, d), figstyle.SERIES):
        ax.plot(t, series, color=color, label=f"[{name}]")
    ax.axhline(peak_a, color=figstyle.MUTED, linewidth=0.8, linestyle=":")
    ax.annotate(f"[A] peaks at {peak_a:.3f} mM,\nthen settles to {ss[0]:.2f} mM",
                xy=(peak_t, peak_a), xytext=(peak_t + 0.5, peak_a + 0.05),
                arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0), fontsize=9.5)

    ax.set_xlabel("time (s)")
    ax.set_ylabel("concentration (mM)")
    ax.legend(loc="center right")
    fig.suptitle("One reaction, four consequences: A overshoots while B accumulates",
                 color=figstyle.NAVY, fontweight="bold", fontsize=12.5, x=0.008, y=0.99, ha="left")

    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l03-figure-2-8.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    print(f"{out}  (peak [A]={peak_a:.4f} at t={peak_t:.3f}, steady state={ss.round(4)})")


if __name__ == "__main__":
    main()
