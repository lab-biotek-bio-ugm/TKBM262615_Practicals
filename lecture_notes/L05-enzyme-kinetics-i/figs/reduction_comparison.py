#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""L05 Figure — rapid equilibrium vs quasi-steady-state, on Ingalls' network (2.24)/(2.26).

    -> A <=> B ->     with k0=5, k1=20, k-1=12, k2=2 (all time^-1 except k0, which is
                       concentration*time^-1), k1+k-1 >> k2 so the A<->B conversion is fast.

Both reductions replace two ODEs with one. The point of putting them on the same axes: rapid
equilibrium's error in [A] does not shrink as t grows -- it is wrong about where the system is
even after everything has settled -- while the QSSA's error over the transient closes completely.
Same network, same time-scale separation, two different fates, and that is the whole argument for
preferring QSSA once you can afford the extra care it needs (finding the right species).

This is the abstract rehearsal for the enzyme mechanism: Michaelis and Menten (1913) assumed the
binding step sits at equilibrium, Briggs and Haldane (1925) applied the QSSA to the complex
instead, and the two give different expressions for KM for exactly the reason shown here.

All four numbers used in the annotations (both steady states, both final errors) are computed
here and asserted against the values worked out by hand in notes.md, not read off the plot.
"""
import pathlib
import sys

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

K0, K1, KM1, K2 = 5.0, 20.0, 12.0, 2.0    # mM/s, /s, /s, /s
T_END = 6.0
A0, B0 = 8.0, 4.0


def full_model(t, y):
    a, b = y
    return [K0 - K1 * a + KM1 * b, K1 * a - KM1 * b - K2 * b]


def main():
    figstyle.use(width=7.2, height=4.2)
    tol = dict(rtol=1e-10, atol=1e-13, dense_output=True)

    full = solve_ivp(full_model, [0, T_END], [A0, B0], **tol)

    # Rapid equilibrium: pool c = a+b, effective rate k2*k1/(k1+k-1), split by k-1/(k1+k-1)
    k_eff = K2 * K1 / (KM1 + K1)
    frac_a = KM1 / (KM1 + K1)
    pool = solve_ivp(lambda t, y: [K0 - k_eff * y[0]], [0, T_END], [A0 + B0], **tol)

    # QSSA: a tracks b algebraically; b alone obeys production-and-decay
    qssa = solve_ivp(lambda t, y: [K0 - K2 * y[0]], [0, T_END], [235 / 32], **tol)
    a_qss = lambda b: (K0 + KM1 * b) / K1

    t = np.linspace(0, T_END, 600)
    a_full = full.sol(t)[0]
    a_re = frac_a * pool.sol(t)[0]
    a_qss_t = a_qss(qssa.sol(t)[0])

    a_ss_true = 1.75
    a_ss_re = frac_a * (K0 / k_eff)          # rapid equilibrium's long-run limit
    err_re_final = abs(a_full[-1] - a_re[-1])
    err_qss_final = abs(a_full[-1] - a_qss_t[-1])

    assert abs(a_full[-1] - a_ss_true) < 0.01, f"expected full model near ss=1.75, got {a_full[-1]:.4f}"
    assert abs(a_ss_re - 1.5) < 0.01, f"expected rapid-equilibrium limit 1.5, got {a_ss_re:.4f}"
    assert err_re_final > 0.2, f"expected a persistent RE error > 0.2, got {err_re_final:.4f}"
    assert err_qss_final < 0.01, f"expected QSSA error < 0.01 by t=6, got {err_qss_final:.4f}"

    fig, ax = plt.subplots()
    ax.plot(t, a_full, color=figstyle.INK, linewidth=2.4, label="full model")
    ax.plot(t, a_re, color=figstyle.SERIES[1], linestyle="--", label="rapid equilibrium")
    ax.plot(t, a_qss_t, color=figstyle.SERIES[0], linestyle=":", linewidth=2.4, label="QSSA")
    ax.axhline(a_ss_true, color=figstyle.MUTED, linewidth=0.8, linestyle=":")

    ax.annotate(f"gap never closes: {err_re_final:.2f} mM at t={T_END:g}",
                xy=(T_END, a_re[-1]), xytext=(T_END - 2.6, a_re[-1] - 0.35),
                arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0), fontsize=9.5)
    ax.annotate(f"converges: {err_qss_final:.3f} mM at t={T_END:g}",
                xy=(T_END, a_qss_t[-1]), xytext=(T_END - 2.9, a_qss_t[-1] + 0.35),
                arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0), fontsize=9.5)

    ax.set_xlabel("time (s)")
    ax.set_ylabel("[A] (mM)")
    ax.legend(loc="upper right")
    fig.suptitle("Same time-scale separation, two different fates",
                 color=figstyle.NAVY, fontweight="bold", fontsize=12.5, x=0.008, y=0.99, ha="left")

    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l05-reduction-comparison.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    print(f"{out}  (RE final error={err_re_final:.4f}, QSSA final error={err_qss_final:.4f})")


if __name__ == "__main__":
    main()
