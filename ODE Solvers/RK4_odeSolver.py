"""
Consider an ideal gas at the absolute temperature T in a uniform gravitational field described by acceleration g. 
From the codition of hydrostatic equalibrium for a slice of gas located between heights z and z+dz, n(z)
(the number of molecules per cm3 at height z) can be obtained from the following differential equation,
	
dn(z)dz=−mgkTn(z)

Write a python code to solve this differential equation. 
Use Runge Kutta (RK4) scheme with step, Δz to find the value of n(z) at given z=zfinal for a given initial condition n(z=0)=n0.
	
The input will be provided in three lines containing n0, Δz and zfinal respectively. 
"""

import numpy as np

n0 = float(input())
deltaz = float(input())
zfinal = float(input())

def f(n):
    return -n

nos = int(round(zfinal/deltaz))+1

zs = np.linspace(0, zfinal, nos)
ns = np.zeros((nos))
ns[0] = n0

for i in range(nos-1):
    k1 = deltaz*f(ns[i])
    k2 = deltaz*f(ns[i]+k1/2)
    k3 = deltaz*f(ns[i]+k2/2)
    k4 = deltaz*f(ns[i]+k3)
    ns[i+1] = ns[i] + (k1+2*k2+2*k3+k4)/6

print(round(ns[nos-1], 2))