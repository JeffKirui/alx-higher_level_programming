#!/usr/bin/python3

""" Module for say_my_name method. """

def say_my_name(first_name, last_name=""):
    """ Function that prints first and last names.

    Raises:
        TypeError if first or last name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
