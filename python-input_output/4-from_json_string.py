#!/usr/bin/python3
"""Module that defines a function building an object from a JSON string."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str: the JSON string to parse.
    """
    return json.loads(my_str)
