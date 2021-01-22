#!/usr/bin/python3
"""Converts a class to json"""


def class_to_json(obj):
    """Converts class to json"""
    return vars(obj)
