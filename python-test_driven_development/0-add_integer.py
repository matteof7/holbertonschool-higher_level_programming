#!/usr/bin/python3
"""
This module defines the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the integer result.
    Raises a TypeError if either argument is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
