#!/usr/bin/python3

def print_last_digit(number):
    last = (number % 10, abs(number % -10))[number < 0]
    print("{}".format(last), end='')
    return last
