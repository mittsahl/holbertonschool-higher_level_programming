#!/usr/bin/python3
"""File converts object to a JSON representation"""
import json


def to_json_string(my_obj):
    """returns the object, json format"""
    return json.dumps(my_obj)
