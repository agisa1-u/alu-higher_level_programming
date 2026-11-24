#!/usr/bin/python3
"""Module that defines a function inserting text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a text after each line of a file containing a given string.

    Args:
        filename: the path of the UTF-8 text file to update.
        search_string: the string to look for in each line.
        new_string: the text inserted after each line that matches.
    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                if not line.endswith("\n"):
                    f.write("\n")
                f.write(new_string)
        f.truncate()
