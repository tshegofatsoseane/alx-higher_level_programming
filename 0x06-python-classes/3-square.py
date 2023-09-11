#!/usr/bin/python3
"""Define square class ."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): The square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)
