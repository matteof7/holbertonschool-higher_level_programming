#!/usr/bin/python3
"""
This module defines a function that writes an Object to a text file,
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize and write to the file.
        filename (str): The name of the file to write to.
    """
    # Convert sets to lists for JSON serialization
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
