"""
The third wavefunction of the Hydrogen atom, is written as,
		
Ψ300(r)=181(3πa3)1/2(27−18ra+2r2a2)exp(−r3a)

		
Use the five-point Laguerre-Gauss quadrature rule to evaluate the following integration up to two decimal places
∫∞04πr2|Ψ300(r)|2dr,

and print it as an output from your code. 

Note that you may need to scale the coordinate r properly (in your notebook) to use the 
Laguerre-Gauss quadrature rule for integration. 

Round off your answer up to two decimal places using python round function as below: 
ans = round(ans, 2)
"""

import numpy as np

def f(r):
    return 1/18*(3*r - 3*r**2 + 1/2*r**3)**2 # after simplifying the integral

ws = np.array([0.521756, 0.398667, 0.0759424, 0.00361176, 0.00002337])
xs = np.array([0.26356, 1.4134, 3.59643, 7.08581, 12.6408])

ys = f(xs)

print(round(np.dot(ws, ys), 2))