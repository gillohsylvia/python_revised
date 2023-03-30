#!/usr/bin/python3
"""
* given a tuple
* find out the length of the tuple
* return the length and the element at index 0
"""
def multiple_returns(sentence):
    if not  (sentence):
        return (0, None)
    else:
        Length = len(sentence)
        First_character = sentence[0]
        return (Length, First_character)

