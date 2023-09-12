#!/usr/bin/python3
"""Define a file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Append text after each line containing a given.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
