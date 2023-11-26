#!/usr/bin/python3

def add_integer(a, b=98):
    """ Function that add two integers.

    Arguments:
        a: 1st integer.
        b: 2nd integer with default value 98.

    Raises:
        TypeError if a and b are not int or float.

    Returns:
        The sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (it, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
