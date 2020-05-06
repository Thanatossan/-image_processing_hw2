from scipy.fft import fft2, ifft2
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy
import numpy as np
import math

kernel = [[0.0625, 0.125, 0.0625], [
    0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]]


filename = "./image/Chess.pgm"
col = 0
row = 0
converted_img = []
mattrix_img = []
converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)
padded_img = []
for i in range(len(mattrix_img)+2):
    padded_img_inloop = []
    for j in range(len(mattrix_img)+2):
        padded_img_inloop.append(0)
    padded_img.append(padded_img_inloop)
for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        padded_img[i][j] = mattrix_img[i][j]


# convolution
convoluted = copy(padded_img)
# print(convoluted)
result = 0

for i in range(len(padded_img)-2):
    for j in range(len(padded_img[i])-2):
        for k in range(3):
            for z in range(3):
                result += kernel[k][z] * padded_img[i+k][j+z]
        convoluted[i][j] = result
        result = 0
cutpad = []
for i in range(len(padded_img)-2):
    cutpad_inloop = []
    for j in range(len(padded_img[i])-2):
        cutpad_inloop.append(convoluted[i][j])
    cutpad.append(cutpad_inloop)


wirefile = "output1_7_blur.pgm"
writepgm(wirefile, cutpad, 256, 256)

new_pad_img = []
padded_kernel = []


# fillter

for i in range((2*256)-1):
    new_pad_img_inloop = []
    for j in range((2*256)-1):
        new_pad_img_inloop.append(0)
    new_pad_img.append(new_pad_img_inloop)
    padded_kernel.append(new_pad_img_inloop)

for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        new_pad_img[i][j] = mattrix_img[i][j] * pow(-1, i+j)

new_pad_img = (fft2(new_pad_img)).tolist()

for i in range(len(kernel)):
    for j in range(len(kernel[i])):
        padded_kernel[i][j] = kernel[i][j] * pow(-1, i+j)
padded_kernel = (fft2(padded_kernel)).tolist()

output = (np.zeros_like(padded_kernel)).tolist()
for i in range(len(padded_kernel)):
    for j in range(len(padded_kernel[i])):
        output[i][j] = padded_kernel[i][j].real * new_pad_img[i][j].real

fourier_output = ifft2(output)
# print(output)
for i in range(len(fourier_output)):
    for j in range(len(fourier_output[i])):
        output[i][j] = fourier_output[i][j] * pow(-1, i+j)

final_output = np.zeros_like(mattrix_img)
for i in range(256):
    for j in range(256):
        final_output[i][j] = (fourier_output[i][j])
        if final_output[i][j] < 0:
            final_output[i][j] = 0
        elif final_output[i][j] > 255:
            final_output[i][j] = 255
final_output = final_output.tolist()


wirefile = "output1_7_filter_test.pgm"
writepgm(wirefile, final_output, 256, 256)
