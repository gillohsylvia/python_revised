"""
* given a dictionary
* sort the keys
* print out the sorted keys with their values

def print_sorted_dictionary(a_dictionary):
    dict_1 = sorted(a_dictionary.keys())
    for i in dict_1:
        print("{}: {}".format(i,a_dictionary[i]))
        """
def print_sorted_dictionary(a_dictionary):
    sorted_values = sorted(a_dictionary.items())
    for keys, values in sorted_values:
        print("{}: {}".format(keys,values))

