#!/usr/bin/python3
"""Define an inherited class checking function."""


def inherits_from(obj, a_class):
    """Checks if object is inherited instance of class.

    Args:
        obj (any): The object.
        a_class (type): The class.
    Returns:
        If object inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
