#!/usr/bin/python3
"""Module that defines a function returning a JSON string of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation (string) of an object.

    Args:
        my_obj: the object to serialize.
    """
    return json.dumps(my_obj)
