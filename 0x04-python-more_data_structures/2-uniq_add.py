#!/usr/bin/python3
def uniq_add(my_list=[]):

    # another way to do it
    #    b = set(my_list)
    #    number = 0
    #    for i in b:
    #        number += i
    #    return number
    return sum(set(my_list))
