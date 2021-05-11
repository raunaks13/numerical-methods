"""
Write a python code to solve the differential equation dxdt=x−2t2+1 using Predictor-Corrector scheme with time step, 
Δt to find the value of x(t) at given t=tfinal for a given initial condition x(t=0)=xinit. 

The input will be provided in three lines containing xinit, tfinal, and  Δt respectively. 
"""

import numpy as np

x_init = float(input())
tfinal = float(input())
delta = float(input())

def f(x, t):
    return x - 2*t**2 + 1

n = int(round(tfinal/delta))+1
ts = np.linspace(0, tfinal, n)
xs = np.zeros((n))
xs[0] = x_init

for i in range(n-1):
    x_star = xs[i] + delta*f(xs[i], ts[i])
    xs[i+1] = xs[i] +0.5*delta*(f(xs[i], ts[i]) + f(x_star, ts[i+1]))

print(round(xs[n-1], 2))