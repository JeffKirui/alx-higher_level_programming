#!/usr/bin/python3
""" Defining rectangle based on 3-rectangle. """


class Rectangle:
    """ Defining Rectangle class. """

    def __init__(self, width=0, height=0):
        """ Intializing self. """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getting width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getting height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Defining area. """
        return self.__height * self.__width

    def perimeter(self):
        """ Defining perimeter. """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ Defining str. """
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return str1
        str1 += ("#" * self.__width + "\n") * self.__height
        return str1[:-1]

    def __repr__(self):
        """ Defining repr. """
        str1 = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return str1
