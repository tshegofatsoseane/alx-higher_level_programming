#!/usr/bin/python3
"""Define a class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize new Rectangle.

        Args:
            width (int): The new Rectangle width.
            height (int): The new Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
