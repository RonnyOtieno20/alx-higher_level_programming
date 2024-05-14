#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Function that replaces or adds key/value in a dictionary.
    key argment will always be a string
    value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn't exists, it will be created
    You are not allowed to import any module
    Args:
        a_dictionary: the dictionary in question
        key: dictionary key
        value: dictionary value
    """
    a_dictionary.update({key: value})
    return a_dictionary


if __name__ == '__main__':
    main()
