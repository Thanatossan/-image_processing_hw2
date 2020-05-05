from scipy.fft import fft2, ifft2, fft
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy, Bilinear
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
rotate_img = np.zeros_like(mattrix_img)

for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        padded_img[28+i][28+j] = mattrix_img[i][j]
