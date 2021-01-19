#!/usr/bin/python3
"""This is a makiing a list and method to print sorted list"""


"""This is defining the class list"""
class MyList(list):
    """Function that prints the sorted list"""
    def print_sorted(self):
        print(sorted(self))

