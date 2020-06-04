#!/usr/bin/python3
""" Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Args:
        n (int): the depth of pascal's
    """
    lista = [[1], [1, 1]]
    for i in range(1, n-1):
        linea = [1]
        for j in range(0, len(lista[i])-1):
            linea.extend([lista[i][j] + lista[i][j+1]])
        linea += [1]
        lista.append(linea)
    return lista