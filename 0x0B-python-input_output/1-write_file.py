#!/usr/bin/python3
"""This writes to file"""


def write_file(filename="", text=""):
    """Fcuntion that opens and writes to file"""
    with open(filename, "w") as f:
        f.write(text)
        return (len(text))
