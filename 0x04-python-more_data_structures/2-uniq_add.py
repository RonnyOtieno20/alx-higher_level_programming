#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Function that adds all unique integers in a list
    (only once for each integer).
    You are not allowed to import any module.
    """
    new_list = set(my_list)
    return sum(new_list)
