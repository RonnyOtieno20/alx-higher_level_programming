#!/usr/bin/python3

def max_integer(my_list=[]):
    """
        finds the biggest integer of a list
        if the list is empty, return None
        you can assume that the list only contains integers
        you are not allowed to import any module
        you are not allowed to use the builtin max()
    """

    if not my_list:
        return (None)
    else:
        max_value = my_list[0]
        for num in my_list:
            if num > max_value:
                max_value = num
        return (max_value)
