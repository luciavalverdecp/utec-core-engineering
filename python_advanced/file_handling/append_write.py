#!/usr/bin/env python3
"""Modulo que define la funcion append_write."""


def append_write(filename="", text=""):
    """Agrega una cadena al final de un archivo de texto UTF-8.

    Crea el archivo si no existe.

    Args:
        filename (str): nombre del archivo.
        text (str): cadena a agregar.

    Returns:
        int: numero de caracteres agregados.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
