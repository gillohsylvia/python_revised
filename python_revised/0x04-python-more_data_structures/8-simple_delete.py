"""
* given a dictionary
* check if the key exist 
* delete if does otherwise return the dictionary
"""
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]

    return a_dictionary
