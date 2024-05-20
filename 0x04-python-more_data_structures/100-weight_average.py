#!/usr/bin/python3


def weight_average(my_list=[]):
    """Function that returns the weighted average of all integers tuple
    (<score>, <weight>).
    You are not allowed to import any module.
    Args:
        my_list
    Returns:
        0 if list is empty, otherwise the weighted average.
    """
    if not my_list:
        return 0

    total = sum(x * y for (x, y) in my_list)

    divisor = sum(y for (x, y) in my_list)

    weighted_average = total / divisor

    return weighted_average
