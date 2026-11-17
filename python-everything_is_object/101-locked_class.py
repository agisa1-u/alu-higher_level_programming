#!/usr/bin/python3
"""Module that defines a LockedClass that only accepts first_name."""


class LockedClass:
    """A class that only allows the instance attribute first_name."""
    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        """Refuse every attribute except first_name."""
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        object.__setattr__(self, name, value)
