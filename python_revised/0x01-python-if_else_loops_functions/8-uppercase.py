#!/usr/bin/env python3
"""
* given a string
* declare a new variable new_string
* loop through the string 
* if a character in the string is an uppercase add it to the new_string variable, else convert it to uppercase then add it to the new_string variable
* return the new string
"""

def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) in range(97, 123):
            new_str += chr(ord(i)-32)
        else:
            new_str += i
    print(new_str)

