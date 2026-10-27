#!/usr/bin/env python3
"""Define una clase Square que representa un cuadrado."""


class Square:
    """Representa un cuadrado."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = 

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @property
    def position(self):
        """Obtiene la posicion."""
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado."""
        print(str(self), end="\n")

    def __str__(self):
        """Devuelve el cuadrado como una cadena."""
        lines = [""] * self.__position[0]

        for _ in range(self.__size):
            lines.append(" " * self.__position[1] + "#" * self.__size)

        return "\n".join(lines)