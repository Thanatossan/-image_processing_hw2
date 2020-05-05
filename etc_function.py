def createHistogram(converted_img):
    gray_level = []
    frequency = []
    histogram = {}
    for i in range(len(converted_img)):
        if converted_img[i] not in gray_level:
            gray_level.append(converted_img[i])
    gray_level.sort()
    for i in range(len(gray_level)):
        frequency.append(converted_img.count(gray_level[i]))
    histogram = dict(zip(gray_level, frequency))
    return histogram


def solve4eqaultion(A, b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = float(M[n-1][n])/M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = float(M[i][n] - z)/M[i][i]
    return x


def Bilinear(old_image, pixelXP, pixelYP):
    # point
    x = int(pixelXP//1)
    xplus = int((pixelXP+1)//1)

    y = int(pixelYP//1)
    yplus = int((pixelYP+1)//1)

    xScale = pixelXP - x
    yscale = pixelYP - y
    # read color from old image
    a = old_image[xplus][y] - old_image[x][y]
    b = old_image[x][yplus] - old_image[x][y]
    c = old_image[xplus][yplus] + old_image[x][y] - \
        old_image[x][yplus] - old_image[xplus][y]
    d = old_image[x][y]
    # caculate
    color = (a * xScale) + (b * yscale) + (c * xScale * yscale) + d

    color = int(round(color))
    return color


def createHistogram(converted_img):
    gray_level = []
    frequency = []
    histogram = {}
    for i in range(len(converted_img)):
        if converted_img[i] not in gray_level:
            gray_level.append(converted_img[i])
    gray_level.sort()
    for i in range(len(gray_level)):
        frequency.append(converted_img.count(gray_level[i]))
    histogram = dict(zip(gray_level, frequency))
    return histogram


def solve4eqaultion(A, b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = float(M[n-1][n])/M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = float(M[i][n] - z)/M[i][i]
    return x


def Bilinear(old_image, pixelXP, pixelYP):
    # point
    x = int(pixelXP//1)
    xplus = int((pixelXP+1)//1)

    y = int(pixelYP//1)
    yplus = int((pixelYP+1)//1)

    xScale = pixelXP - x
    yscale = pixelYP - y
    # read color from old image
    a = old_image[xplus][y] - old_image[x][y]
    b = old_image[x][yplus] - old_image[x][y]
    c = old_image[xplus][yplus] + old_image[x][y] - \
        old_image[x][yplus] - old_image[xplus][y]
    d = old_image[x][y]
    # caculate
    color = (a * xScale) + (b * yscale) + (c * xScale * yscale) + d

    color = int(round(color))
    return color


def writepgm(filename, mattriximg, col, row):
    string = ""
    filename = "./output_img/"+filename
    for i in range(len(mattriximg)):
        for j in range(len(mattriximg[i])):
            mattriximg[i][j] = chr(int(mattriximg[i][j]))
            string += mattriximg[i][j]
    f = open(filename, "a", encoding="ISO-8859-1")

    f.write("P5 \r")
    f.write(str(col) + " " + str(row) + "\r")
    f.write("255 \r")
    f.write(string)
    f.close


def read_pgm(filename, col, row):
    f = open(filename, encoding="ISO-8859-1")
    img = ""
    list_img = []
    comment = False
    # matirx_img = []
    for i, line in enumerate(f):
        if i == 1 and line[0:1] == "#":
            comment = True
        elif i == 1 and line[0:1] != "#":
            col = int(line[0:3])
            row = int(line[4:])
        if i == 2 and comment == True:
            col = int(line[0:3])
            row = int(line[4:])
        if i >= 4 and comment == True:
            img = img+line
        elif i >= 3 and comment == False:
            img = img+line
    f.close()
    # print(len(img))
    for i in range(len(img)):
        list_img.append((ord(img[i])))
    list_img = fix_miss_pixel(list_img)
    return list_img, col, row


def list_to_2D_list(lists, list_2D, col, row):
    for i in range(row):
        inner_list = []
        for j in range(col):
            inner_list.append(lists[i*(col)+j])
        list_2D.append(inner_list)
    return list_2D


def copy(lists):
    copy_list = []
    for i in range(len(lists)):
        inner_list = []
        for j in range(len(lists[i])):
            inner_list.append(lists[i][j])
        copy_list.append(inner_list)
    return copy_list


def fix_miss_pixel(list_img):
    if len(list_img) == 65534:
        for i in range(2):
            list_img.append(0)
    if len(list_img) == 331198:
        for i in range(2):
            list_img.append(0)
    if len(list_img) == 65529:
        for i in range(7):
            list_img.append(0)
    return list_img
