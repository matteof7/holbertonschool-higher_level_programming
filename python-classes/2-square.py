#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''A simple class representing a square.'''

    def __init__(self, size=0):
        '''Initializes the square with a given size.'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private attribute

    def area(self):
        '''Calculates the area of the square.'''
        return self.__size ** 2  # Area calculation


# Example usage of the Square class
if __name__ == "__main__":
    my_square = Square(5)
    print(f"The area of the square is: {my_square.area()}.")
