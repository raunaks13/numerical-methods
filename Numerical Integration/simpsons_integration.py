"""
Write a python program to calculate the value of the integral ∫π/40(acos(x)+bsin(x))dx using Simpson's 1/3 rule. 
Divide the integration interval into N segments of equal width. 

The value of a, b and N will be specified as input. Print your answer rounded off up to two decimal places.
				
The input will consist of three lines, with the first and second lines specifying a and b respectively. 
The third line will contain the value of N.
"""

import numpy as np
a = float(input())
b = float(input())
N = int(input())

def f(x):
    ans = a*np.cos(x) + b*np.sin(x)
    return ans

h = np.pi/(4*N)

res = 0
for i in range(0, N, 2):
    res += h/3*(f(i*h) + 4*f((i+1)*h) + f((i+2)*h))

print(round(res, 2))