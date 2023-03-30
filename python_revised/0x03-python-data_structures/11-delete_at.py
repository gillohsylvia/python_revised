"""
* given a list with an index to be deleted
* if the index is negative or out of range, return the list
* delete the element at the given index
* return the new_list
"""
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list

