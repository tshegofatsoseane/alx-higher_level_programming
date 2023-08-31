#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print number of elements of a list.

    Args:
        my_list (list): The list to store elements to print.
        x (int): No of elements of my_list.

    Returns:
        Results
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
