#!/usr/bin/python3
"""
Given an 'n' x 'n' matrix,
rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix 90 degrees clockwise
    - @matrix: a list of lists
    - @return: nothing - edit in place
    """
    # transpose matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for row in matrix:
        row.reverse()

    return matrix
