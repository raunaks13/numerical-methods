"""
d2y/dx2 = 6x, y(1) = 2, y(2) = 9
"""

import numpy as np
import matplotlib.pyplot as plt

eps = 1e-4
dt = 0.001
xend = 2
xstart = 1
y_end_true = 9

N = int((xend - xstart)/dt) + 1
xs = np.linspace(xstart, xend, N)

def euler_method(y_start):
    y = np.zeros((N, 2)) # column 1 = y, column 2 = y'

    y[0, 0] = y_start[0]
    y[0, 1] = y_start[1]
    for i in range(1, N):
        y[i, 0] = y[i-1, 0] + dt*y[i-1, 1] # update y
        y[i, 1] = y[i-1, 1] + dt*(6*xs[i-1]) # update y'
    
    return y

slope_undershoot = 0.1
y_start = np.array([2, slope_undershoot])
y = euler_method(y_start)
plt.plot(xs, y[:, 0], 'r--')

slope_overshoot = 11
y_start = np.array([2, slope_overshoot])
y = euler_method(y_start)
plt.plot(xs, y[:, 0], 'g--')

for i in range(500):
    if abs(y[-1, 0] - y_end_true) < eps:
        break

    slope_mid = (slope_undershoot + slope_overshoot)/2
    y_start = np.array([2, slope_mid])
    y = euler_method(y_start)

    if y[-1, 0] > y_end_true:
        slope_overshoot = slope_mid
    else:
        slope_undershoot = slope_mid

plt.plot(xs, y[:, 0], label='solution')
plt.plot(xs, (xs**3) + 1)
plt.grid()
plt.show()

