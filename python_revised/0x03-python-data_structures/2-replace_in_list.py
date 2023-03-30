#!/usr/bin/python3
"""
* given a list and an index 
* update the element at the given index of the list
* if the given position is negative then return the list
* if the position is out of range return the list


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
        """
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
