from scipy.fft import fft2, ifft2
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy, checkfft2, checkfft
import numpy as np
import math

filename1 = "./output_img/output1_1_spectrum.pgm"
filename2 = "./output_img/output1_1_phase.pgm"
col = 0
row = 0
converted_img = []
mattrix_img = []
converted_img, col, row = read_pgm(filename1, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)


for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        mattrix_img[i][j] = pow(mattrix_img[i][j], 2)
for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        mattrix_img[i][j] = mattrix_img[i][j] * pow(-1, i+j)
mattrix_img = (ifft2(mattrix_img)).tolist()
for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        # copy_img[i][j] = check2(
        #     fourier_transform[i][j].imag, fourier_transform[i][j].real)
        value = abs(mattrix_img[i][j])

        # fourier_transform[i][j] = int(check(value))
        mattrix_img[i][j] = checkfft2(value)

wirefile = "output1_5_spectrum.pgm"

writepgm(wirefile, mattrix_img, 256, 256)

converted_img2 = []
mattrix_img2 = []
converted_img2, col, row = read_pgm(filename2, col, row)
mattrix_img2 = list_to_2D_list(converted_img2, mattrix_img2, col, row)


for i in range(len(mattrix_img2)):
    for j in range(len(mattrix_img2[i])):
        mattrix_img2[i][j] = pow(mattrix_img2[i][j], 2)
for i in range(len(mattrix_img2)):
    for j in range(len(mattrix_img2[i])):
        mattrix_img2[i][j] = mattrix_img2[i][j] * pow(-1, i+j)
mattrix_img2 = (ifft2(mattrix_img2)).tolist()
for i in range(len(mattrix_img2)):
    for j in range(len(mattrix_img2[i])):
        # copy_img[i][j] = check2(
        #     fourier_transform[i][j].imag, fourier_transform[i][j].real)
        value = abs(mattrix_img2[i][j])

        # fourier_transform[i][j] = int(check(value))
        mattrix_img2[i][j] = checkfft(value)

wirefile2 = "output1_5_phase.pgm"

writepgm(wirefile2, mattrix_img2, 256, 256)
