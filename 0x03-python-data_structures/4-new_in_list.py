#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list) - 1)):
        return my_list
    else:
        # if I put  new_list = my_list I'm working in the same list
        # that's why I have to copy it
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
