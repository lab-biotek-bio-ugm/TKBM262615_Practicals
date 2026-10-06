#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "matplotlib"]
# ///
"""L02 Figure — the tangent line approximation, and exactly where it stops working.

The lecture's point: near an operating point x*, a nonlinear curve is well approximated by its
tangent line. Far from x*, the approximation is not just imprecise, it can predict something
physically impossible. This reproduces the worked example on the local-versus-global-behaviour
wiki page: f(x) = x / (1 + x), a saturating curve with y_max = 1 and K = 1, linearised at x* = 1.

The two check values (x=1.1: close; x=5: predicts above the y_max=1 ceiling) are computed here,
not guessed, and asserted before the figure is saved.
"""
import pathlib
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

X_STAR = 1.0


def f(x):
    return x / (1.0 + x)


def tangent(x, x_star=X_STAR):
    f_star = f(x_star)
    slope = 1.0 / (1.0 + x_star) ** 2       # f'(x) = 1/(1+x)^2
    return f_star + slope * (x - x_star)


def main():
    figstyle.use(width=6.8, height=4.2)
    x = np.linspace(0, 6, 400)

    # the two check points quoted in the lecture
    close_x, far_x = 1.1, 5.0
    close_err = abs(tangent(close_x) - f(close_x))
    far_pred = tangent(far_x)
    assert close_err < 0.002, f"expected the x=1.1 approximation within 0.002, got {close_err:.4f}"
    assert far_pred > 1.0, f"expected the x=5 prediction above the y_max=1 ceiling, got {far_pred:.4f}"

    fig, ax = plt.subplots()
    ax.plot(x, f(x), color=figstyle.SERIES[0], label="f(x) = x / (1+x)")
    ax.plot(x, tangent(x), color=figstyle.SERIES[1], linestyle="--",
            label=f"tangent at x* = {X_STAR:g}")
    ax.axhline(1.0, color=figstyle.MUTED, linewidth=1.0, linestyle=":")
    ax.text(5.7, 1.03, "$y_{max}=1$", color=figstyle.MUTED, fontsize=9.5, ha="right")

    ax.plot([X_STAR], [f(X_STAR)], "o", color=figstyle.INK, markersize=6, zorder=5)
    ax.annotate(f"x={close_x:g}: off by {close_err:.3f}", xy=(close_x, f(close_x)),
                xytext=(close_x + 0.3, f(close_x) - 0.28),
                arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0), fontsize=9.5)
    ax.annotate(f"x={far_x:g}: predicts {far_pred:.2f} —\nabove the ceiling", xy=(far_x, tangent(far_x)),
                xytext=(far_x - 2.6, tangent(far_x) + 0.05),
                arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0), fontsize=9.5)

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_ylim(0, 1.6)
    ax.legend(loc="lower right")
    fig.suptitle("Local means local: the tangent line, and where it breaks",
                 color=figstyle.NAVY, fontweight="bold", fontsize=12.5, x=0.008, y=0.99, ha="left")

    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l02-local-linear.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    print(f"{out}  (x=1.1 error: {close_err:.4f}, x=5 prediction: {far_pred:.4f})")


if __name__ == "__main__":
    main()
