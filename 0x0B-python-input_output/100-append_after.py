#!/usr/bin/python3
"""append after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """append after each line with search string """
    with open(filename, 'r+', encoding='utf-8') as file:
        stuff = file.readlines()
        line = 0
        for index in range(len(stuff)):
            if search_string in stuff[line]:
                line += 1
                stuff.insert(line, new_string)
            line+= 1
        file.seek(0)
        for line in stuff:
            file.write(line)
