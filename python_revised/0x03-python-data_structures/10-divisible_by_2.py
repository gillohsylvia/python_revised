"""
* on a given list of intergers
* declare an empty new list
* loop through the given list
* find the modulo 2 of each element
* append True if the answer is 0 and False when it is 1 to the new list
"""
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
