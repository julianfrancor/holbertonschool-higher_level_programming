#!/usr/bin/python3
"""[summary]"""


def matrix_mul(m_a, m_b):
    """[summary]

    Arguments:
            m_a: [must be an list of lists of integers or floats]
            m_b: [must be an list of lists of integers or floats]

    Raises:
            TypeError: [m_a must be a list]
            TypeError: [m_b must be a list]
            TypeError: [m_a can't be empty]
            TypeError: [m_b can't be empty]
            TypeError: [m_a must be a list of lists]
            TypeError: [m_b must be a list of lists]
            TypeError: [m_a should contain only integers or floats]
            ValueError: [m_b should contain only integers or floats]
            ValueError: [each row of m_a must be of the same size]
            TypeError: [each row of m_b must be of the same size]
            TypeError: [m_a and m_b can't be multiplied]
    """

    m_c = []
    m_temp = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for a in m_a:
        if not isinstance(a, list):
            raise TypeError("m_a must be a list of lists")
        elif len(a) == 0:
            raise ValueError("m_a can't be empty")
        for i in a:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for b in m_b:
        if not isinstance(b, list):
            raise TypeError("m_b must be a list of lists")
        elif len(b) == 0:
            raise ValueError("m_b can't be empty")
        for j in b:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a) is 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0:
        raise ValueError("m_b can't be empty")

    if len(set([len(row) for row in m_a])) is not 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set([len(row) for row in m_b])) is not 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            m_temp.append(sum)
        m_c.append(m_temp)
        m_temp = []

    return(m_c)
