#!/usr/bin/python3
"""
Define a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square instance
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square
        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
