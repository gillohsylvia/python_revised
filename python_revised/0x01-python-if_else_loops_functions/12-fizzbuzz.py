#!/usr/bin/env python3
"""
* in range of 100
* print all the numbers in a ascending order
* replace the multiples of 3 with Fizz
* replace the multiples of five with Buzz
* replace the multiples of both 3 and 5 with FizzBuzz
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", end=' ')
        elif i % 5 == 0:
            print("Fizz", end=' ')
        elif i % 3 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
