#!/usr/bin/python3

def no_c(my_string):
    """Remove all c and C characters in string"""
    new_string = ""
    for letter in my_string:
        if letter == "c" or letter == "C":
            continue
        new_string += letter

    return new_string
