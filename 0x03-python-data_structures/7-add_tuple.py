#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
        Adds two tuples
        Returns a tuple with 2 integers:
            The first element should be the addition of the first element of
                each argument
            The second element should be the addition of the second element
                of each argument
        You are now allowed to import any module
        If a tuple is smaller than 2, use the value 0 for each missing integer
        You can assume that the two tuples will only contain integers
        If a tuple is biger than 2, use only the first 2 integers
    """
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    return (a[0] + b[0], a[1] + b[1])
