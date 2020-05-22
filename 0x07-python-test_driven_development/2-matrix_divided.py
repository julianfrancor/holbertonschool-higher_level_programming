#!/usr/bin/python3

"""Function that returns the sum of two intigers
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

    Args:
            matrix (list) must be a list of lists of integers or floats,
            div (int or float) must be a number (integer or float)

    Raise error exceptions:
            TypeError: matrix must be a matrix (list of lists) of integers/floats
            TypeError: Each row of the matrix must have the same size
            TypeError: div must be a number
            ZeroDivisionError: division by zero

    Returns:
            Returns a new matrix
    """
    error_type_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    error_length = "Each row of the matrix must have the same size"
    error_type_div = "div must be a number"
    error_div_zero = "division by zero"

    length = len(matrix[0])
    if length is 0:
        raise TypeError(error_type_matrix)

    for row in matrix:
        if length != len(row):
            raise TypeError(error_length)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_type_matrix)

    if type(div) not in [int, float]:
        raise TypeError(error_type_div)
    if div is 0:
        raise ZeroDivisionError(error_div_zero)

    return [[round(float(element)/float(div), 2) for element in row] for row in matrix]




