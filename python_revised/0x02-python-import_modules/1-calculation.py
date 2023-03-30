"""
* import all the functions from the file calculator_1.py
* assign values to the variables a and b
* use the functions to do maths
* print the results using a string format
"""
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5


    print("{} + {} = {}".format(a,b,add(a,b)))
    print("{} - {} = {}".format(a,b,sub(a,b)))
    print("{} * {} = {}".format(a,b,mul(a,b)))
    print("{} / {} = {}".format(a,b,div(a,b)))


