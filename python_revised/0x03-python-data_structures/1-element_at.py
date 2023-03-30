#!/usr/bin/python3
"""
* given a list 
* return the element at the given position of the list
* if the given position is negative then return none
* if the position out of range return none


def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
    """
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return None
    return my_list[idx]
