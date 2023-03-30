#!/usr/bin/python3
"""
* given a list
* loop through the list
* print elements from the startin from the last element
        new_list = 


def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        index = len(my_list) -1
        for i in my_list:
            print(index)
            index -= 1
"""
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        print( i)
    
