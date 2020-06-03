#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    Args:
        filename: string
        nb_lines: intiger
    for goes in range nb_lines + 1 to take into account inclusive
    that last line
    """
    with open(filename, mode="r", encoding="UTF8") as file:
        if nb_lines > 0:
            for i in range(0, nb_lines + 1):
                print(file.readline(), end='')
        else:
            print(file.read(), end='')
