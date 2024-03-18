#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
        print a matrix of integers
        you are not allowed to import any module
        you can assume that the list only contains integers
        you are not allowed to cast integers into strings
        you have to use str.format() to print integers
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
