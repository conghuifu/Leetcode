def sparse_matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a) == 0:
        return [[]]
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    # Write your code here.
    dense_a = get_no_zero_dict(matrix_a)
    dense_b = get_no_zero_dict(matrix_b)
    n = len(matrix_b[0])

    matrix = [[0 for j in range(len(matrix_b[0]))] for i in range(len(matrix_a))]
    for row, col in dense_a.keys():
        for j in range(n):
            if (col, j) in dense_b:
                matrix[row][j] += dense_a[(row, col)] * dense_b[(col, j)]

    return matrix

def get_no_zero_dict(matrix):
    res = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                res[(i, j)] = matrix[i][j]

    return res