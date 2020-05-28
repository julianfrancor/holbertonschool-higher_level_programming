#!/usr/bin/python3
"""Function that multiplies 2 matrices by using the module NumPy"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """Arguments:
    m_a: [must be an list of lists of integers or floats]
    m_b: [must be an list of lists of integers or floats]
    """
    return(numpy.matmul(m_a, m_b))
