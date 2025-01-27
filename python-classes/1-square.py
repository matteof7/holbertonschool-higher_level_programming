#!/usr/bin/python3

'''
Module for the Square class
'''


class Square:
    '''A simple class representing a square.'''

    def __init__(self, size):
        '''Initializes the square with a given size.'''
        self.__size = size

    def area(self):
        '''Calculates the area of the square.'''
        return self.__size ** 2

if __name__ == "__main__":
    my_square = Square(5)
    print(f"The area of the square is: {my_square.area()}.")
