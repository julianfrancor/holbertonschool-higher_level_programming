#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout
"""


def number_of_lines(filename=""):
    """
    with:
        It is good practice to use the "with" keyword when dealing with file objects.
        This has the advantage that the file is properly closed after its suite finishes,
        even if an exception is raised on the way.
        It is also much shorter than writing equivalent try-finally blocks

    in the open function we don't have to put explicit the mode to read "r"
    because by default if you don't put anything it will read.
    You just have to specify the mode for the write "w"
    Another way to do it:

    number_lines = 0
    for line in file:
            number_lines += 1
    return number_lines
    --------------------------
    number_lines = 0
        while file.readline():
            number_lines += 1
        return number_lines

    """
    with open("my_file_0.txt", mode="r", encoding="UTF8") as file:
        return len(file.readlines())
