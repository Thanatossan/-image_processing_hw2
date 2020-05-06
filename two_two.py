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


def median_filter(size, matrix, k, m):
    median_finder = []
    median_finder.append(matrix[k-1][m-1])
    median_finder.append(matrix[k][m-1])
    median_finder.append(matrix[k+1][m-1])
    median_finder.append(matrix[k-1][m])
    median_finder.append(matrix[k][m])
    median_finder.append(matrix[k+1][m])
    median_finder.append(matrix[k-1][m+1])
    median_finder.append(matrix[k][m+1])
    median_finder.append(matrix[k-1][m+1])
    median_finder.sort()
    mid = len(median_finder) // 2
    res = int((median_finder[mid] + median_finder[~mid]) / 2)
    return res


def filtered1(matrix, output, filter_name, cutoff_freq):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Hu = butter_filter(cutoff_freq, 256, 256, i, j)
            matrix[i][j] = Hu * matrix[i][j]
    matrix = (ifft2(matrix)).tolist()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[i][j] = matrix[i][j].real
    wirefile = "output2_2_" + filter_name + "_" + str(cutoff_freq) + ".pgm"
    writepgm(wirefile, output, 256, 256)


def filtered2(matrix, output, filter_name, cutoff_freq):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            Hu = idel_filter(cutoff_freq, 256, 256, i, j)
            matrix[i][j] = Hu * matrix[i][j]
    matrix = (ifft2(matrix)).tolist()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[i][j] = matrix[i][j].real
    wirefile = "output2_2_" + filter_name + "_" + str(cutoff_freq) + ".pgm"
    writepgm(wirefile, output, 256, 256)


filename1 = "./image/Lenna_noise.pgm"
col = 0
row = 0
converted_img1 = []
mattrix_img1 = []
converted_img1, col, row = read_pgm(filename1, col, row)
mattrix_img1 = list_to_2D_list(converted_img1, mattrix_img1, col, row)

filename2 = "./image/Lenna_noise.pgm"
col = 0
row = 0
converted_img2 = []
mattrix_img2 = []
converted_img2, col, row = read_pgm(filename2, col, row)
mattrix_img2 = list_to_2D_list(converted_img2, mattrix_img2, col, row)

padded_img = copy(mattrix_img1)
for i in range(len(padded_img)):
    for j in range(len(padded_img[i])):
        padded_img[i][j] = padded_img[i][j] * pow(-1, i+j)

matrix1 = copy(padded_img)
matrix2 = copy(padded_img)
matrix3 = copy(padded_img)
matrix4 = copy(padded_img)
matrix5 = copy(padded_img)
matrix6 = copy(padded_img)
matrix7 = copy(padded_img)
matrix8 = copy(padded_img)


matrix1 = (fft2(matrix1)).tolist()
matrix2 = (fft2(matrix2)).tolist()
matrix3 = (fft2(matrix3)).tolist()
matrix4 = (fft2(matrix4)).tolist()
matrix5 = (fft2(matrix5)).tolist()
matrix6 = (fft2(matrix6)).tolist()
matrix7 = (fft2(matrix7)).tolist()
matrix8 = (fft2(matrix8)).tolist()

output1 = copy(padded_img)
output2 = copy(padded_img)
output3 = copy(padded_img)
output4 = copy(padded_img)
output5 = copy(padded_img)
output6 = copy(padded_img)
output7 = copy(padded_img)
output8 = copy(padded_img)

filtered1(matrix1, output1, "ideal", 10)
filtered1(matrix2, output2, "ideal", 20)
filtered1(matrix3, output3, "ideal", 30)
filtered1(matrix4, output4, "ideal", 40)

filtered2(matrix5, output5, "butter", 10)
filtered2(matrix6, output6, "butter", 20)
filtered2(matrix7, output7, "butter", 30)
filtered2(matrix8, output8, "butter", 40)


matrix9 = copy(padded_img)
padded_img = []

for i in range(257):
    padded_img_inloop = []
    for j in range(257):
        padded_img_inloop.append(0)
    padded_img.append(padded_img_inloop)
for i in range(len(matrix9)):
    for j in range(len(matrix9[i])):
        padded_img[1+i][1+j] = matrix9[i][j]

for k in range(1, len(matrix9)-1):
    for m in range(1, len(matrix9[i])-1):
        # print(k, m)
        padded_img[k][m] = median_filter(3, matrix9, k, m)

for i in range(256):
    for j in range(256):
        matrix9[i][j] = padded_img[i+1][j+1]
wirefile = "output2_2_median.pgm"
writepgm(wirefile, matrix9, 256, 256)


def rms(origin, filltered):
    summ = 0
    for i in range(256):
        for j in range(256):
            summ += pow(origin[i][j] - filltered[i][j], 2)
    result = math.sqrt((1/256) * summ)
