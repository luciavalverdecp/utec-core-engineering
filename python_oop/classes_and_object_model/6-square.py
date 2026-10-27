#!/usr/bin/env python3
"""Define una clase Square que representa un cuadrado."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Obtiene la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición del cuadrado."""
        if (type(value) is not tuple or len(value) != 2
                or any(type(n) is not int or n < 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime el cuadrado en stdout."""
        print(self, end="\n\n")

    def __str__(self):
        """Devuelve la representación del cuadrado como una cadena."""
        lines = [""] * self.__position[0]

        for _ in range(self.__size):
            lines.append(" " * self.__position[1] + "#" * self.__size)

        return "\n".join(lines)