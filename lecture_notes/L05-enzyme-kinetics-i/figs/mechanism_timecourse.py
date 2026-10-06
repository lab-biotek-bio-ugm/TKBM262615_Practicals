#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""L05 Figure -- the full mechanism on two clocks (after Ingalls Figure 3.3A).

The four mass-action equations for S + E <=> C -> P + E, integrated with Ingalls' Figure 3.3
parameters (k1 = 30 /mM/s, k-1 = 1 /s, k2 = 10 /s, eT = 1 mM, s(0) = 5 mM). The time axis is
logarithmic so both clocks are visible on one plot: the complex forms within a few hundredths of a
second (fast clock), while substrate becomes product over about a second (slow clock).

The left panel also checks the enzyme conservation e + c = eT along the whole trajectory; the
build asserts it rather than trusting the solver.
"""
import pathlib
import sys

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

K1, KM1, K2 = 30.0, 1.0, 10.0      # /mM/s, /s, /s
ET, S0 = 1.0, 5.0                  # mM, mM


def mechanism(t, y):
    """All four species, no conservation used: s, e, c, p."""
    s, e, c, p = y
    bind, unbind, cat = K1 * s * e, KM1 * c, K2 * c
    return [-bind + unbind, -bind + unbind + cat, bind - unbind - cat, cat]


def main():
    figstyle.use(width=9.0, height=4.0)
    t = np.logspace(-4, np.log10(2.0), 800)
    sol = solve_ivp(mechanism, [0, 2.0], [S0, ET, 0.0, 0.0], t_eval=t,
                    rtol=1e-10, atol=1e-13, method="LSODA")
    s, e, c, p = sol.y
    drift = np.max(np.abs(e + c - ET))
    assert drift < 1e-8, f"enzyme conservation drifted by {drift}"
    t_c = t[np.argmax(c > 0.5 * c.max())]           # complex half-formed
    t_p = t[np.argmax(p > 0.5 * S0)]                # half the substrate converted
    assert t_p / t_c > 10, "the two clocks should differ by at least a factor of ten"

    fig, ax = plt.subplots()
    for y, name, col in ((s, "substrate s", figstyle.SERIES[0]),
                         (p, "product p", figstyle.SERIES[2]),
                         (c, "complex c", figstyle.SERIES[1]),
                         (e, "free enzyme e", figstyle.SERIES[3])):
        ax.plot(t, y, color=col, label=name)
    ax.axvspan(1e-4, 3 * t_c, color=figstyle.SERIES[1], alpha=0.08)
    ax.text(1.3e-4, 5.35, "fast clock:\ncomplex forms", fontsize=9, color=figstyle.INK, va="top")
    ax.text(0.09, 5.35, "slow clock:\nS becomes P", fontsize=9, color=figstyle.INK, va="top")
    ax.set_xscale("log")
    ax.set_xlim(1e-4, 2.0)
    ax.set_ylim(0, 5.6)
    ax.set_xlabel("time (s, log scale)")
    ax.set_ylabel("concentration (mM)")
    ax.legend(loc="center left", fontsize=9)
    ax.set_title("One mechanism, two clocks", pad=8)
    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l05-mechanism-timecourse.png"
    fig.savefig(out)
    print(out)
    print(f"  complex half-formed at t = {t_c:.4f} s; half of S converted at t = {t_p:.3f} s;"
          f" ratio {t_p / t_c:.0f}; max |e + c - eT| = {drift:.1e}")


if __name__ == "__main__":
    main()
