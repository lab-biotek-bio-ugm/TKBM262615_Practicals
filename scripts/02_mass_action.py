"""L02 — Jaringan Reaksi Kimia I / Chemical Reaction Networks I.

Hukum aksi massa: reaksi reversibel A <-> B dan dimerisasi 2R <-> R2,
termasuk pemeriksaan kekekalan massa.

Referensi:
  - Ingalls (2013) Bab 2
  - Swain, PSB notes, sec. 2.1-2.3 (rate equations, detailed balance, mass action)
  - Swain, PSB notes, sec. 2.1.1 (dimerisation)

Cara menjalankan:
  python code/02_mass_action.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Reaksi reversibel A <-> B ---
def reversible(t, y, kp, km):
    A, B = y
    dA = -kp * A + km * B
    dB = kp * A - km * B
    return [dA, dB]

# --- Dimerisasi 2R <-> R2 (perhatikan faktor 2 pada R) ---
def dimerisation(t, y, f, b):
    R, R2 = y
    dR = -2 * f * R**2 + 2 * b * R2
    dR2 = f * R**2 - b * R2
    return [dR, dR2]

kp, km = 0.8, 0.2          # konstanta maju/mundur (1/s)
A0, B0 = 1.0, 0.0
t_eval = np.linspace(0, 10, 400)

sol = solve_ivp(reversible, (0, 10), [A0, B0], t_eval=t_eval, args=(kp, km))
A, B = sol.y
print("Reversibel A <-> B:")
print(f"  Steady state B/A = kp/km = {kp/km:.2f}  |  hasil simulasi = {B[-1]/A[-1]:.2f}")
print(f"  Kekekalan massa  : A+B = {A0+B0:.2f} -> {A[-1]+B[-1]:.2f}")

f, b = 0.5, 0.1
R0, R20 = 1.0, 0.0
sol2 = solve_ivp(dimerisation, (0, 10), [R0, R20], t_eval=t_eval, args=(f, b))
R, R2 = sol2.y
# Konservasi: [R] + 2[R2] = konstanta
conserved = R + 2 * R2
print("\nDimerisasi 2R <-> R2:")
print(f"  Konservasi [R]+2[R2] : awal {R0+2*R20:.2f} -> akhir {conserved[-1]:.2f}")

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(sol.t, A, label="A")
axes[0].plot(sol.t, B, label="B")
axes[0].set_title("Reversibel A <-> B")
axes[0].legend()
axes[1].plot(sol2.t, R, label="R")
axes[1].plot(sol2.t, R2, label="R2")
axes[1].set_title("Dimerisasi 2R <-> R2")
axes[1].legend()
for ax in axes:
    ax.set_xlabel("waktu t")
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
