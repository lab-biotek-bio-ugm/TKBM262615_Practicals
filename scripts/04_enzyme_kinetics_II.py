"""L04 — Kinematika Enzim II / Enzyme Kinetics II.

Inhibisi kompetitif dan non-kompetitif, regulasi alosterik dan kooperatif,
fungsi Hill (bentuk aktivasi/"kompetitif" dan represi/"non-kompetitif") sebagai
model regulasi, serta kinematika sigmoidal sebagai "soft switch".

Referensi:
  - Ingalls (2013) Bab 3 (inhibisi enzim, kooperativitas, persamaan Hill)
  - Alon (2006) Bab 2 (fungsi Hill sebagai fungsi input aktivator/represor)
  - Swain, PSB notes (bagian kinematika enzim)

Cara menjalankan:
  python scripts/04_enzyme_kinetics_II.py
"""

import numpy as np
import matplotlib.pyplot as plt

Vmax, KM, Ki = 10.0, 5.0, 2.0
S = np.linspace(0, 50, 400)

# --- Inhibisi kompetitif: KM_app naik, Vmax tetap ---
def v_competitive(S, I):
    KM_app = KM * (1 + I / Ki)
    return Vmax * S / (KM_app + S)

# --- Inhibisi non-kompetitif: Vmax_app turun, KM tetap ---
def v_noncompetitive(S, I):
    Vmax_app = Vmax / (1 + I / Ki)
    return Vmax_app * S / (KM + S)

I_values = [0, 2, 6, 20]
for I in I_values:
    print(f"I={I:5.1f}: kompetitif KM_app={KM * (1 + I / Ki):5.2f}, Vmax_app={Vmax:5.2f}"
          f"  |  non-kompetitif KM_app={KM:5.2f}, Vmax_app={Vmax / (1 + I / Ki):5.2f}")

# --- Fungsi Hill: aktivasi (sigmoid naik) dan represi (sigmoid turun) ---
def hill_activation(S, n, K=KM):
    return Vmax * S**n / (K**n + S**n)

def hill_repression(S, n, K=KM):
    return Vmax * K**n / (K**n + S**n)

n_values = [1, 2, 4, 8]

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
for I in I_values:
    axes[0, 0].plot(S, v_competitive(S, I), label=f"I={I}")
axes[0, 0].set_title("Inhibisi kompetitif")
axes[0, 0].legend()

for I in I_values:
    axes[0, 1].plot(S, v_noncompetitive(S, I), label=f"I={I}")
axes[0, 1].set_title("Inhibisi non-kompetitif")
axes[0, 1].legend()

for n in n_values:
    axes[1, 0].plot(S, hill_activation(S, n), label=f"n={n}")
axes[1, 0].set_title("Fungsi Hill aktivasi (soft switch ON)")
axes[1, 0].legend()

for n in n_values:
    axes[1, 1].plot(S, hill_repression(S, n), label=f"n={n}")
axes[1, 1].set_title("Fungsi Hill represi (soft switch OFF)")
axes[1, 1].legend()

for ax in axes.flat:
    ax.set_xlabel("[S]")
    ax.set_ylabel("v")
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()
