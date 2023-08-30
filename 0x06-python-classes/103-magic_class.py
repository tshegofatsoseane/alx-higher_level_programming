#!/usr/bin/python3
"""Define MagicClass matching bytecode."""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize MagicClass.

        Arg:
            radius (float or int): The radius of MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return MagicClass area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return MagicClass circumference."""
        return (2 * math.pi * self.__radius)
