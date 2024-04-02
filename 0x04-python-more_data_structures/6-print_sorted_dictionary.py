#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Function that prints a dictionary by ordered keys
    You can assume that all keys are strings
    Keys should be sorted by alphabetical order
    Only sort keys of the first level
    Dictionary values can be any type
    You are not allowed to import any module
    """
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
