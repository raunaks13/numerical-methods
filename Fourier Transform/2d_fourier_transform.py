"""
Evaluate the above expression over a square grid of 64×64 points with limits (0≤x≤2π) and (0≤y≤2π). 
Use A=256. Then use NumPy's fft2() function to obtain its 2D Fourier transform.

For a given input pair of wave-numbers, kx,ky, calculate 
and print the corresponding absolute value of the Fourier amplitude.

Note that since, you are solving in the interval [0,2π]×[0,2π], your input wavenumber kx and ky 
will be integer (may be positive/negative). 
"""

import numpy as np

A = 256
N = 64
kx = int(input())
ky = int(input())

def f(x, y):
    return A*(np.sin(x)**2)*(np.cos(2*y)**3)

xs = np.arange(0, 2*np.pi, 2*np.pi/N)
ys = xs

func = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        func[i][j] = f(xs[i], ys[j])

ft = np.fft.fft2(func)/(N**2)
print(round(abs(ft[kx][ky]), 2))