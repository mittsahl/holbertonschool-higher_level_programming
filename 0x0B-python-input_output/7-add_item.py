#!/usr/bin/python3
"""Adds arguments to list then saves to file"""
from sys import argv


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


name = "add_item.json"


try:
    f = load(name)
except:
    with open(name, 'w'):
        f = []
f += argv[1:]
save(f, name)
