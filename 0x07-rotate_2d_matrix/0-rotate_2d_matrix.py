#!/usr/bin/python3
"""
2D matrix 
"""


def rotate_2d_matrix(matrix):
    """
    2d square matrix should rotate 
    90 degrees clockwise in-place
    Args:
    matrix (list): 2d square matrix
    Return:
    None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
