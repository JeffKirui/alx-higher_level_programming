#!/usr/bin/python3
""" Module for print_square method. """


def print_square(size):
    """ Method for printing a square with # characters.

    Raise:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """

    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
