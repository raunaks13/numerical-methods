"""
Write a python code to plot the phase space of the driven harmonic oscillator d2xdt2+γdxdt+ω20x=f0cos(ωt) upto time t=tfinal. 

Use leap frog scheme with time step Δt and initial conditions x(t=0)=x0 and dxdt(t=0)=v0 . 

The phase space plot is obtained by plotting position vs momentum. Here this is equivalent to the plot of x vs dxdt.

Use the following parameters to obtain the plot:
 γ=0.001, ω0=1.0, f0=1.0, Δt=0.01, tfinal=10.0, x0=0.05, v0=0.2, and ω=3.0.

"""

#!/usr/bin/python
from pylab import *
import prutorlib as pl
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
from pylab import rcParams
rcParams['figure.figsize'] = 6,5
###############################################################################
## put your code here

gamma = 0.001
w0 = 1
f0 = 1
delta = 0.01
tfinal = 10
x0 = 0.05
v0 = 0.2
w = 3

def f(x, v, t):
    return f0*np.cos(w*t) - x*w0**2 - gamma*v
    
n = int(round(tfinal/delta))+1
ts = np.linspace(0, tfinal, n)
xs = np.zeros((n))
vs = np.zeros((n))

xs[0] = x0
vs[0] = v0 + delta*f(x0, v0, 0)/2

for i in range(n-1):
    xs[i+1] = xs[i] + delta*vs[i]
    vs[i+1] = vs[i] + delta*f(xs[i+1], vs[i+1], ts[i+1])

x2 = xs
v2 = vs

############################################################################
plt.figure()
plt.plot(x2,v2)
plt.xlabel(r'$x$')
plt.ylabel(r'$p$')
pl.plot(plt, 'plot1d.pdf')