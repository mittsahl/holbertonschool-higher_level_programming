#!/usr/bin/python3

def uppercase(string):
    strang = ""
    for letter in range(0, len(string)):
        if (ord(string[letter]) > 96 and (ord(string[letter]) < 123)):
            strang += chr(ord(string[letter]) - 32)
        else:
            strang += string[letter]
    print(strang)
