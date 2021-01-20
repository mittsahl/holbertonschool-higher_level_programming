#!/usr/bin/python3
"""Class with different methods and errors"""


class BaseGeometry:
    """method for raising area() error"""
    def area(self):
        raise Exception("area() is not implemented")

    """method for validation of value"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
