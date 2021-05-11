"""
Write a python code to solve the differential equation dxdt=x+xt. Use Euler's forward scheme with time step, Δt to find the value of x(t) at given t=tfinal for a given initial condition x(t=0)=xinit. 

The input will be provided in three lines containing xinit, Δt and tfinal respectively. 

Round the answer to two decimal places using the Python function round() as below:
ans = round(ans, 2)
"""

import numpy as np

x_init = float(input())
delta = float(input())
tfinal = float(input())

def f(x, t):
    return x + x*t

n = int(round(tfinal/delta)) + 1
ts = np.linspace(0, tfinal, n)
xs = np.zeros((n))
xs[0] = x_init

for i in range(n-1):
    xs[i+1] = xs[i] + delta*f(xs[i], ts[i])

print(round(xs[n-1], 2))
