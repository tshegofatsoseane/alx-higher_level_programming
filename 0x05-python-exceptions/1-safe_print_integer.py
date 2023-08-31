afe_print_integer(value):
    """Print int in "{:d}".format().

    Args:
        value (int): The print integer.

    Returns:
         Results 
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
