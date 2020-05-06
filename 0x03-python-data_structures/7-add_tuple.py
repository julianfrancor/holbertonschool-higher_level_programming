#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = tuple_a
    new_tuple_b = tuple_b
	# conditional to check the number of elements in the tuple
    if (len(tuple_a)) > 2:
        new_tuple_a = tuple_a[0:2]
    # if the elements are less than 2, set the empty spaces to zero
    if (len(tuple_a)) < 2:
        new_tuple_a = tuple_a + (0, 0)
    # conditional to check the number of elements in the tuple
    if (len(tuple_b)) > 2:
        new_tuple_b = tuple_b[0:2]
    # if the elements are less than 2, set the empty spaces to zero
    if (len(tuple_b)) < 2:
        new_tuple_b = tuple_b + (0, 0)
    # In this, we add inbuilt sum() to perform summation
    # and zip the like indices using zip() and extend
    # logic to both tuples using map().
    tuple_a = tuple(map(sum, zip(new_tuple_a, new_tuple_b)))
    return tuple_a
