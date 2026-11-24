#!/usr/bin/python3
"""Module that defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list with a method to print its elements in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order (list is unchanged)."""
        print(sorted(self))
