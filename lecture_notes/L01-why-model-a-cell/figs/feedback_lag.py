#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "matplotlib"]
# ///
"""L01 Figure 1 — one negative feedback loop, three amounts of lag.

The lecture's point: "negative feedback stabilises" is the default, not a law. Delay the
correction and the same loop goes from settling, to ringing, to oscillating forever. Nothing
about the loop changes except *when* the correction arrives — which is the hallway thermostat.

Model: dx/dt = 1 / (1 + x(t - tau)^n) - k x(t). The output represses its own production, but
using its value tau time units ago. This is a delay differential equation, so it is integrated
with RK4 on a fixed grid holding the delayed value across each step — scipy's solve_ivp does
not take a delay term.

The three regimes are *measured* from the simulation, not asserted, and the script asserts
them before saving. If the parameters ever change, the labels stay honest or the run fails.
"""
import pathlib
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, next(str(p / "tools") for p in pathlib.Path(__file__).resolve().parents
                        if (p / "tools" / "figstyle.py").exists()))
import figstyle

N_HILL, K_DECAY, T_END, DT = 6, 1.0, 60.0, 0.002


def simulate(tau, x0=0.3):
    """RK4 on a fixed grid; the delayed value is held constant across each step."""
    steps, lag = int(T_END / DT), int(round(tau / DT))
    x = np.empty(steps + 1)
    x[0] = x0
    for i in range(steps):
        x_delayed = x[max(i - lag, 0)]                 # x(t - tau), or x0 before t = tau
        production = 1.0 / (1.0 + x_delayed ** N_HILL)
        f = lambda v: production - K_DECAY * v
        k1 = f(x[i])
        k2 = f(x[i] + DT / 2 * k1)
        k3 = f(x[i] + DT / 2 * k2)
        k4 = f(x[i] + DT * k3)
        x[i + 1] = x[i] + DT / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.arange(steps + 1) * DT, x


def late_amplitude(x):
    """Peak-to-trough over the last 30% of the run — zero if it has settled."""
    tail = x[int(0.7 * len(x)):]
    return tail.max() - tail.min()


def main():
    figstyle.use(width=7.6, height=3.2)
    fig, axes = plt.subplots(1, 3, sharey=True)
    cases = [(0.0, "No lag — settles"),
             (3.0, "Some lag — rings, then settles"),
             (8.0, "More lag — never settles")]

    amplitudes = []
    for ax, (tau, label) in zip(axes, cases):
        t, x = simulate(tau)
        amp = late_amplitude(x)
        amplitudes.append(amp)
        ax.plot(t, x, color=figstyle.SERIES[0])
        ax.set_title(f"{label}\nlag $\\tau$ = {tau:g}", fontsize=10.5, pad=8)
        ax.set_xlabel("time (arbitrary units)")
        ax.set_ylim(0, 1.15)

    # the labels above are claims about the simulation; check them
    assert amplitudes[0] < 1e-3, f"panel 1 should settle, amplitude {amplitudes[0]:.4f}"
    assert amplitudes[1] < 1e-2, f"panel 2 should settle, amplitude {amplitudes[1]:.4f}"
    assert amplitudes[2] > 0.2, f"panel 3 should oscillate, amplitude {amplitudes[2]:.4f}"

    axes[0].set_ylabel("output concentration")
    fig.subplots_adjust(top=0.74)
    fig.suptitle("The same negative feedback loop, with more lag each time",
                 color=figstyle.NAVY, fontweight="bold", fontsize=12.5, x=0.008, y=0.99, ha="left")
    fig.text(0.008, -0.06,
             "Only the delay changes. The loop, its strength, and every rate constant are identical "
             "in all three panels.",
             color=figstyle.MUTED, fontsize=9.5)

    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l01-feedback-lag.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    print(f"{out}  (late amplitudes: {', '.join(f'{a:.4f}' for a in amplitudes)})")


if __name__ == "__main__":
    main()
