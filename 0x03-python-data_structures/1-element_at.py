#!/usr/bin/python3

def element_at(my_list, idx):
    """
        function that retrieves an element from a list like in C
        if idx is negative, the function should return None
        if idx is out of range (> number of elements in my_list), return None
        You are not allowed to import any module
        You are not allowed to use try/except
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
