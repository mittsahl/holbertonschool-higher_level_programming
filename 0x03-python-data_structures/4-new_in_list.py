#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    if idx > len(my_list) or idx < 0 or element is None or my_list is None:
        return (my_list)
    for num in my_list:
        new_list.append(num)
    new_list[idx] = element
    return new_list
