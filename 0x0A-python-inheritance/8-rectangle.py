#!/usr/bin/python3
"""This file is about inheriting classes from other files"""
geo = __import__('7-base_geometry').BaseGeometry


class Rectangle(geo):
    """Class definition that inherits BaseGeometry"""
    def __init__(self, width, height):
        """Init function that checks and sets the values"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
