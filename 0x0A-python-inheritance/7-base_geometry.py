#!/usr/bin/python3
"""This file defines test class and methods"""


class BaseGeometry:
    """Class definition"""
    def area(self):
        """Throws an error when not made"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        """Checks the data type of value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
