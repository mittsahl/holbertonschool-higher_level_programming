#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) or idx == None or my_list == None:
        return None
    return my_list[idx]
