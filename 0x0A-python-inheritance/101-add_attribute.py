#!/usr/bin/python3
"""Define a function to add attributes to objs."""


def add_attribute(obj, att, value):
    """Add an attribute to object.

    Args:
        obj (any): Object to add attribute.
        att (str): The attribute name  to add to object.
        value (any): The value of att.
    Raises:
        TypeError: Attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
