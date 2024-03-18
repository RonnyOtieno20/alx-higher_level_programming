#!/usr/bin/python3


def replace_in_list(my_list, idx, new_element):
    """
        function that replaces an element of a list at a specific position
        (like in C).
        if idx is negative or out of range, return the original list
        you are not allowed to import any module
    you are not allowed to use try/except
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = new_element
        return my_list
