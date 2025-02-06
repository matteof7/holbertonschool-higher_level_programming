#!/usr/bin/python3
"""Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """__init__"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """__str__"""
        return "[Square] {}/{}".format(self.__size, self.__size)
