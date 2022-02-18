#!/usr/bin/python3
"""
2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    rotates two dimension matrix and returns nothing
    """
    l = len(matrix)
    for k in range(int(l / 2)):
        j = (l - k - 1)
        for i in range(k, j):
            y = (l - 1 - i)
            # checking the number
            temp_number = matrix[k][i]
            # changing the top to the left
            matrix[k][i] = matrix[y][k]
            # moving the left to bottom
            matrix[y][k] = matrix[j][y]
            # moving bottom to the right
            matrix[j][y] = matrix[i][j]
            # moving the right to the top
            matrix[i][j] = temp_number
