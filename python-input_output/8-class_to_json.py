#!/usr/bin/python3
"""Module that defines a function giving the dictionary of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: an instance of a class whose attributes are all serializable
            (list, dictionary, string, integer and boolean).
    """
    return obj.__dict__.copy()
