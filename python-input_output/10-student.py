#!/usr/bin/python3
"""Module defining a Student class
"""

class Student:
    """Class to define a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.
        
        If attrs is a list of strings, only attribute names contained in this
        list are retrieved. Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        
        # Create a dictionary with only the requested attributes
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
