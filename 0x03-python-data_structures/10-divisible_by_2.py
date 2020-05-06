#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new_list = my_list.copy()
    i = 0
    while my_list[i]:
        if i % 2 == 0:
            new_list[i] = FALSE
            i += 1
        else:
            new_list[i] = TRUE
            i += 1
    return new_list
