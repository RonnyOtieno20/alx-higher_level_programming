#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    print all integers of a list, in reverse order
    format: one integer per line
    you are not allowed to import any module
    you can assume that the list only contains integers
    you are not allowed to cast integers into strings
    you have to use str.format() to print integers
    """
    if not my_list:
        return None
    my_list.reverse()

    for num in my_list:
        print("{:d}".format(num))
