"""
∂t u + u ∂x u = ν ∂2x u
"""

import numpy as np
import matplotlib.pyplot as plt

nu = 1
N = 64
L = 2*np.pi
h = L/N
xs = np.linspace(0, L, N) 

dt = 0.1
tfinal = 1

init_temp = np.sin(xs)
f = np.zeros(N+2)
f_mid = np.zeros(N+2)

f[1:N+1] = init_temp
f[0] = init_temp[-1]
f[N+1] = init_temp[0]

t = 0
while t <= tfinal:
    # Euler Fwd + (Upwind Scheme for nonlinear term, central difference for diffusion term)
    # for i in range(1, N+2):
    #     if f[i] > 0:
    #         f[i] = f[i] - (dt/h)*f[i]*(f[i] - f[i-1]) + nu*dt/(h**2)*(f[i+1] - 2*f[i] + f[i-1])
    #     elif f[i] < 0:
    #         f[i] = f[i] - (dt/h)*f[i]*(f[i+1] - f[i]) + nu*dt/(h**2)*(f[i+1] - 2*f[i] + f[i-1])

    # f[0] = f[N] 
    # f[-1] = f[1]
    
    # RK2 for nonlinear term, central difference for diffusion term
    for i in range(1, N+1):
        if f[i] > 0:
            f_mid[i] = f[i] - (dt/(2*h))*f[i]*(f[i] - f[i-1]) + nu*dt/(2*h**2)*(f[i-1] - 2*f[i] + f[i+1])
        else:
            f_mid[i] = f[i] - (dt/(2*h))*f[i]*(f[i+1] - f[i]) + nu*dt/(2*h**2)*(f[i-1] - 2*f[i] + f[i+1])

    f_mid[0] = f_mid[N]
    f_mid[-1] = f_mid[1]

    for i in range(1, N+1):
        if f[i] > 0:
            f[i] = f[i] + (dt/h)*f_mid[i]*(f_mid[i] - f_mid[i-1]) + nu*dt/(h**2)*(f_mid[i-1] - 2*f_mid[i] + f_mid[i+1])
        else:
            f[i] = f[i] + (dt/h)*f_mid[i]*(f_mid[i] - f_mid[i-1]) + nu*dt/(h**2)*(f_mid[i-1] - 2*f_mid[i] + f_mid[i+1])

    f[0] = f[N]
    f[-1] = f[1]

    t = np.round(t, 4)
    t += dt

plt.plot(xs, f)