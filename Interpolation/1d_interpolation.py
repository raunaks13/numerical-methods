"""
Consider the following data of half-life (t12) vs. activity (A) of a radioactive sample.

t12(arbitrary unit)0,1,2,3,4
A(arbitrary unit)
100.0, 51.66, 26.41, 14.19, 6.45

Use Lagrange’s interpolation to compute A(t) for a given t. Take t as your input and print A(t) as the output. 
Your input must consist of one line. Round off your output to 3 decimal places.
"""

t = float(input())

a = [100, 51.66, 26.41, 14.19, 6.45]
ts = [0, 1, 2, 3, 4]

final = 0
for i in range(5):
    y = a[i]
    for j in range(5):
        if i != j:
            y *= (t - ts[j])/(ts[i] - ts[j])
    
    final += y

print(round(final, 3))