#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = (number % 10, number % -10)[(number < 0) == True]
print("Last digit of {} is {} and is".format(number, last), end = ' ')
if last > 5:
    print("greater than 5")
elif last < 6 and last != 0:
    print("less than 6 and not 0")
elif last == 0:
    print("0")
