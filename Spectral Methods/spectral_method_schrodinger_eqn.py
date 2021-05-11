import numpy as np

"""
The Schrodinger equation is given by:
	
i∂ψ/∂t = −α∂2ψ/∂x2
	
Solve the above PDE over a domain x∈[0,60] for α=1.0 (divide the space into N=256 grid points), using second order 
Runge-Kutta (RK2) method for performing time integration. 
Calculate the required time-step dt, appropriately for solving the system. 

Use the following representation of a Gaussian wave packet as initial condition:
ψ(x,0)=exp{−5(x−4)2}sin(18x)

	
Plot the real part of the solution at times t=0.0,0.4,0.8 and 1.2, all in a single frame to show the progression 
of your solution with time. 

You can do this by calling the matplotlib's plot function repeatedly for each of the above times.
"""

## Libraries

import numpy as np
import matplotlib.pyplot as plt

# Grid in real plane
N = 64
L = 60
dx = L/N
xs = np.linspace(0, L, N)

ys = np.exp(-5*((xs-4)**2))*np.sin(18*xs)
# ys = np.exp(-2*(x-np.pi)**2)
ft = np.fft.fft(ys)
k = np.array(list(range(0, N//2+1))+list(range(-N//2+1, 0)))

k = k*2*np.pi/L

dt = 0.001
j = np.complex(0, 1)
tfinal = 1.2
writeint = 0

ft_mid = np.zeros(ft.shape)
t = 0
while t < tfinal:
    ft_mid = ft - j*(k**2)*dt*ft/2
    ft -= j*(k**2)*dt*ft_mid
    
    if t + dt/2 > writeint:
        y = np.fft.ifft(ft)
        plt.plot(xs, np.real(y), label='t={}'.format(round(t, 2)))
        plt.xlabel('x')
        plt.ylabel('Real part of psi(x, t)')
        plt.legend()
        writeint += 0.4
        
    t += dt