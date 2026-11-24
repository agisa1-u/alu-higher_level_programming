#!/usr/bin/python3
"""Module with the MagicClass, rewritten from Python bytecode."""
import math


class MagicClass:
    """A circle defined by its radius."""

    def __init__(self, radius=0):
        """Initialize the circle with a radius (int or float)."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
