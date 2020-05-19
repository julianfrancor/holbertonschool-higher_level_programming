#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(args[0], args[1])
        return result
    except (ZeroDivisionError, IndexError) as julian:
        print("Exception: {}".format(julian), file=sys.stderr)

"""
Write a function that executes a function safely.
Prototype: def safe_function(fct, *args):
You can assume fct will be always a pointer to a function
Returns the result of the function,
Otherwise, returns None if something happens during the function
and prints in stderr the error precede by Exception:
You have to use try: / except:

"""
