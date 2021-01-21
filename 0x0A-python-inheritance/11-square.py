#!/usr/bin/python3
"""Files defines class square with inheritance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines class sqaure inherited from rectangle"""

    def __init__(self, size):
        """Initialization method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        """String representation of a squaree"""
        return ("[Square] {}/{}".format(self._size, self._size))
