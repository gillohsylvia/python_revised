#!/usr/bin/env python3
"""
*given a string
*make a copy of the string
*delete element at index n
"""

def remove_char_at(str, n):
    new_str = ""
    if n >= 0 and n < len(str):
        new_str = str[:n] + str[n+1:]
        return(new_str)    
    else:
        return(str)

    """     run = str[n]
    else:
        run = ""
    for i in str:
        if i != run:
            new_str += i
            """
        
