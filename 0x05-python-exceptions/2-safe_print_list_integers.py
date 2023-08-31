afe_print_list_integers(my_list=[], x=0):
    """Print the first number of integer elements of a list.

    Args:
        my_list (list): The list to store elemts to print.
        x (int): No. of elements of my_list.

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
