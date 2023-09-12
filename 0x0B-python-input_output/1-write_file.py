i#!/usr/bin/python3
"""Define file writing function."""


def write_file(filename="", text=""):
    """Write str to UTF8 textfile.

    Args:
        filename (str): File name.
        text (str): Text.
    Returns:
        No of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
