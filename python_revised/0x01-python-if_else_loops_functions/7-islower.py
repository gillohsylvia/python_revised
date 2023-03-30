#!/usr/bin/env python3
"""
* take a character
* check if the character is in range(97, 123)
* return true if the character exit between the range and return false if it doesn't
"""

def islower(c):
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
    

