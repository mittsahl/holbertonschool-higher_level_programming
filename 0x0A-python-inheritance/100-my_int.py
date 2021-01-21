#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """ Canging equality attributes of int class"""
    def __eq__(self, other):
        """Chagnes equality artributes form equal to not equal"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """changes equality attributes from not equal to equal"""
        return int.__eq__(self, other)
