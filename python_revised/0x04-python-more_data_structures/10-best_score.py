"""
* given a dictionary
* find the max value
* a print the key to that valu
"""
def best_score(a_dictionary):
    if type(a_dictionary) == dict and a_dictionary:
        top = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == top:
                return (key)
    else:
        return None

    
