"""
Uses 3 point central scheme for calculating derivative on RHS
"""

import numpy as np
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
########## code here

c = 1
delta = 0.0001
L = 5
N = 1000
h = L/N
tfinal = 3

xs = np.linspace(0, L, N)

init = np.exp(-32*(xs-4)**2)
f = np.zeros((N+2))
f_mid = np.zeros((N+2))

f[1:N+1] = init
f[0] = f[N]
f[-1] = f[1]

writeint = 0
t = 0

while t <= tfinal:
    # RK2
    f_mid[1:N+1] = f[1:N+1] - (c*delta/(4*h))*(f[2:N+2] - f[0:N])
    f_mid[0] = f_mid[N]
    f_mid[-1] = f_mid[1]
    
    f[1:N+1] = f[1:N+1] - (c*delta/(2*h))*(f_mid[2:N+2] - f_mid[0:N])
    f[0] = f[N]
    f[-1] = f[1]

    # Upwind (euler backward) - stable
    # f[1:N+1] = f[1:N+1] - (c*delta/h)*(f_mid[1:N+1] - f_mid[0:N])
    # f[0] = f[N]
    # f[-1] = f[1]
    
    # Central Diff + Euler Forward (unstable)
    # f[1:N+1] = f[1:N+1] - (c*delta/(2*h))*(f_mid[2:N+2] - f_mid[0:N])
    # f[0] = f[N]
    # f[-1] = f[1]

    t = np.round(t, 5)
    
    if t >= writeint:
        plt.plot(xs, f[1:N+1], label='t={}'.format(round(t, 2)))
        plt.xlabel('x')
        plt.ylabel('psi(x, t)')
        plt.grid()
        plt.legend()
        writeint += 1
    
    t += delta

plt.show()