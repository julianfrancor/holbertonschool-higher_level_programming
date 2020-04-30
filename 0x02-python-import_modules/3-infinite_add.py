#!/usr/bin/python3

if __name__ == "__main__":  # Your code should not be executed when imported
    from sys import argv

    result = 0

    if len(argv) == 1:
        print(result)
    elif len(argv) == 2:
        result = int(argv[1])
        print('{:d}'.format(result))
    elif len(argv) > 2:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print('{:d}'.format(result))
