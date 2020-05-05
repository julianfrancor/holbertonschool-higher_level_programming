#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Always check if a list is empty by its type flexibility.
    # we can treat a list like a boolean.
    if not my_list:
        return None
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
