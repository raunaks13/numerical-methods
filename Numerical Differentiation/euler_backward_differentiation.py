import numpy as np

x_init = float(input())
delta = float(input())
tfinal = float(input())

def f(x, t):
    return x**2 - 0.1*x

n = int(round(tfinal/delta)) + 1
ts = np.linspace(0, tfinal, n)
xs = np.zeros((n))
xs[0] = x_init

for i in range(n-1):
    for k in range(5):
        xs[i+1] = xs[i] + delta*f(xs[i+1], ts[i+1])

print(round(xs[n-1], 2))