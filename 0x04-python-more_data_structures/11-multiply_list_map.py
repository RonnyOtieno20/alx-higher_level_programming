#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Function that returns a list with all the values multiplied
    by a number without using any loops
    Initial list should not be modified
    You are not allowed to import any module
    You have to use map, and your file should be max 3 lines
    Args:
        my_list=[]: list whose values are to be modified
        number: number to multiply list values with
    Returns:
        A new list same length as my_list
        Each value should be multiplied by number
    """
    new_list = map(lambda x: x * number, my_list)
    return list(new_list)
