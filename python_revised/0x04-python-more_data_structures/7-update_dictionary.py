"""
* given a key and value
* conditional statement to check if the key exist
* if exist, loop to find the value and replace it with the given value
* create key if it does not exist
"""
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
