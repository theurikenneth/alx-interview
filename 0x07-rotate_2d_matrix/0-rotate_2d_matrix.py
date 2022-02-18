#!/usr/bin/python3
"""
2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    rotates two dimension matrix and returns nothing
    """
    length = len(matrix)
    for k in range(int(length / 2)):
        j = (length - k - 1)
        for i in range(k, j):
            y = (length - 1 - i)
            # checking the number
            temp_number = matrix[k][i]
            # changing the top to the left
            matrix[k][i] = matrix[y][k]
            # moving the left to bottom
            matrix[y][k] = matrix[j][y]
            # moving bottom to the right
            matrix[j][y] = matrix[l][j]
            # moving the right to the top
            matrix[i][j] = temp_number
