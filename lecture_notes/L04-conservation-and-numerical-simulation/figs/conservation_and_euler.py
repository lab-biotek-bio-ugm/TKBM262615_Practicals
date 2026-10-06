#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""L04 Figure -- the two halves of the lecture, side by side.

Panel A: the closed network A <-> B. Both concentrations move; their sum does not. The flat
line is the conservation relation a(t) + b(t) = T, and it is flat for every choice of rate
constants, which is what "structural" means.

Panel B: Euler's method on da/dt = -a, at h = 2/3 and h = 1/3, against the exact e^{-t}. The
markers are the only points Euler actually computes; the straight segments between them are the
constant-rate assumption made visible.

Panel C: the price list. Euler's error against step size on log-log axes is a straight line of
slope 1 -- halve h, halve the error -- while solve_ivp with tight tolerances sits nine orders of
magnitude lower. This is the slide that says why nobody uses Euler and everybody should
understand it.

Every annotated number is computed and asserted here, not read off the plot.
"""
import pathlib
import sys

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

KP, KM = 0.8, 0.2          # forward / reverse rate constants, 1/s  (Practical 02 Example IV)
A0, B0 = 3.0, 1.0          # mM
T = A0 + B0
T_END = 2.0                # for the Euler panel, on da/dt = -a


def reversible(t, y, kp, km):
    a, b = y
    return [-kp * a + km * b, kp * a - km * b]


def euler(f, y0, t_end, h):
    """Ingalls equation (2.16), applied repeatedly.

    The mesh is built with linspace on an integer step count, never with arange: a
    floating-point arange can emit a spurious final point past t_end and silently report the
    answer at the wrong time.
    """
    n = int(round(t_end / h))
    ts = np.linspace(0, t_end, n + 1)
    ys = np.empty_like(ts)
    ys[0] = y0
    for i in range(n):
        ys[i + 1] = ys[i] + h * f(ys[i])
    return ts, ys


def main():
    figstyle.use(width=12.6, height=3.9)
    tol = dict(rtol=1e-11, atol=1e-13, dense_output=True)

    # ---------------------------------------------------------------- checks first
    sol = solve_ivp(reversible, [0, 40], [A0, B0], args=(KP, KM), **tol)
    t = np.linspace(0, 12, 800)
    a, b = sol.sol(t)
    total = a + b
    drift = np.max(np.abs(total - T))
    assert drift < 1e-9, f"the conservation should survive integration; drifted {drift:.2e}"

    a_ss, b_ss = KM * T / (KP + KM), KP * T / (KP + KM)
    assert abs(a_ss + b_ss - T) < 1e-12, "the two steady states must add back to T"
    assert abs(sol.sol(40)[0] - a_ss) < 1e-9, f"expected a -> {a_ss:.4f}, got {sol.sol(40)[0]:.6f}"

    exact = lambda tt: np.exp(-tt)
    steps = [2 / 3, 1 / 3, 1 / 6, 1 / 12, 1 / 30, 1 / 100, 1 / 300]
    errors = [abs(euler(lambda y: -y, 1.0, T_END, h)[1][-1] - exact(T_END)) for h in steps]
    slope = np.polyfit(np.log(steps), np.log(errors), 1)[0]
    assert 0.9 < slope < 1.1, f"Euler is first order; measured slope {slope:.3f}"

    ref = solve_ivp(lambda tt, y: [-y[0]], [0, T_END], [1.0], rtol=1e-12, atol=1e-14)
    ivp_err = abs(ref.y[0, -1] - exact(T_END))
    assert ivp_err < 1e-9, f"solve_ivp should be far better than Euler; got {ivp_err:.2e}"

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.subplots_adjust(wspace=0.32)

    # ---------------------------------------------------------------- A: conservation
    ax1.plot(t, a, color=figstyle.SERIES[0], label="[A]")
    ax1.plot(t, b, color=figstyle.SERIES[1], label="[B]")
    ax1.plot(t, total, color=figstyle.INK, linewidth=2.4, label="[A] + [B]")
    ax1.axhline(T, color=figstyle.MUTED, linestyle=":", linewidth=1.0)
    ax1.annotate(f"T = {T:g} mM, whatever $k_+$ and $k_-$ are",
                 xy=(8.5, T), xytext=(2.3, T + 0.55), fontsize=9, color=figstyle.INK,
                 arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0))
    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("concentration (mM)")
    ax1.set_ylim(0, T * 1.35)
    ax1.set_xlim(0, 12)
    ax1.text(11.8, b_ss + 0.12, f"$b^{{ss}}$ = {b_ss:g}", ha="right", fontsize=9,
             color=figstyle.SERIES[1])
    ax1.text(11.8, a_ss + 0.12, f"$a^{{ss}}$ = {a_ss:g}", ha="right", fontsize=9,
             color=figstyle.SERIES[0])
    ax1.legend(loc="center left", fontsize=9, ncol=1)
    ax1.set_title("A  The sum never moves", pad=8)

    # ---------------------------------------------------------------- B: Euler steps
    fine = np.linspace(0, T_END, 400)
    ax2.plot(fine, exact(fine), color=figstyle.INK, linewidth=2.2, label=r"exact  $e^{-t}$")
    for h, colour in ((2 / 3, figstyle.SERIES[1]), (1 / 3, figstyle.SERIES[2])):
        ts, ys = euler(lambda y: -y, 1.0, T_END, h)
        ax2.plot(ts, ys, "-o", color=colour, linewidth=1.6, markersize=5,
                 label=f"Euler, h = {h:.3g}")
    ax2.set_xlabel("time")
    ax2.set_ylabel("a(t)")
    ax2.set_xlim(0, T_END)
    ax2.set_ylim(0, 1.05)
    ax2.legend(loc="upper right", fontsize=9)
    ax2.set_title("B  Euler freezes the rate", pad=8)

    # ---------------------------------------------------------------- C: error vs step size
    ax3.loglog(steps, errors, "-o", color=figstyle.SERIES[0], markersize=5,
               label=f"Euler (slope {slope:.2f})")
    ax3.axhline(ivp_err, color=figstyle.SERIES[3], linestyle="--", linewidth=1.8,
                label="solve_ivp, tight tol")
    ax3.set_xlabel("step size h")
    ax3.set_ylabel("error in a(2)")
    ax3.set_xlim(2e-3, 1.5)
    ax3.set_ylim(3e-15, 3)
    ax3.legend(loc="upper left", fontsize=9)
    ax3.grid(True, which="both", color=figstyle.GRID, linewidth=0.6)
    ax3.set_title("C  Halve h, halve the error", pad=8)

    fig.suptitle("Conservation is exact; a numerical answer is only as good as you paid for",
                 color=figstyle.NAVY, fontweight="bold", fontsize=12.5, x=0.005, y=1.03, ha="left")

    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l04-conservation-and-euler.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    print(f"{out}")
    print(f"  T={T:g}  a_ss={a_ss:.4f}  b_ss={b_ss:.4f}  conservation drift={drift:.2e}")
    print(f"  Euler slope={slope:.3f}  errors={[f'{e:.4f}' for e in errors[:3]]}"
          f"  solve_ivp err={ivp_err:.2e}")


if __name__ == "__main__":
    main()
