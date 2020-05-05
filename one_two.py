from scipy.fft import fft2, ifft2
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy, checkfft
import numpy as np
import math
filename = "./output_img/output1_1_phase.pgm"
col = 0
row = 0
converted_img = []
mattrix_img = []
converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)


for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        complex_num = complex(
            math.e**(-2j*math.pi*(((20*i)/256)+((30*j)/256))))
        mattrix_img[i][j] = mattrix_img[i][j]*complex_num

for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        mattrix_img[i][j] = mattrix_img[i][j] * pow(-1, i+j)

output_img = np.zeros_like(mattrix_img)
output_img = ifft2(mattrix_img).tolist()
# print(output_img)
for i in range(len(output_img)):
    for j in range(len(output_img[i])):
        value = abs(output_img[i][j])
        output_img[i][j] = value

print(output_img)
wirefile = "output1_2.pgm"
writepgm(wirefile, output_img, 256, 256)
