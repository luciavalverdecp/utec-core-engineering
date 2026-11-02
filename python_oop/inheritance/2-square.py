#!/usr/bin/env python3
"""Modulo cuadrado."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Clase cuadrado."""

    def __init__(self, size):
        """Constructor basico."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcula area."""
        return self.__size * self.__size

    def __str__(self):
        """Representacion texto."""
        return "[Square] {}/{}".format(self.__size, self.__size)
