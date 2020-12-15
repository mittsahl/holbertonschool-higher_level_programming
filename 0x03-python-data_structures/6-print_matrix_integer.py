#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for firstArray in matrix:
            index = 0
            for number in firstArray:
                if index == len(firstArray) - 1:
                    print("{:d}".format(number), end='')
                else:
                    print("{:d}".format(number), end=' ')
            print("", end='\n')
