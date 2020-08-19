#!/usr/bin/python3

"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Timsort - function that finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return "None"
    lista = list_of_integers.copy()
    right = len(lista) - 1
    left = 0
    while left < right:
        mid = left + (right - left) // 2
        if (lista[mid] < lista[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return lista[left]
