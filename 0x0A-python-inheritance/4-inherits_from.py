#!/usr/bin/python3
"""Function that checks to see if the instance of a class"""


"""Function that checks"""
def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    return (issubclass(type(obj), a_class))
