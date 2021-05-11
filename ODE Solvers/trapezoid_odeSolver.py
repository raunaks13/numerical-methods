"""
Write a python code to solve the differential equation dxdt+αx=0, where α>0. 

Use Trapezoid method with time step, Δt to find the value of x(t) at given t=tfinal for a given initial condition x(t=0)=xinit. 

The input will be provided in four lines containing xinit, α, tfinal, and  Δt respectively. 

Round the answer to two decimal places using the Python function round() as below:
ans = round(ans, 2)
"""

import numpy as np

x_init = float(input())
alpha = float(input())
tfinal = float(input())
delta = float(input())

def f(x):
    return -alpha*x

n = int(round(tfinal/delta)) + 1
ts = np.linspace(0, tfinal, n)
xs = np.zeros((n))
xs[0] = x_init

for i in range(n-1):
    xs[i+1] = xs[i]*(1-(alpha*delta)/2)/(1+(alpha*delta)/2)
    
print(round(xs[n-1], 2))