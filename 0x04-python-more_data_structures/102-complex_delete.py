#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = a_dictionary.copy()
    for key, v in new_dictionary.items():
        if v == value:
            del a_dictionary[key]
    # we can delete it in this way as well
    # a_ditionary.pop(key)
    return a_dictionary
