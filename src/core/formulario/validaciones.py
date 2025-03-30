import os
from tkinter import messagebox


DEFAULT_TEXT = "<Selecciona una imagen>"


def validar_campo(campo: str, nombre: str) -> bool:
    """
    Devuelte verdadero si el campo es válido, de otro modo
    devuelve Falso y muestra un error personalizado.
    """

    validez = True
    mensaje = f"Ingrese {nombre}"

    if not campo:
        validez = False
        mensaje += "."

    elif len(campo) < 5:
        validez = False
        mensaje += " con 5 o más caracteres."

    elif len(campo) > 50:
        validez = False
        mensaje += " de 50 caracteres o menos."

    if not validez:
        messagebox.showerror("Error", mensaje)

    return validez


def validar_nombre(nombre: str) -> bool:
    return validar_campo(nombre, "un nombre")


def validar_apellido(apellido: str) -> bool:
    return validar_campo(apellido, "un apellido")


def validar_ubicacion(ubicacion: str) -> bool:
    return validar_campo(ubicacion, "una ubicacion")


def validar_imagen(ruta_imagen: str) -> bool:
    msg = ""
    es_valida = True
    if ruta_imagen == DEFAULT_TEXT:
        es_valida = False
        msg = "Ingrese una imagen."

    if not os.path.isfile(ruta_imagen):
        es_valida = False
        msg = "La ruta de la imagen es invalida."

    if not es_valida:
        messagebox.showerror("Error", msg)

    return es_valida
