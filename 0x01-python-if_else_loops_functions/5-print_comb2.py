#!/usr/bin/python3

for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    elif num < 10:
        print("{}{}".format(num % 1, num), end=", ")
    else:
        print("{}".format(num), end=", ")
