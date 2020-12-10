#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(str(a), str(b), str(add(a, b))))
    print("{} - {} = {}".format(str(a), str(b), str(sub(a, b))))
    print("{} * {} = {}".format(str(a), str(b), str(mul(a, b))))
    print("{} / {} = {}".format(str(a), str(b), str(div(a, b))[0]))
