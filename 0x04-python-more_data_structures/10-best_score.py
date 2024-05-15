#!/usr/bin/python3


def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value.
    Args:
        a_dictionary
    Returns:
        a key
    """
    if a_dictionary:
        max_key = max(a_dictionary.keys())
    else:
        max_key = None
    return max_key
