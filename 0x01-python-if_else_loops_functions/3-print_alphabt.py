#!/usr/bin/python3

string = ""
for char in range(97, 123):
    if char != 101 and char != 113:
        string += chr(char)
print(string)
