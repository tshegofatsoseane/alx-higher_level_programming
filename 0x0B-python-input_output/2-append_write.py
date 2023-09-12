#!/usr/bin/python3
"""Define file appending function."""


def append_write(filename="", text=""):
    """Append str to the end of UTF8 textfile.

    Args:
        filename (str): File name.
        text (str): The string.
    Returns:
        No of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
