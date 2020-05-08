#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
# define the dictionary
    r_dictionary = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50),
                         ('C', 100), ('D', 500), ('M', 1000)])
# define a variable number_int where we will store the number to return
    number_int = 0
# the bult-in zip let us run the for with two variables
    for current_num, next_num in zip(roman_string, roman_string[1:]):
        # if the current number is less than the next one, substract
        if r_dictionary[current_num] < r_dictionary[next_num]:
            number_int -= r_dictionary[current_num]
# if the current number is bigger than the next one or equal, sum
        else:
            number_int += r_dictionary[current_num]
# we have to add the last number of the string cuz we didn't evaluate that
    number_int += r_dictionary[roman_string[-1]]
    return number_int
