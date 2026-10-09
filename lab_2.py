"""
lab_2.py
Numerisk modell og analyse av rullende kule på krum bane.
TFY4106 / TFY4125 Fysikk - Institutt for fysikk, NTNU.
Gruppe 3: Adrian Andersen, Thomas Neegård, Håkon Asheim,
         Filip Gløckner, Hilmar Holmen-Løkke, Anna Hødnebø.
Høst 2026.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ==========================================
# 1. Fysiske parametere og konstanter
# ==========================================
g = 9.81           # Tyngdeakselerasjon [m/s^2]
m = 0.031          # Kulas masse [kg] (31 g)
r = 0.011          # Kulas radius [m] (11 mm)
c = 2.0 / 5.0      # Treghetsmomentfaktor for kompakt kule (I = c*m*r^2)

# Målte festepunkter (de 8 skruene på banen) i meter
x_screws = np.array([0, 200, 400, 600, 800, 1000, 1200, 1400]) * 1e-3
y_screws = np.array([300, 258, 172, 175, 242, 256, 203, 190]) * 1e-3

# ==========================================
# 2. Baneprofil via kubisk spline
# ==========================================
# Naturlige randbetingelser: y''(x_0) = y''(x_end) = 0
cs = CubicSpline(x_screws, y_screws, bc_type='natural')

# Diskretisering av banen med oppløsning dx = 1 mm
x = np.linspace(0.0, 1.4, 1401)
dx = x[1] - x[0]

y = cs(x)
d1 = cs(x, 1)      # Førstederivert y'(x)
d2 = cs(x, 2)      # Andrederivert y''(x)

# Helningsvinkel beta(x) og krumning kappa(x)
beta = np.arctan(d1)
kappa = d2 / ((1.0 + d1**2)**1.5)

# ==========================================
# 3. Teoretisk hastighet og rulletid
# ==========================================
# Energibevaring: m*g*y0 = m*g*y + 0.5*(1+c)*m*v^2
y0 = y[0]
v = np.sqrt(2 * g * (y0 - y) / (1.0 + c))
vx = v * np.cos(beta)

# Numerisk tidsintegrasjon: dt = dx / v_x
dt = np.zeros_like(x)
dt[0] = 0.0
# Første intervall fra ro med konstant akselerasjon:
dt[1] = 2.0 * dx / vx[1]
# Resterende intervaller med trapesapproksimasjon:
for i in range(2, len(x)):
    dt[i] = 2.0 * dx / (vx[i - 1] + vx[i])

t = np.cumsum(dt)

# ==========================================
# 4. Dynamiske krefter og sklibetingelse
# ==========================================
# Normalkraft N(x) = m * (g * cos(beta) + v^2 * kappa)
N_kraft = m * (g * np.cos(beta) + (v**2) * kappa)

# Statisk friksjonskraft f(x) = -(c / (1+c)) * m * g * sin(beta)
f_friksjon = -(c / (1.0 + c)) * m * g * np.sin(beta)

# Friksjonsforhold |f/N|
f_over_N = np.abs(f_friksjon / N_kraft)

# ==========================================
# 5. Energier i den ideelle modellen
# ==========================================
E_pot = m * g * y
E_kin = 0.5 * (1.0 + c) * m * (v**2)
E_mek = E_pot + E_kin

# ==========================================
# 6. Utskrift av teoretiske nøkkelstørrelser
# ==========================================
print("----------------- RESULTATER FOR RAPPORTEN -----------------")
print(f"Teoretisk rulletid:       {t[-1]:.3f} s")
print(f"Teoretisk sluttfart:      {v[-1]:.3f} m/s")
print(f"Teoretisk mekanisk energi:{E_mek[0]:.5f} J")
print(f"Maksimal |f/N|:           {np.max(f_over_N):.3f}")
print(f"Maksimal friksjonskraft:  {np.max(np.abs(f_friksjon)):.4f} N")
print(f"Maksimal normalkraft:     {np.max(N_kraft):.4f} N")
print(f"Minimal normalkraft:      {np.min(N_kraft):.4f} N")
print("------------------------------------------------------------")
