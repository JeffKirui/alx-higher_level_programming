#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print dictionary by ordered keys."""
    for i, s in sorted(a_dictionary.items(), key=lambda x: x[0]):
        print("{}: {}".format(i, s))
