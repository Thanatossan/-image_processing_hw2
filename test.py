from scipy.fft import fft2, ifft2, fft, ifft
import math
import numpy as np
x = fft2([[0], [0], [255], [0], [0]])

x = x.tolist()
print(np.angle(x))
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = math.atan(x[i][j].real / x[i][j].imag)
print(x)
