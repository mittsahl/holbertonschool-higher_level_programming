#!/usr/bin/python3
"""Converts a json string into a python object"""
import json


def from_json_string(my_str):
    """Function that does the conversion"""
    return json.loads(my_str)
