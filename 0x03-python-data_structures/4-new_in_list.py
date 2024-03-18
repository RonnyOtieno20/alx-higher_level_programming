#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
        replaces an element in a list at a specific position without
        modifying the original list like in C
        if idx is negative or out of range, the function should return
        a copy of the original list
        you are not allowed to import any module
        you are not allowed to use try/escape
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
