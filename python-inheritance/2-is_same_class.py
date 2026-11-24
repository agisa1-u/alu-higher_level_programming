#!/usr/bin/python3
"""Module that defines a function checking for an exact class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: the object to check.
        a_class: the class to compare to.
    """
    return type(obj) is a_class
