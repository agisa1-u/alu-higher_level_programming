#!/usr/bin/python3
"""Module that defines a Student class with JSON export and reload."""


class Student:
    """A student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name: the first name of the student.
            last_name: the last name of the student.
            age: the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        Args:
            attrs: optional list of attribute names (strings). If given,
                only the attributes listed are retrieved; otherwise all.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace the attributes of the student from a dictionary.

        Args:
            json: a dictionary whose keys are public attribute names and
                whose values are the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
