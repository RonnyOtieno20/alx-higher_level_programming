#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Function that deletes a key in a string
    Args:
        a_dictionary: The dictionary in question
        key="": key to delete
    Returns:
        modified dictionary
    """
    a_dictionary.pop(key, None)
    return a_dictionary
