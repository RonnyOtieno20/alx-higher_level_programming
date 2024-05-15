#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Function that returns a new dictionary with all values multiplied by 2.
    Args:
        a_dictionary
    Returns:
        a new dictionary
    """
    new_dict = {k: v * 2 for k, v in sorted(a_dictionary.items())}
    return new_dict
