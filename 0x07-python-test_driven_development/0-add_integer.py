#!/usr/bin/python3
# 0-add_integer.py
"""Integer addition function."""


def add_integer(a, b=98):
    """Integer addition of a and b.

    Raises:
        A or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("A must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("B must be an integer")
    return (int(a) + int(b))
