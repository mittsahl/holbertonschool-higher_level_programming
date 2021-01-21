#!/usr/bin/python3
"""This file defines saure that inherits from rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition of square"""

    def __init__(self, size):
        """Initialization funcitons"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
