#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = my_list.copy()
    for i in my_list:
        if i % 2 > 0:
            new_list[i] = False
        else:
            new_list[i] = True
    return new_list
