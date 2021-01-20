#!/usr/bin/python3
"""Function that checks to see if the instance of a class"""


def inherits_from(obj, a_class):
    """returns false if the clases and object are the same"""
    if type(obj) is a_class:
        return False
    return (issubclass(type(obj), a_class))
