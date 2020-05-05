#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in matrix:
            for elem in row:
                print(elem, end=' ')
            print()
