"""
* use the argv function from sys
* declare a variable and assign it to zero
* loop through the length of the argv
* increment the value of the variable by the length of the argv
* print the variable
"""

from sys import argv

if __name__ == "__main__":

    sum = 0
    args = len(argv)

    for i in range(1, args):
        sum += int(argv[i])
    print(sum)
