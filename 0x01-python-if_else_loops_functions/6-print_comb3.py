#!/usr/bin/python3

for num1 in range(0, 8):
    for num2 in range(num1 + 1, 10):
        print("{}{}, ".format(num1, num2), end='')
print("{:d}".format(89))
