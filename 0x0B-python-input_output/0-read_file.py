#!/usr/bin/python3
"""This program reads a file and prints it to standard out"""


def read_file(filename=""):
    """Reads file and prints"""
    with open(filename) as f:
        print(f.read(), end="")
