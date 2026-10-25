#!/usr/bin/env python3
"""Modulo que define la funcion write_file."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo de texto UTF-8.

    Crea el archivo si no existe y sobrescribe su contenido si ya existe.

    Args:
        filename (str): nombre del archivo.
        text (str): cadena a escribir.

    Returns:
        int: numero de caracteres escritos.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
