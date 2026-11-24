#!/usr/bin/python3
"""Module that defines a function loading an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename: the path of the JSON file to read.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
