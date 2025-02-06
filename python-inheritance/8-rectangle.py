#!/usr/bin/python3
"""8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """__init__"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """__str__"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return area"""
        return self.__width * self.__height
