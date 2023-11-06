#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers on list in reverse order."""
    for i in my_list[::-1]:
        print("{:d}".format(i))
