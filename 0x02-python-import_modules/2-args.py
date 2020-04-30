#!/usr/bin/python3

if __name__ == "__main__":  # Your code should not be executed when imported
    from sys import argv  # to import the module sys and the function argv
# print the head part where we say how many arguments where passed
    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print('{:d} argument:'.format(len(argv) - 1))
    elif len(argv) > 2:
        print('{:d} arguments:'.format(len(argv) - 1))

# print the bottom part where we display each of the arguments
    for i in range(1, len(argv)):
        print('{:d}: {}'.format(i, argv[i]))
