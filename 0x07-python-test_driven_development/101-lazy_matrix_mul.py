#!/usr/bin/python3
"""A matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Give multiplication of 2 matrices.

    Args:
        m_a (list of ints/floats): The 1st matrix.
        m_b (list of ints/floats): The 2nd matrix.
    """

    return (np.matmul(m_a, m_b))
