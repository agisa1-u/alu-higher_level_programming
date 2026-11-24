#!/usr/bin/python3
"""Module that defines a function writing a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file (overwriting any content).

    Args:
        filename: the path of the file (created if it doesn't exist).
        text: the string to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
