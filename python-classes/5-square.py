#!/usr/bin/python3
'''Module for Square class'''


class Square:
    '''A class representing a square.'''

    def __init__(self, size=0):
        '''Initialize the square with a given size.'''
        self.size = size  # Use the setter to validate size

    @property
    def size(self):
        '''Retrieve the size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square with validation.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        '''Print the square using the character #.'''
        if self.size == 0:
            print()  # Print an empty line if size is 0
            return

        # Print each row of the square
        for _ in range(self.size):
            print("#" * self.size)


# Example usage of the Square class
if __name__ == "__main__":
    square = Square(3)
    square.my_print()  # Print the square
    print(f"Area: {square.area()}")  # Print the area
