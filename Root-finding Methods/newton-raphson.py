import numpy as np

def f(x):
    return np.exp(x) - 6
    
for i in range(1,N):
    x[i] = x[i-1] - f(x[i-1])/np.exp(x[i-1])

    if (abs(x[i]-x[i-1]) < eps):
        break
    
print ("estimated root ", x[i])