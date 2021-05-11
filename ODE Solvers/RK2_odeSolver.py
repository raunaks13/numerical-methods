"""
Write a python code to solve the differential equation of the damped Duffing oscillator d2xdt2+kdxdt−x+x3=0 (here k>0). 

Use second order Runge-Kutta (RK2) scheme with time step Δt, initial conditions x(t=0)=x0 and dxdt(t=0)=v0  to 
find the value of x(t) and v(t) i,e (\frac{dx}{dt})(t) at given t = t_final. 

The input will be provided in five lines containing x0, v0, k, tfinal and Δt respectively. 

The output will contain two lines. In the first line it will print x(t=tfinal) and in the second line it will print v(t=tfinal).

Round the answer to two decimal places using the Python function round() as below:
ans = round(ans, 2)
"""

import numpy as np

x0 = float(input())
v0 = float(input())
k = float(input())
tfinal = float(input())
delta = float(input())

def f(x, v):
    return -k*v + x - x**3

n = int(round(tfinal/delta))+1
ts = np.linspace(0, tfinal, n)
xs = np.zeros((n))
vs = np.zeros((n))
vs[0] = v0
xs[0] = x0

for i in range(n-1):
    j1 = delta*f(xs[i], vs[i])
    k1 = delta*vs[i]
    j2 = delta*f(xs[i]+k1/2, vs[i]+j1/2)
    k2 = delta*(vs[i]+j2/2)
    
    vs[i+1] = vs[i] + j2
    xs[i+1] = xs[i] + k2
    
print(round(xs[n-1], 2))
print(round(vs[n-1], 2))