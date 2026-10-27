#!/usr/bin/env python3
"""Define una clase Square que representa un cuadrado."""


class Square:
    """Representa un cuadrado."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            return "\n" 

        for nro in range(self.__size):
            print("#" * self.__size)

