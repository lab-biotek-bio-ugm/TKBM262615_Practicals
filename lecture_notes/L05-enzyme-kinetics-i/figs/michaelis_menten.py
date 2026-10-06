#!/usr/bin/env python3
# /// script
# dependencies = ["numpy", "scipy", "matplotlib"]
# ///
"""L05 Figure -- the rate law, the assumption under it, and what the assumption costs.

Panel A reproduces Ingalls' Figure 3.4: v = Vmax*s/(KM+s), with the initial slope Vmax/KM and
the Vmax ceiling drawn in, and KM marked where the rate is exactly half-maximal. Both constants
are read off the curve, which is how they are measured.

Panel B is the evidence for the lecture's central claim. The QSSA replaces the differential
equation for the complex with an algebraic one, c_qss(s) = k1*eT*s/(k-1+k2+k1*s). Plotted here
against the true c(t) from the full mechanism, at the cell-like ratio eT = 0.1 mM against
s(0) = 5 mM: after a brief transient the algebraic formula tracks the real complex to about 2%
of the enzyme pool, and it does so by *moving* -- it rides on s(t), scaled and drawn underneath.
That movement is the thing students most often get wrong about the QSSA.

Panel C is the price. The reduced model has no complex to store substrate in, so its [S] runs
above the full mechanism's. The gap is sequestration and it scales with the enzyme pool. Time
is scaled by 1/eT so all three runs consume their substrate over the same horizontal span,
which makes the three gaps directly comparable rather than merely differently stretched.

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

K1, KM1, K2 = 30.0, 1.0, 10.0              # /mM/s, /s, /s      (Ingalls Figure 3.3)
ET_FIG = 1.0                               # mM, for the rate-law constants quoted on slides
VMAX = K2 * ET_FIG
KM = (KM1 + K2) / K1
S0 = 5.0                                   # mM
ET_PANEL_B = 0.1                           # mM -- the cell-like ratio s >> eT
ET_SWEEP = (1.0, 0.1, 0.01)                # mM


def mm_rate(s, vmax=VMAX):
    return vmax * s / (KM + s)


def c_qss(s, eT):
    """The algebraic replacement for dc/dt = 0. It depends on s, hence on t: not a constant."""
    return K1 * eT * s / (KM1 + K2 + K1 * s)


def full_mechanism(t, y, eT):
    s, c, p = y
    e = eT - c
    return [-K1 * s * e + KM1 * c, K1 * s * e - KM1 * c - K2 * c, K2 * c]


def reduced(t, y, eT):
    v = mm_rate(y[0], K2 * eT)
    return [-v, v]


def run(eT, t_end, n=2000):
    """Full mechanism and MM reduction on a shared mesh. -> (t, s_full, c_full, s_reduced)."""
    tol = dict(rtol=1e-11, atol=1e-14, dense_output=True)
    t = np.linspace(0, t_end, n)
    full = solve_ivp(full_mechanism, [0, t_end], [S0, 0.0, 0.0], args=(eT,), **tol)
    red = solve_ivp(reduced, [0, t_end], [S0, 0.0], args=(eT,), **tol)
    s_full, c_full, _ = full.sol(t)
    return t, s_full, c_full, red.sol(t)[0]


def main():
    figstyle.use(width=12.6, height=3.9)

    # ---------------------------------------------------------------- checks first
    assert abs(mm_rate(KM) - VMAX / 2) < 1e-12, "v(KM) must be exactly Vmax/2"

    # Panel B: does the algebraic formula track the true complex, and does it move?
    tb, sb, cb, _ = run(ET_PANEL_B, 6.0)
    qb = c_qss(sb, ET_PANEL_B)
    settled = tb > 0.3
    worst = np.max(np.abs(cb[settled] - qb[settled]))
    worst_pct = worst / ET_PANEL_B * 100
    swing_pct = (qb.max() - qb.min()) / ET_PANEL_B * 100
    assert worst_pct < 5, f"QSSA should track c(t) to a few % of eT; got {worst_pct:.2f}%"
    assert swing_pct > 40, f"c_qss must visibly move or the point is lost; swing {swing_pct:.0f}%"

    # Panel C: the sequestration gap, on time scaled by 1/eT so the runs are comparable
    sweep, gaps = {}, {}
    for eT in ET_SWEEP:
        t, s_full, _, s_red = run(eT, 1.0 / eT)
        sweep[eT] = (t * eT, s_red - s_full)              # scaled time, gap
        gaps[eT] = float(np.max(s_red - s_full))
    assert gaps[1.0] > 0.5, f"expected a visible gap at eT=1, got {gaps[1.0]:.4f}"
    assert gaps[0.01] < 0.02, f"expected the gap to vanish at eT=0.01, got {gaps[0.01]:.4f}"
    for big, small in ((1.0, 0.1), (0.1, 0.01)):
        r = gaps[big] / gaps[small]
        assert 5 < r < 15, f"the gap should scale roughly with eT; {big}/{small} ratio {r:.2f}"

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.subplots_adjust(wspace=0.34)

    # ---------------------------------------------------------------- A: the rate law
    s = np.linspace(0, 5, 500)
    ax1.plot(s, mm_rate(s), color=figstyle.SERIES[0], linewidth=2.4)
    near = np.linspace(0, 0.45, 50)          # the linear regime only, or it leaves the axes
    ax1.plot(near, VMAX / KM * near, color=figstyle.MUTED, linestyle=":", linewidth=1.6,
             label=r"initial slope $V_{max}/K_M$")
    ax1.axhline(VMAX, color=figstyle.MUTED, linestyle="--", linewidth=1.2,
                label=r"ceiling $V_{max}$")
    ax1.plot([KM], [VMAX / 2], "o", color=figstyle.INK, markersize=6, zorder=5)
    ax1.vlines(KM, 0, VMAX / 2, color=figstyle.INK, linewidth=0.9)
    ax1.hlines(VMAX / 2, 0, KM, color=figstyle.INK, linewidth=0.9)
    ax1.annotate(f"$K_M$ = {KM:.2f} mM,\nwhere v = $V_{{max}}$/2",
                 xy=(KM, VMAX / 2), xytext=(KM + 1.0, VMAX / 2 - 2.6), fontsize=9,
                 arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0))
    ax1.set_xlabel("substrate s (mM)")
    ax1.set_ylabel("rate v (mM/s)")
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0, VMAX * 1.18)
    ax1.legend(loc="center right", fontsize=9)
    ax1.set_title("A  Reading the two constants", pad=8)

    # ---------------------------------------------------------------- B: does the QSSA hold?
    ax2.plot(tb, sb / S0, color=figstyle.MUTED, linewidth=1.3, linestyle="-",
             label="s(t)/s(0), for reference")
    ax2.plot(tb, cb / ET_PANEL_B, color=figstyle.INK, linewidth=2.4,
             label="[C]/$e_T$, full mechanism")
    ax2.plot(tb, qb / ET_PANEL_B, color=figstyle.SERIES[3], linestyle="--", linewidth=2.2,
             label=r"$c^{qss}(s(t))/e_T$, algebraic")
    ax2.axvspan(0, 0.3, color=figstyle.SERIES[1], alpha=0.10)
    ax2.annotate("transient", xy=(0.15, 0.06), fontsize=9, color=figstyle.SERIES[1], ha="center")
    ax2.annotate(f"the two agree to {worst_pct:.1f}% of $e_T$",
                 xy=(3.4, qb[tb.searchsorted(3.4)] / ET_PANEL_B), xytext=(1.5, 0.42),
                 fontsize=9, arrowprops=dict(arrowstyle="->", color=figstyle.MUTED, lw=1.0))
    ax2.set_xlabel("time (s)")
    ax2.set_ylabel(r"fraction of enzyme as complex")
    ax2.set_xlim(0, 6)
    ax2.set_ylim(0, 1.12)
    ax2.legend(loc="upper right", fontsize=8.5)
    ax2.set_title(r"B  $c^{qss}$ is not a constant", pad=8)

    # ---------------------------------------------------------------- C: the price
    for eT, colour in zip(ET_SWEEP, (figstyle.SERIES[1], figstyle.SERIES[2], figstyle.SERIES[0])):
        ts, gap = sweep[eT]
        ax3.plot(ts, gap, color=colour, linewidth=2.0,
                 label=f"$e_T$ = {eT:g} mM   max {gaps[eT]:.3f}")
    ax3.set_xlabel(r"scaled time  $t \cdot e_T$  (mM$\cdot$s)")
    ax3.set_ylabel("[S] overcount: reduced $-$ full (mM)")
    ax3.set_xlim(0, 1)
    ax3.legend(loc="upper right", fontsize=9, title="substrate hidden inside C",
               title_fontsize=9)
    ax3.set_title("C  The error scales with $e_T$", pad=8)

    fig.suptitle("Michaelis-Menten: the curve, the assumption under it, and what it costs",
                 color=figstyle.NAVY, fontweight="bold", fontsize=12.5, x=0.005, y=1.03, ha="left")

    out = next(p for p in pathlib.Path(__file__).resolve().parents
               if (p / "tools").is_dir()) / "course/build/l05-michaelis-menten.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    print(f"{out}")
    print(f"  at eT={ET_FIG:g} mM:  Vmax={VMAX:g} mM/s   KM={KM:.4f} mM   kcat=k2={K2:g} /s")
    print(f"  panel B (eT={ET_PANEL_B:g}): worst |c - c_qss| after t=0.3 s = {worst:.5f} mM"
          f" ({worst_pct:.2f}% of eT);  c_qss swing {swing_pct:.0f}% of eT")
    for eT in ET_SWEEP:
        print(f"  eT={eT:<5g} max [S] overcount = {gaps[eT]:.4f} mM"
              f"  ({gaps[eT] / S0 * 100:.2f}% of s(0))")


if __name__ == "__main__":
    main()
