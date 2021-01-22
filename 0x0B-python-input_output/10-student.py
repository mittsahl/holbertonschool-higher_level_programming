#!/usr/bin/python3
"""Dict representationof an instance"""


class Student:
    """Definition of class student"""

    def __init__(self, first_name, last_name, age):
        """Initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dict rerpesentation student"""
        new = {}
        if type(attrs) is list:
            for key in attrs:
                if type(key) is str:
                    try:
                        new[key] = self.__dict__[key]
                    except:
                        pass
            return new
        return vars(self)
