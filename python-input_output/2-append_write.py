#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty string.
        text (str): The text to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
    