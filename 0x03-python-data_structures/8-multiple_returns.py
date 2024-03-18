#!/usr/bin/python3


def multiple_returns(sentence):
    """
    returns the length of a string and its first character
    if the sentence is empty, the first character should be equal to None
    you are not allowed to import any module
    """
    if len(sentence) == 0:
        return len(sentence), None
    return (len(sentence), sentence[:1])
