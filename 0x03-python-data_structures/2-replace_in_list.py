#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if (my_list or element or idx) is None or idx < 0 or idx > len(my_list):
        print("First Check")
        return my_list
    my_list[idx] = element
    return my_list
