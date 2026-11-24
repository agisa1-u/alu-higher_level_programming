#!/usr/bin/python3
"""Module that defines a function appending a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file.

    Args:
        filename: the path of the file (created if it doesn't exist).
        text: the string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
