#!usr/bin/python3
"""Inherits form task 8"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defintion of square class"""
    def __init__(self, size):
        """Initialization method"""
        Rectangle.__init__(self, size, size)
        self.size = size
