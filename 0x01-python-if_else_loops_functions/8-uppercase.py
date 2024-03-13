#!/usr/bin/python3


def uppercase(str):
    """prints a string in uppercase followed by a newline
    str: string to be printed
    return: string in uppercase
    """
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
