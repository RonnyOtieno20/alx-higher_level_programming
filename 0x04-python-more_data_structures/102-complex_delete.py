#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Function that deletes a key associated with the value given
    Args:
        a_dictionary: Dictionary
        value: Value
    Returns:
        Dictionary or None if value doesn't exist
    """
    if a_dictionary is None:
        return None
    for key in sorted(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
