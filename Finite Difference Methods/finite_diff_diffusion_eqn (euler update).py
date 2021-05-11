"""
Uses 3 point central scheme for 2nd derivative in RHS
"""

import numpy as np
# import prutorlib
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
######## code here

alpha = 0.5
delta = 0.0001
L = 10
N = 1000
h = L/N
tfinal = 4

xs = np.linspace(0, L, N)

init = np.exp(-5*(xs-5)*(xs-5))
f = np.zeros(N+2)

f[1:N+1] = init
f[0] = 1
f[N+1] = 0
writeint = 0
t = 0

while t <= tfinal:
    # Central Diff for 2nd der + Euler Fwd
    f[1:N+1] = f[1:N+1] + (delta*alpha)/(h**2)*(f[0:N]-2*f[1:N+1]+f[2:N+2])
    f[0] = 1
    f[N+1] = 0
    
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
# prutorlib.plot(matplotlib.pyplot, "output.png")