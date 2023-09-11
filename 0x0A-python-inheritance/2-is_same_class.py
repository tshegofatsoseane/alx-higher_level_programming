#!/usr/bin/python3
"""Define a class-checking function."""


def is_same_class(obj, a_class):
    """Check if object is instance of class.

    Args:
        obj (any): The object.
        a_class (type): The class.
    Returns:
        If object is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
