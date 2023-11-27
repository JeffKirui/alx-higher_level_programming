#!/usr/bin/python3
""" Defining rectangle based on 7-rectangle.py. """


class Rectangle:
    """ Defining Rectangle class. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializing self. """
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
        self.__class__.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ Prints the rectangle. """
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return str1
        str1 += (str(self.print_symbol) * self.__width + "\n") * self.__height
        return str1[:-1]

    def __repr__(self):
        """ Returns a representation of the rectangle. """
        str1 = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return str1

    def __del__(self):
        """ Defining delete. """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Defining bigger or equal. """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
