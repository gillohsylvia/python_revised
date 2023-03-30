"""
*import the function from the file add_0.py
*assign values to variable a and b
*print the sum of a and b using a the function add
"""

if __name__=="__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a,b,add(a,b)))

