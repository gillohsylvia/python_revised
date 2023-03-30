#!/usr/bin/env python3
"""
* given a string
* declare an empty string
* loop through the elements given string
* declare a conditional statement to filter out c and C* increment the new string with the remaining element

"""
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_string += i
    return new_string       
