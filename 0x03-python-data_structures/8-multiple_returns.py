#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tuple_a = len(sentence)
        tuple_b = None
        return tuple_a, tuple_b
    else:
        tuple_a = len(sentence)
        tuple_b = sentence[0]
        return tuple_a, tuple_b
