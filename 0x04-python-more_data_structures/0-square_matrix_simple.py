#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Function that computes the square value of all integers of a matrix.
    Matrix is a two dimensional array.
        Same size as matrix.
        Each value should be the square of the value of the input.
    Initial matrix should not be modified.
    You are not allowed to import any module.
    You are not allowed to use regular loops, maps, etc.
    """
    new_matrix = [[i**2 for i in row] for row in matrix]
    return new_matrix
