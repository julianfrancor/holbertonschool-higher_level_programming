#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    in the open function we don't have to put explicit the mode to read "r"
    because by default if you don't put anything it will read.
    You just have to specify the mode for the write "w"

    f = open('workfile', 'w')

    The first argument is a string containing the filename.
    The second argument is another string containing a few
    characters describing the way in which the file will be used.
    mode can be 'r' when the file will only be read, 'w' for only
    writing (an existing file with the same name will be erased),
    and 'a' opens the file for appending; any data written to the
    file is automatically added to the end. 'r+' opens the file for both reading and writing.
    The mode argument is optional; 'r' will be assumed if it’s omitted.
    """
    with open(filename, mode="r", encoding="UTF8") as file:
        print(file.read())
