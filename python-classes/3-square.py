#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''A simple class representing a square.'''

    def __init__(self, size=0):
        '''Initializes the square with a given size.'''
        self.size = size  # Using the setter for validation

    @property
    def size(self):
        '''Getter for the size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for the size of the square.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Calculates the area of the square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns a string representation of the square.'''
        return f"Square with size {self.__size} and area {self.area()}"


if __name__ == "__main__":
    my_square = Square(5)
    print(my_square)  # Print the information about this square
