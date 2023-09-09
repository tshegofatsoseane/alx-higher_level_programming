#!/usr/bin/python3
"""A square-printing function."""

def print_square(size):
    """Print # character square.

    Args:
        size (int): The height or width of square.
    Raises:
        TypeError: If size is not int.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
