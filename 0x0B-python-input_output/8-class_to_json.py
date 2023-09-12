#!/usr/bin/python3
"""Define a Python class-to-JSON function."""


def class_to_json(obj):
    """Print dictionary represntation of data structure."""
    return obj.__dict__
