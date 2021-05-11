"""
finds roots of f(x)
"""

import numpy as np

def f(x):
    return a*x**3 + b*x**2 + c*x + d

a = float(input())
b = float(input())
c = float(input())
d = float(input())
upper = float(input())
lower = float(input())

eps = 0.001; N = 10

x = np.zeros(N)
x[0] = lower
x[1] = upper

for i in range(2,N):
    mid = (x[i-2] + x[i-1])/2
    
    if (abs(mid - x[i-1]) < eps):
        x[i] = mid
        break
    elif f(x[i-2])*f(mid) > 0:
        x[i] = mid
    else:
        x[i-1] = x[i-2]
        x[i] = mid
    
print("i, mid = ", i, mid)
print ("estimated root ", mid)