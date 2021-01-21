#!/usr/bin/python3
"""Changes class"""


class MyInt(int):
    """MyInt - changing certain implementation of int class"""
    def __eq__(self, other):
        """__eq__ - chnages from equal to not equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """__ne__ - function changes value from not equal to equal"""
        return int.__eq__(self, other)
