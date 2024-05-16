#!/usr/bin/python3


def roman_to_int(roman_string):
    """Function that converts a Roman numeral into an integer.
    You can assume the number will be between 1 to 3999.
    If the roman_string is not a string or None, return 0.
    Args:
        roman_string
    Return:
        Integer representation of roman_string, else 0.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0
    n = len(roman_string)

    while i < n:
        if roman_string[i] not in roman_values:
            return 0

        current_value = roman_values[roman_string[i]]
        if i == n - 1:
            result += current_value
            break

        next_value = roman_values[roman_string[i + 1]]

        if next_value > current_value:
            result += next_value - current_value
            i += 2
        else:
            result += current_value
            i += 1

    return result
