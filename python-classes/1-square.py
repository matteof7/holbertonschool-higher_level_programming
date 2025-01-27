#!/usr/bin/python3
class Square:
    """A class that defines a square with a private attribute `size`."""

    def __init__(self, size):
        """
        Initializes a Square instance with a private attribute `size`.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
