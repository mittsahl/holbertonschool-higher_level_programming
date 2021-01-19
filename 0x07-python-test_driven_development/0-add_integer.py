#!/usr/bin/python3
"""Adds two integers together and returns sum"""

def add_integer(a, b=98):
    """Returns sum only if a and b are int or float"""
    if a is None:
        raise TyperError("add_integer() missing 1 required positional argument: 'a'")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
