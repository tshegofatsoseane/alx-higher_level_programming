#!/usr/bin/python3
"""Define base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """No implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a param as an int.

        Args:
            name (str): Parameterame.
            value (int): The param to validate.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is < or = 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
