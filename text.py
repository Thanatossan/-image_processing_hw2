def median_filter(size, matrix, k, m):
    median_finder = []
    for i in range(size):
        for j in range(size):
            median_finder.append(matrix[k+i][m+j])
    median_finder.sort()
    mid = len(median_finder) // 2
    res = int((median_finder[mid] + median_finder[~mid]) / 2)
    return res


matrix = [[0, 0, 0], [125, 255, 255], [210, 250, 240]]

median_filter(3, matrix)
