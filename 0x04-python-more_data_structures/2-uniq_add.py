#!/usr/bin/python3
def uniq_add(my_list=[]):
    b = set(my_list)
    number = 0
    for i in b:
        number += i
    return number
