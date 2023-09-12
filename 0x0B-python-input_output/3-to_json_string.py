#!/usr/bin/python3
"""Defin string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Print JSON representation of str object."""
    return json.dumps(my_obj)
