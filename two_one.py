from scipy.fft import fft2, ifft2
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy, checkfft2, checkfft
import numpy as np
import math


def idel_filter(cutoff_freq, row, col, i, j):
    Duv = math.sqrt(pow(i-(row/2), 2) + pow(j-(col/2), 2))
    if Duv <= cutoff_freq:
        return 1
    else:
        return 0


def butter_filter(cutoff_freq, row, col, i, j):
    Duv = math.sqrt(pow(i-(row/2), 2) + pow(j-(col/2), 2))
    n = 2
    divider = 1 + pow((Duv/cutoff_freq), 2*n)
    return (1/divider)


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
for i in range(len(padded_img)):
    for j in range(len(padded_img[i])):
        padded_img[i][j] = padded_img[i][j] * pow(-1, i+j)

matrix1 = copy(padded_img)
matrix2 = copy(padded_img)
matrix3 = copy(padded_img)
matrix4 = copy(padded_img)

matrix1 = (fft2(matrix1)).tolist()
matrix2 = (fft2(matrix2)).tolist()
matrix3 = (fft2(matrix3)).tolist()
matrix4 = (fft2(matrix4)).tolist()

# 10
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        Hu = idel_filter(10, 256, 256, i, j)
        matrix1[i][j] = Hu * matrix1[i][j]
matrix1 = (ifft2(matrix1)).tolist()

output1 = copy(padded_img)
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        output1[i][j] = matrix1[i][j].real
wirefile = "output2_1_ideal_10.pgm"
writepgm(wirefile, output1, 256, 256)

# 20
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        Hu = idel_filter(20, 256, 256, i, j)
        matrix2[i][j] = Hu * matrix2[i][j]
matrix2 = (ifft2(matrix2)).tolist()

output2 = copy(padded_img)
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        output2[i][j] = matrix2[i][j].real
wirefile = "output2_1_ideal_20.pgm"
writepgm(wirefile, output2, 256, 256)

# 30
for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        Hu = idel_filter(30, 256, 256, i, j)
        matrix3[i][j] = Hu * matrix3[i][j]
matrix3 = (ifft2(matrix3)).tolist()

output3 = copy(padded_img)
for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        output3[i][j] = matrix3[i][j].real
wirefile = "output2_1_ideal_30.pgm"
writepgm(wirefile, output3, 256, 256)

# 40

for i in range(len(matrix4)):
    for j in range(len(matrix4[i])):
        Hu = idel_filter(40, 256, 256, i, j)
        matrix4[i][j] = Hu * matrix4[i][j]
matrix4 = (ifft2(matrix4)).tolist()

output4 = copy(padded_img)
for i in range(len(matrix4)):
    for j in range(len(matrix4[i])):
        output4[i][j] = matrix4[i][j].real
wirefile = "output2_1_ideal_40.pgm"
writepgm(wirefile, output4, 256, 256)

matrix5 = copy(padded_img)
matrix6 = copy(padded_img)
matrix7 = copy(padded_img)
matrix8 = copy(padded_img)


matrix5 = (fft2(matrix5)).tolist()
matrix6 = (fft2(matrix6)).tolist()
matrix7 = (fft2(matrix7)).tolist()
matrix8 = (fft2(matrix8)).tolist()
output5 = copy(padded_img)
output6 = copy(padded_img)
output7 = copy(padded_img)
output8 = copy(padded_img)


def filtered(matrix, output, filter_name, cutoff_freq):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Hu = butter_filter(cutoff_freq, 256, 256, i, j)
            matrix[i][j] = Hu * matrix[i][j]
    matrix = (ifft2(matrix)).tolist()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[i][j] = matrix[i][j].real
    wirefile = "output2_1_" + filter_name + "_" + str(cutoff_freq) + ".pgm"
    writepgm(wirefile, output, 256, 256)


filtered(matrix5, output5, "butter", 10)
filtered(matrix6, output6, "butter", 20)
filtered(matrix7, output7, "butter", 30)
filtered(matrix8, output8, "butter", 40)
