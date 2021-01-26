#!/usr/bin/python3
""" as of now empty rectangle class """


class Rectangle:
    """ the rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiation for rectangle"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """width getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of a rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ the string representation of the rectanlge"""
        retstr = ""
        if self.__width is 0 or self.__height is 0:
            return retstr
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                retstr += str(self.print_symbol)
            if i is not self.__height - 1:
                retstr += "\n"
        return retstr

    def __repr__(self):
        """ a new str representation o be used with eval """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints a message when deleting a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ which rectangle is bigger """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
