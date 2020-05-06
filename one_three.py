from scipy.fft import fft2, ifft2
from scipy import ndimage
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy, Bilinear, checkfft
import numpy as np
import math

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
rotated = (ndimage.rotate(mattrix_img, 30, reshape=False)).tolist()
copy_rotate = copy(rotated)
wirefile = "output1_3_original.pgm"
writepgm(wirefile, rotated, 200, 200)

for i in range(len(copy_rotate)):
    for j in range(len(copy_rotate[i])):
        padded_img[28+i][28+j] = copy_rotate[i][j]
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
        fourier_transform[i][j] = checkfft(value)


wirefile = "output1_3_spectrum.pgm"
writepgm(wirefile, fourier_transform, 256, 256)

for i in range(len(copy_img)):
    for j in range(len(copy_img[i])):
        copy_img[i][j] = copy_img[i][j]*100
        if(copy_img[i][j] <= 0):
            copy_img[i][j] = 0
        elif(copy_img[i][j] > 255):
            copy_img[i][j] = 255
# print(copy_img)

wirefile = "output1_3_phase.pgm"
writepgm(wirefile, copy_img, 256, 256)
