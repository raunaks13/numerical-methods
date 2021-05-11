"""
Consider the function, z(x,y)=12(x2+y2) on xy-plane in the interval 0≤x≤1 and  0≤y≤1. 
Divide these intervals in ten equally spaced points in each direction. 

Write a python program to estimate the value of the function, z(x,y) at some point (x0,y0) using Lagrange interpolation. 
Take (x0,y0) as your input and print z(x0,y0) as your output. 

Also, your input must consist of two lines where the first line specifies x0 and the next line y0. 
Round off your result up to 3 decimal places.
"""

import numpy as np

x0 = float(input())
y0 = float(input())

xs = np.linspace(0, 1, 10)
ys = np.linspace(0, 1, 10)

z = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        z[i][j] = (xs[i]**2 + ys[j]**2)/2

final = 0
for i in range(10):
    for j in range(10):
        l = 1
        for k in range(10):
            if i != k:
                l *= (x0 - xs[k])/(xs[i] - xs[k])
            if j != k:
                l *= (y0 - ys[k])/(ys[j] - ys[k])
    
        final += z[i][j]*l

print(round(final, 3))
