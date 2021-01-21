#!/usr/bin/python3
"""This program loads a json file"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        print(f.read())
