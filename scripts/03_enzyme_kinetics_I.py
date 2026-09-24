"""L03 — Kinematika Enzim I / Enzyme Kinetics I.

Mekanisme enzim E + S <-> ES -> E + P, asumsi keadaan quasi-steady-state
(QSSA) untuk [ES], penurunan persamaan Michaelis-Menten, dan interpretasi
parameter Vmax dan KM.

Referensi:
  - Ingalls (2013) Bab 3 (kinematika enzim, QSSA, penurunan Michaelis-Menten)
  - Alon (2006) Bab 2 (relasi input-output, Michaelis-Menten)
  - Swain, PSB notes (bagian kinematika enzim)

Cara menjalankan:
  python scripts/03_enzyme_kinetics_I.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Mekanisme lengkap: E + S <-> ES -> E + P ---
def enzyme_full(t, y, k1, km1, kcat):
    E, S, ES, P = y
    v_f = k1 * E * S
    v_r = km1 * ES
    v_cat = kcat * ES
    dE = -v_f + v_r + v_cat
    dS = -v_f + v_r
    dES = v_f - v_r - v_cat
    dP = v_cat
    return [dE, dS, dES, dP]

k1, km1, kcat = 100.0, 50.0, 10.0   # 1/(uM s), 1/s, 1/s
Etot = 1.0                          # uM
KM = (km1 + kcat) / k1
Vmax = kcat * Etot
print(f"KM = {KM:.3f} uM, Vmax = {Vmax:.3f} uM/s")

# --- Kurva progres: S0 >> Etot, syarat QSSA terpenuhi ---
S0 = 100.0
t_eval = np.linspace(0, 15, 600)
sol = solve_ivp(enzyme_full, (0, 15), [Etot, S0, 0.0, 0.0],
                 t_eval=t_eval, args=(k1, km1, kcat), rtol=1e-8, atol=1e-10)
E, S, ES, P = sol.y

# Perbandingan [ES] hasil simulasi penuh vs pendekatan QSSA: ES = Etot*S/(KM+S)
ES_qssa = Etot * S / (KM + S)
# QSSA hanya berlaku setelah transien cepat awal (skala waktu ~1/(k1*S0+k-1+kcat));
# sebelum itu [ES] masih naik dari 0 menuju plateau-nya.
t_fast = 5.0 / (k1 * S0 + km1 + kcat)
after_transient = sol.t > 10 * t_fast
max_err_all = np.max(np.abs(ES - ES_qssa)) / Etot
max_err_after = np.max(np.abs(ES[after_transient] - ES_qssa[after_transient])) / Etot
print(f"Pemeriksaan QSSA (seluruh t, termasuk transien cepat awal): max error relatif = {max_err_all:.4f}")
print(f"Pemeriksaan QSSA (t > {10 * t_fast:.4f} s, setelah transien cepat): max error relatif = {max_err_after:.4f}")

# --- Laju awal v0(S0): tahan [S] tetap, integrasikan subsistem (E, ES) sampai
# mencapai keadaan tunak, lalu v0 = kcat*[ES]_tunak. Dibandingkan dengan kurva MM analitik. ---
def enzyme_fixed_S(t, y, k1, km1, kcat, S_val):
    E, ES = y
    v_f = k1 * E * S_val
    v_r = km1 * ES
    v_cat = kcat * ES
    return [-v_f + v_r + v_cat, v_f - v_r - v_cat]

def initial_rate(S0_val, t_ss=1.0):
    s = solve_ivp(enzyme_fixed_S, (0, t_ss), [Etot, 0.0],
                   args=(k1, km1, kcat, S0_val), rtol=1e-10, atol=1e-14)
    return kcat * s.y[1, -1]

S_values = np.logspace(-2, 2, 25)
v_sim = np.array([initial_rate(s) for s in S_values])
v_analytic = Vmax * S_values / (KM + S_values)
print(f"\nDi S = KM: v_simulasi = {initial_rate(KM):.3f} uM/s, Vmax/2 = {Vmax / 2:.3f} uM/s")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(sol.t, S, label="S")
axes[0].plot(sol.t, P, label="P")
axes[0].set_title("Kurva progres S(t), P(t)")
axes[0].legend()

axes[1].plot(sol.t, ES, label="[ES] penuh")
axes[1].plot(sol.t, ES_qssa, "--", label="[ES] QSSA")
axes[1].set_title("[ES]: simulasi penuh vs QSSA")
axes[1].legend()

axes[2].semilogx(S_values, v_sim, "o", label="v0 simulasi")
axes[2].semilogx(S_values, v_analytic, "-", label="Vmax S / (KM + S)")
axes[2].axhline(Vmax / 2, color="gray", ls=":", lw=1)
axes[2].axvline(KM, color="gray", ls=":", lw=1)
axes[2].set_title("Kurva Michaelis-Menten v0(S)")
axes[2].legend()

for ax in axes:
    ax.set_xlabel("waktu t" if ax is not axes[2] else "[S]")
    ax.grid(alpha=0.3)
axes[2].set_ylabel("v0")
plt.tight_layout()
plt.show()
