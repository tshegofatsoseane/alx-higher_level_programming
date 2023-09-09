#!/usr/bin/python3
"""Module to find the the highest integer in a list
"""

def max_integer(list=[]):
    """Funcfor finding and returning the highest integer in a list.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
