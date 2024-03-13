#!/usr/bin/python3


def print_last_digit(number):
    """
    prints the last digit of  number
    returns the value of the last digit
    you are not allowed to import any module
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
