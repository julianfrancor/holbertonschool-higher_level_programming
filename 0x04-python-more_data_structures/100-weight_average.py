#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0
    denomiator = 0
    numerator = 0
    for tup in my_list:
        numerator += tup[0] * tup[1]
        denomiator += tup[1]
    result = numerator / denomiator
    return result
