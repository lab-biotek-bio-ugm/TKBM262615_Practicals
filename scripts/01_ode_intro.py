"""L01 — Pengantar Model Dinamis / Introduction to Dynamic Models.

Simulasi model populasi sederhana dengan scipy.integrate.solve_ivp:
pertumbuhan eksponensial vs logistik, dan model lahir-degradasi.

Referensi:
  - Ingalls (2013) Bab 1-2
  - Swain, Practical Systems Biology notes, sec. 2.1 (chemical rate equations)
  - https://swainlab.bio.ed.ac.uk/psb/lectures/notes.pdf

Cara menjalankan:
  python code/01_ode_intro.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- Model 1: pertumbuhan eksponensial dN/dt = r N ---
def exp_model(t, N, r):
    return r * N

# --- Model 2: logistik dN/dt = r N (1 - N/K) ---
def logistic_model(t, N, r, K):
    return r * N * (1 - N / K)

# --- Model 3: lahir-degradasi dx/dt = k_in - k_deg x ---
def birth_death(t, x, k_in, k_deg):
    return k_in - k_deg * x

r, K = 0.5, 100.0          # parameter logistik
t_eval = np.linspace(0, 10, 400)

sol_exp = solve_ivp(exp_model, (0, 10), [1.0], t_eval=t_eval, args=(r,))
sol_log = solve_ivp(logistic_model, (0, 10), [1.0], t_eval=t_eval, args=(r, K))
sol_bd = solve_ivp(birth_death, (0, 10), [0.0], t_eval=t_eval, args=(2.0, 0.5))

fig, axes = plt.subplots(1, 3, figsize=(13, 4))
axes[0].plot(sol_exp.t, sol_exp.y[0])
axes[0].set_title("Eksponensial $dN/dt = rN$")
axes[1].plot(sol_log.t, sol_log.y[0])
axes[1].set_title(f"Logistik (K = {K})")
axes[2].plot(sol_bd.t, sol_bd.y[0])
axes[2].set_title("Lahir-degradasi")
for ax in axes:
    ax.set_xlabel("waktu t")
    ax.grid(alpha=0.3)
plt.tight_layout()

print(f"Steady state logistik   : N(K) -> {K}")
print(f"Steady state lahir-deg  : x_ss = k_in/k_deg = {2.0/0.5}")
print("Lihat jendela plot; tutup jendela untuk mengakhiri skrip.")

plt.show()
