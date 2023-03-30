"""
* given two sets
* find the elements in set_1 that are not in set_2
* store the elements in a new_set
* find the elements in set_2 that are not in set_1
* store the elements in onother new-set
* add the new_sets
* return the results
"""
def only_diff_elements(set_1, set_2):
    #new_set = set_1.difference(set_2)
    #new_set2 = set_2.difference(set_1)
    #diff = new_set.union(new_set2)
    diff = set_1 ^ set_2
    return diff

