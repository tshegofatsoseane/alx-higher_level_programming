#!/usr/bin/python3
"""Define square class."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize square.

        Args:
            size (int): The square size.
        """
        self.size = size

    @property
    def size(self):
        """Get and set size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparision of Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison of Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison of Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison of Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison of square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison of quare."""
        return self.area() >= other.area()
