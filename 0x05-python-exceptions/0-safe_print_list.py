#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print number of elememts of a list.

    Args:
        my_list (list): List to store elements to print.
        x (int): No. of elements of my_list to print.

    Returns:
        No. of printed elements.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
