#!/usr/bin/python3
""" Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Args:
        n (int): the depth of pascal's
    """
    lista = []
    if n <= 0:
        return lista
    if n == 1:
        lista = [1]
        return lista
    lista = [[1], [1, 1]]
    for i in range(1, n - 1):
        linea = [1]
        for j in range(0, len(lista[i]) - 1):
            linea.extend([lista[i][j] + lista[i][j + 1]])
        linea += [1]
        lista.append(linea)
    return lista
