"""
Write a python program to solve the  1D nondimensionalized Schrödinger equation for a Harmonic oscillator numerically. 
The nondimensionalized Schrodinger equation is-
                          
i∂ψ/∂t=−1/2 ∂2ψ/∂x2 + 1/2 x^2

Solve the PDE using RK2 method for time stepping and central difference scheme for derivative 
over box size 2π with 101 grid points. 
Estimate the appropriate time step dt and discritized the domain properly for solving the equation. 

Use Gaussian wave packet as initial condition - 
                                           
ψ(x,0)=12‾√π−14e−x22[1+2‾√x]

Plot the solution |ψ(x,t)|2 from your simulation at times t=0.0 and 1.0 in a single frame. 
For plotting use prutorlib library to generate the link of the plot on Prutor. 

Note: There are not any test cases for this problem.
"""

import numpy as np
import matplotlib.pyplot as plt

tf = 2
dt = 0.0001
nsteps = int(tf/dt)

L = 6*np.pi
N = 101
h = L/N

j = np.arange(0,N)
x = j*h - L/2 + h

init_f = (1/np.sqrt(2))*np.pi**(-0.25)*np.exp(-(x**2)/2)*(1+np.sqrt(2)*x)
R = np.zeros(N+2)
R[1:N+1] = np.real(init_f)
R[0] = np.real(init_f[-1])
R[N+1] = np.real(init_f[0])

I = np.zeros(N+2)
I[1:N+1] = np.imag(init_f)
I[0] = np.imag(init_f[-1])
I[N+1] = np.imag(init_f[0])

y = R[1:-1]**2 + I[1:-1]**2

plt.plot(x, y, label=0)
mR = np.zeros(N+2)
mI = np.zeros(N+2)

for time_ind in range(nsteps+2):
    mR[1:N+1] = R[1:N+1] - (dt/(4*h**2))*(I[2:N+2] - 2*I[1:N+1] + I[0:N]) + dt*(1/4)*x[0:N]**2*I[1:N+1]
    mR[0] = mR[N]
    mR[-1] = mR[1]

    mI[1:N+1] = I[1:N+1] + (dt/(4*h**2))*(R[2:N+2] - 2*R[1:N+1] + R[0:N]) - dt*(1/4)*x[0:N]**2*R[1:N+1]
    mI[0] = mI[N]
    mI[-1] = mI[1]

    R[1:N+1] = R[1:N+1] - (dt/(2*h**2))*(mI[2:N+2] - 2*mI[1:N+1] + mI[0:N]) + dt*(1/2)*x[0:N]**2*mI[1:N+1]
    R[0] = R[N]
    R[-1] = R[1]

    I[1:N+1] = I[1:N+1] + (dt/(2*h**2))*(mR[2:N+2] - 2*mR[1:N+1] + mR[0:N]) - dt*(1/2)*x[0:N]**2*mR[1:N+1]
    I[0] = I[N]
    I[-1] = I[1]

R[1:N+1] = R[1:N+1] - (dt/(4*h**2))*(I[2:N+2] - 2*I[1:N+1] + I[0:N]) + (dt/2)*(1/2)*x[0:N]**2*I[1:N+1]
R[0] = R[N]
R[-1] = R[1]

y = R[1:-1]**2 + I[1:-1]**2

plt.plot(x, y, label=2)
plt.legend(loc="best")
plt.xlim(min(x),max(x))
plt.grid()
plt.xlabel("x")
plt.ylabel("$\|psi(x,t)|^2$")
plt.legend(loc="best")
plt.title("Linear Harmonic Oscillator")
plt.show()
