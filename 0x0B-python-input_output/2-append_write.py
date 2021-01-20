#!/usr/bin/python3
"""Program that appends to a file"""


def append_write(filename="", text=""):
    """Function that opens and writes to file"""
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
