"""
* given a dictionary
* create a new dictionary
* loop through the dictionary
* increment the value by two
* append the results to the new dictionary
* return the new dictionary


def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary.keys():
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
"""
def multiply_by_2(a_dictionary):
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary

