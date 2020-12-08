#!/usr/bin/python3

def uppercase(string):
    strang = ""
    for letter in string:
        if (ord(letter) > 96 and ord(letter) < 123):
            letter = ord(letter) - 32
            strang += chr(letter)
        else:
            strang += letter
    print("{}".format(strang)) 
