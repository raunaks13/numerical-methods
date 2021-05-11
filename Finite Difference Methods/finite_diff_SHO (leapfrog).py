import numpy as np

tf = 0.1
dt = 0.001
nsteps = int(tf/dt)

L = 2*np.pi
N = 101
h = L/N
j = np.arange(0,N)
x = j*h - L/2 + h

init_f = (np.pi**(-0.25))*np.exp(-(x**2)/2)*(1+np.sqrt(2)*x)/np.sqrt(2)

R = np.zeros(N+2)
R[1:N+1] = np.real(init_f)
R[0] = np.real(init_f[-1])
R[N+1] = np.real(init_f[0])

I = np.zeros(N+2)
I[1:N+1] = np.imag(init_f)
I[0] = np.imag(init_f[-1])
I[N+1] = np.imag(init_f[0])

I[1:N+1] = I[1:N+1] + (dt/(4*h**2))*(R[2:N+2] - 2*R[1:N+1] + R[0:N]) - (dt/2)*(1/2)*x[0:N]**2*R[1:N+1]
I[0] = I[N]
I[-1] = I[1]

t = 0
for time_ind in range(nsteps+2):
    R[1:N+1] = R[1:N+1] - (dt/(2*h**2))*(I[2:N+2] - 2*I[1:N+1] + I[0:N]) + dt*(1/2)*x[0:N]**2*I[1:N+1]
    R[0] = R[N]
    R[-1] = R[1]

    I[1:N+1] = I[1:N+1] + (dt/(2*h**2))*(R[2:N+2]-2*R[1:N+1]+R[0:N]) - dt*(1/2)*x[0:N]**2*R[1:N+1]
    I[0] = I[N]
    I[-1] = I[1]

R[1:N+1] = R[1:N+1] - (dt/(4*h**2))*(I[2:N+2] - 2*I[1:N+1] + I[0:N]) + (dt/2)*(1/2)*x[0:N]**2*I[1:N+1]
R[0] = R[N]
R[-1] = R[1]

y = R[1:-1]**2 + I[1:-1]**2

m = max(R[1:-1]**2 + I[1:-1]**2)
print(np.round(m, 2))
