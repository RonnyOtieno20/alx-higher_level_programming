#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
       finds all multiples of 2 in a list
        return a new list with True or False, depending on whether the integer
        at the same position in the original list is a multiple of 2
        the new list should have the same size as the original list
        you are not allowed to mport any module
    """
    result_list = []
    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return (result_list)
