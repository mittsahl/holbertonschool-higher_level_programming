#!/usr/bin/python3
"""Defines class student"""


class Student:
    """Defines class student"""
    def __init__(self, first_name, last_name, age):
        """Initialization method"""
        self.first name = first_name
        self.last_name = last_name
        self.age = age

    def to_josn(self):
        """Converts to a dict"""
        return self.__dict__
