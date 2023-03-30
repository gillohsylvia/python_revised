#!/usr/bin/env python3
"""
* given a number
* get the absolute value of the number
* find the modulo 10 of the number
* print the answer
* return the answer
"""

def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end = '')
    return last_digit
