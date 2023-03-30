""" 
* given a list and an element at a given position
* replace the element with the one in the list at the same position
* if the position is negative, return the copy of the list by the use of the inbuilt function copy()
* if the position is out of the range, return the copy of the list 
"""

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx >= len(my_list):
        return new_list
    else:
        new_list[idx] = element
        return new_list





