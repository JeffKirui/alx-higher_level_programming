#!/usr/bin/python3
"""
Module of Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ initializing self """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def __str__(self):
        """ returns str """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
