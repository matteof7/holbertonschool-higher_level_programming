#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''A class representing a square.'''

    def __init__(self, size=0):
        '''Initialize the square with a specified size.'''
        self.__set_size(size)  # Use a private method to set size

    def __set_size(self, value):
        '''Private method to set the size with validation.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def get_size(self):
        '''Getter method for size.'''
        return self.__size

    def set_size(self, value):
        '''Setter method for size with validation.'''
        self.__set_size(value)

    size = property(get_size, set_size)  # Create a property for size

    def area(self):
        '''Calculate and return the area of the square.'''
        return self.__size ** 2


# Example usage of the Square class
if __name__ == "__main__":
    square_instance = Square(4)
    print(f"Area: {square_instance.area()} for size: {square_instance.size}")

    # Change the size of the square
    square_instance.size = 10
    print(f"Area: {square_instance.area()} for size: {square_instance.size}")

    # Attempt to set an invalid size
    try:
        square_instance.size = -3  # This should raise an error
    except Exception as e:
        print(e)
