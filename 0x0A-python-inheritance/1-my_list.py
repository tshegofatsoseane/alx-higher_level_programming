#!/usr/bin/python3
"""Define an inherited list class MyList."""


class MyList(list):
    """Implement a sorted printing for built-in list class."""

    def print_sorted(self):
        """Return a list in sorted order."""
        print(sorted(self))
