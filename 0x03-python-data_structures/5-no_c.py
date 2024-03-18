#!/usr/bin/python3

def no_c(my_string):
    """
        function that removes all the characters c and C from a string
        the function should return the new string
        you are not allowed to import any module
        you are not allowed to use str.replace()
    """
    new_string = ''
    for char in my_string:
        if char not in 'c' and char not in 'C':
            new_string += char
    return new_string
