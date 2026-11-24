#!/usr/bin/python3
"""Module that defines a function checking for a strict subclass."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    An instance of a_class itself does not count.

    Args:
        obj: the object to check.
        a_class: the class to compare to.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
