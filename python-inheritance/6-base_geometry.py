#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area() method."""


class BaseGeometry:
    """A geometry base class."""

    def area(self):
        """Raise an Exception: area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
