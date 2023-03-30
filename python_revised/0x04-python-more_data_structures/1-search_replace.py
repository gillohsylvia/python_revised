"""
* given a list, an element to replace, and a new element
* looping the list
* state a conditional statement to check for any occurances of the element to be replaced
* replace it with the new element
* append the results a new-list
* return the new list
"""

def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            i = replace
            new_list.append(i)
        else:
            new_list.append(i)
    return new_list
