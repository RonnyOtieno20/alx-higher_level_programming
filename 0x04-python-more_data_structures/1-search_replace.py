#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Function that replaces all occurrences of an element
    by another in a new list.
    my_list is the initial list.
    search is the element to replace in my_list.
    replace is the new element.
    You are not allowed to import any module.

    new_list = my_list
    for i in new_list:
        if i == search:
            new_list[new_list.index(i)] = replace
    return new_list

    new_list = [replace if i == search else i for i in my_list]
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
