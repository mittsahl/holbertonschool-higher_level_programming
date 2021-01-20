#!/usr/bin/python3
"""Writes an obj to a text file using Json rep"""
import json


def save_to_json_file(my_obj, filename=""):
    """Function that converts"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
