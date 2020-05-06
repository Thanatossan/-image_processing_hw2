from scipy.fft import fft2, ifft2, fft
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy
import numpy as np
import math


def check(value):
    if(value <= 0):
        return 0
    else:
        value = math.sqrt(value)
        if value > 255:
            return 255
        else:
            return value


filename = "./image/Cross.pgm"
col = 0
row = 0
converted_img = []
mattrix_img = []
converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)
padded_img = []
for i in range(256):
    padded_img_inloop = []
    for j in range(256):
        padded_img_inloop.append(0)
    padded_img.append(padded_img_inloop)
for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        padded_img[28+i][28+j] = mattrix_img[i][j]

# shift
for i in range(len(padded_img)):
    for j in range(len(padded_img[i])):
        padded_img[i][j] = padded_img[i][j] * pow(-1, i+j)

fourier_transform = fft2(padded_img)
copy_img = fft2(padded_img)
copy_img = np.angle(copy_img)
copy_img = copy_img.tolist()
fourier_transform = fourier_transform.tolist()


for i in range(len(fourier_transform)):
    for j in range(len(fourier_transform[i])):
        # copy_img[i][j] = check2(
        #     fourier_transform[i][j].imag, fourier_transform[i][j].real)
        value = abs(fourier_transform[i][j])

        # fourier_transform[i][j] = int(check(value))
        fourier_transform[i][j] = check(value)


wirefile = "output1_1_spectrum.pgm"
writepgm(wirefile, fourier_transform, 256, 256)

for i in range(len(copy_img)):
    for j in range(len(copy_img[i])):
        copy_img[i][j] = copy_img[i][j]*100
        if(copy_img[i][j] <= 0):
            copy_img[i][j] = 0
        elif(copy_img[i][j] > 255):
            copy_img[i][j] = 255
# print(copy_img)

wirefile = "output1_1_phase.pgm"
writepgm(wirefile, copy_img, 256, 256)

# for i in range(len(fourier_transform)):
#     for j in range(len(fourier_transform[i])):

#         # fourier_transform[i][j] = int(check(value))
#         fourier_transform[i][j] = math.atan(fourier_transform[i][j])

# wirefile = "output1_2.pgm"
# writepgm(wirefile, fourier_transform, 256, 256)
