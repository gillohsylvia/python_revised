#!/usr/bin/python3
"""
* given a list of integers
* declare a variable max_int
* assign the element index 0 to the variable
* loop through the list
* compare the elements with the variable max_int
* state a conditional to check fo the element that might be greater than the variable max_int and assign it to max_int
* return the value at max_int

def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    max_int = my_list[0]
    for i in my_list:
        if max_int < i:
            max_int = i
 return max_int
 """
def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    list_sort = sorted(my_list)
    max_int = list_sort[-1]
    return max_int


