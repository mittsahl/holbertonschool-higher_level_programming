#!/usr/bin/python3
"""This is a makiing a list and method to print sorted list"""


class MyList(list):
    """Class that inherits from list data type"""
    def print_sorted(self):
        """Prints the sorted list from first to last"""
        print(sorted(self))
