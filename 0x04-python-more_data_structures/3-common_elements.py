#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    Function that returns a set of common elements in two sets.
    You are not allowed to import any other module.

    for i in set_1:
        for j in set_2:
            if i == j:
                return i

    new_set = (i for i in set_1 for j in set_2 if i == j)
    """
    new_set = list(map(lambda x: x, set_1 & set_2))
    return new_set
