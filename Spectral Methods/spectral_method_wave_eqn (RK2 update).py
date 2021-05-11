import numpy as np
import matplotlib.pyplot as plt

c = 1.5
N = 500
L = 2*np.pi
xs = np.linspace(0, L, N)

init_temp = np.exp(-32*(xs-2)**2)
ft = np.fft.fft(init_temp)

k = np.array(list(range(0, N//2+1)) + list(range(-N//2+1, 0)))*2*np.pi/L

dt = 0.001
tfinal = 2

t = 0
ft_mid = np.zeros(ft.shape)
prefactor = -np.complex(0, 1)*c*k*dt

while t <= tfinal:
    ft_mid = ft + (prefactor/2)*ft
    ft = ft + prefactor*ft_mid

    y = np.fft.ifft(ft)
    y[0] = y[-1]

    if t == 1:
        index = np.where(np.round(xs, 2) == 3.48)[0]
        print(t, np.round(np.real(y)[index], 2))

    t = np.round(t, 4)
    t += dt