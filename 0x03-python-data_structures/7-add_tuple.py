#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # conditional to check the number of elements in the tuple
    if (len(tuple_a)) > 2:
        tuple_a = tuple_a[0:2]
    # if the elements are less than 2, set the empty spaces to zero
    if (len(tuple_a)) < 2:
        tuple_a += (0, 0)
    # conditional to check the number of elements in the tuple
    if (len(tuple_b)) > 2:
        tuple_b = tuple_b[0:2]
    # if the elements are less than 2, set the empty spaces to zero
    if (len(tuple_b)) < 2:
        tuple_b += (0, 0)
    # In this, we add inbuilt sum() to perform summation
    # and zip the like indices using zip() and extend
    # logic to both tuples using map().
    return tuple(map(sum, zip(tuple_a, tuple_b)))
