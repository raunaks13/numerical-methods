"""
Write a program to calculate the approximate value of the integral ∫ba(x^6−5x^5+3)dx using Trapezoidal rule. 
Divide the integration interval into N number of segments of equal width. The values of a, b and N will be specified as input.
				
The input will consist of three lines, with the first and second lines specifying a and b respectively. 
The third line will contain the value for N.
"""

a = float(input())
b = float(input())
N = int(input())

def f(x):
    ans = x**6 - 5*x**5 + 3
    return ans

h = (b-a)/N

sum = 0
for i in range(N):
    sum += h/2*(f(a+i*h) + f(a+(i+1)*h))
    
print(round(sum, 2))