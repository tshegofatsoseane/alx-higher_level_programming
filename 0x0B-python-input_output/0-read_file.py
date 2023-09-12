#!/usr/bin/python3
"""Define a file reading function."""


def read_file(filename=""):
    """Print UTF8 text file content."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
