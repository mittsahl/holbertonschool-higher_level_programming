#!/usr/bin/python3
"""Creating another class with inheritance"""
geo = __import__('7-base_geometry').BaseGeometry


class Rectangle(geo):
    """Class definition"""
    def __init__(self, width, height):
        """Initilaization function"""
        self.__width = width
        self.__height = height

    def area(self):
        """Finds the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Finds the dimensions of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
