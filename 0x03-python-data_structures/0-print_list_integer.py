#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    prints all integers in a list
    Format: one integer per line
    You are not allowed to import any module
    You can assume the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
    """
    for num in my_list:
        print("{:d}".format(num))
