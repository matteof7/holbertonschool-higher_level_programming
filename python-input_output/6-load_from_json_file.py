#!/usr/bin/python3
"""
This module defines a function that creates an Object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The object represented by the JSON string in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
