"""
* import sys
* declare the variable that will hold the length of the argv
* print the size of the argument
* loop through the size of the argv and print out the exact values and their position
"""

from sys import argv

argc = len(argv) 
args = argc - 1

if args == 0:
    print(":")
elif args == 1:
    print("{} argument:".format(args))
else:
    print("{} arguments:".format(args))

if args:
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))


