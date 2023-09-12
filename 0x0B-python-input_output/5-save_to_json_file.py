i#!/usr/bin/python3
"""Define SON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writ object to textfile using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
