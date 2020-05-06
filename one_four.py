from scipy.fft import fft2, ifft2, fft
from etc_function import read_pgm, list_to_2D_list, copy, writepgm, copy, checkfft
import numpy as np
import math

filename = "./image/Cross.pgm"
col = 0
row = 0
converted_img = []
mattrix_img = []
converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)
mattrix_img = np.array(mattrix_img)
img_down = mattrix_img[::2, ::2]
img_down = img_down.tolist()
wirefile = "output1_4_downsample.pgm"
copyimg = copy(img_down)
writepgm(wirefile, img_down, 100, 100)
padded_img = []
for i in range(128):
    padded_img_inloop = []
    for j in range(128):
        padded_img_inloop.append(0)
    padded_img.append(padded_img_inloop)
for i in range(len(copyimg)):
    for j in range(len(copyimg[i])):
        padded_img[14+i][14+j] = copyimg[i][j]

for i in range(len(padded_img)):
    for j in range(len(padded_img[i])):
        padded_img[i][j] = padded_img[i][j] * pow(-1, i+j)

fourier_transform = fft2(padded_img)
fourier_transform = fourier_transform.tolist()
copy_img = (np.angle(fft2(padded_img))).tolist()
for i in range(len(fourier_transform)):
    for j in range(len(fourier_transform[i])):
        # copy_img[i][j] = check2(
        #     fourier_transform[i][j].imag, fourier_transform[i][j].real)
        value = abs(fourier_transform[i][j])

        # fourier_transform[i][j] = int(check(value))
        fourier_transform[i][j] = checkfft(value)


wirefile = "output1_4_spectrum.pgm"
writepgm(wirefile, fourier_transform, 128, 128)

for i in range(len(copy_img)):
    for j in range(len(copy_img[i])):
        copy_img[i][j] = copy_img[i][j]*100
        if(copy_img[i][j] <= 0):
            copy_img[i][j] = 0
        elif(copy_img[i][j] > 255):
            copy_img[i][j] = 255
wirefile = "output1_4_phase.pgm"
writepgm(wirefile, copy_img, 128, 128)
