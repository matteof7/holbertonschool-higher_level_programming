#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''Class that defines a rectangle'''
    def __init__(self, width=0, height=0):
        '''Initialization of instance attributes'''
        self.width = width
        self.height = height

    def _validate_dimension(self, value, name):
        '''Helper method to validate dimensions'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
        return value

    @property
    def width(self):
        '''Getter method for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width attribute'''
        self.__width = self._validate_dimension(value, "width")

    @property
    def height(self):
        '''Getter method for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height attribute'''
        self.__height = self._validate_dimension(value, "height")
