#!/usr/bin/python3

""" Matrix divider module. """


def matrix_divided(matrix, div):
    """ Divide all elements in the matrix by div. """
    # Create a new list
    new_list = []

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Loop over the matrix to check the contents
    for content in matrix:
        # if one row of the matrix is bigger than the other, raise error
        if len(content) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        # Check the elements inside the row of the matrix
        for element in content:
            if not isinstance(element, (int, float)):
                raise TypeError(
                        "matrix must be a matrix(list of lists) of integers/floats")

    new_element = list(map(lambda el: round(el / div, 2), content))
    new_list.append(new_element)
