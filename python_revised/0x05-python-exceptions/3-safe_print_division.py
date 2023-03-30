"""
* given two intergers a and b
* divide a by b and save the results on a new variable
* except block should print none when the results is 0
"""

def safe_print_division(a, b):
    try:
        result = a / b
        # print("Inside result: {}".format(result))
    except ZeroDivisionError:
        result = None
        # print("Inside result: {}".format())
    finally:
        print("Inside result: {}".format(result))
    return result


