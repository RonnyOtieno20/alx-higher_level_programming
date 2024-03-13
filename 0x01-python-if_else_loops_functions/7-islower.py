#!/usr/bin/python3

def islower(c):
    """ function that checks for lowercase characters.
        args:
            c: The  character to be checked
        Returns:
            True if c is lowercase, otherwise False
    """
    return ord(c) >= 97 and ord(c) <= 122
