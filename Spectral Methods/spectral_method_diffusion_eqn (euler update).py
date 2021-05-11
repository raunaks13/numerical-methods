"""
Write a Python program to solve the 1D diffusion equation numerically using spectral method. 
The diffusion equation is written as:

∂ρ/∂t = α ∂2ρ/∂x2

Solve the above PDE over a domain x∈[0,20] for the case where α=1.0 (divide the space into 256 grid points). 
Use the forward Euler method for performing time-integration with dt=0.0001. 

Use the following function as initial condition for starting your time-integration,
ρ(x,0)=sin(πx)+sin(2πx)

with boundary condition,
ρ(0,t)=ρ(20,t)=0 for all t. 

Plot the real part of the solution from your simulation at times t = 0.0, 0.02, 0.04, 0.06, 0.08 and 0.10, 
all in a single frame.

You can do this by calling the matplotlib's plot function repeatedly for each of the above times 
and then at the end of the simulation, draw the plot into an output file using the prutorlib's plot function.
"""

import numpy as np
import matplotlib.pyplot as plt

# Grid in real plane
N = 256
L = 20
dx = L/N
xs = np.linspace(0, L, N)

ys = np.sin(np.pi*xs)+np.sin(2*np.pi*xs)
ys = np.exp(-2*(x-np.pi)**2)
ft = np.fft.fft(ys)
k = np.array(list(range(0, N//2+1)) + list(range(-N//2+1, 0)))

k = k*2*np.pi/L

dt = 0.0001
j = np.complex(0, 1)
tfinal = 0.1
limit = 0

t = 0
while t < tfinal:
    ft *= (1 - dt*(k**2))
    
    if t + dt > limit:
        y = np.fft.ifft(ft)
        y[0] = 0
        y[-1] = 0
        plt.plot(xs, np.real(y), label='t={}'.format(round(t, 2)))
        plt.xlabel('x')
        plt.ylabel('Real part of rho(x, t)')
        plt.legend()
        limit += 0.02
    t += dt