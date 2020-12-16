#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    for num in range(0, len(my_list)):
        if num == idx:
            del my_list[idx]
    return my_list
