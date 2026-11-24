#!/usr/bin/python3
"""Module that defines a Square class comparable by area."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: the size of the square (number >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: if value is not a number (float or integer).
            ValueError: if value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if the areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the areas are different."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this area is less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this area is less than or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this area is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this area is greater than or equal to the other."""
        return self.area() >= other.area()
