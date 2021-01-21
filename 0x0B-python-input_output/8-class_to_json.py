#!/usr/bin/python3
"""Converts a class to json"""


def class_to_jason(my_obj):
    """Converts class to json"""
    return my_obj.__dict__
