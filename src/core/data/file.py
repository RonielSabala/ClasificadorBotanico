import os

from ..API.file import obtener_prediccion


RUTA = "core\\data\\"

# Rutas
IMAGENES = f"{RUTA}imagenes"
FORMULARIOS = f"{RUTA}formularios.txt"


def es_ruta(ruta: str) -> bool:
    """
    Devuelve verdadero si la ruta es valida.
    """

    return isinstance(ruta, str) and os.path.exists(ruta)


def agregar_registro(registro: str) -> None:
    """
    Guarda un registro en el archivo formularios.
    """

    with open(FORMULARIOS, "a") as f:
        f.write(f"{registro}\n")


def obtener_ruta(ruta: str):
    """
    Devuelve la ruta completa en
    la carpeta de imagenes.
    """

    ruta = os.path.join(IMAGENES, ruta)
    return ruta.replace("\\", "\\\\")


def obtener_imagenes():
    """
    Devuelve la ruta de todas las imagenes de
    la carpeta imagenes.
    """

    return (obtener_ruta(img) for img in os.listdir(IMAGENES))


def obtener_formularios() -> tuple[list, ...]:
    with open(FORMULARIOS, "r") as f:
        return tuple(list(eval(i.strip("\n"))) for i in f.readlines())


def n_archivos() -> int:
    """
    Devuelve el número de archivos de la carpeta imagenes.
    """

    return len(tuple(obtener_imagenes()))


def limpiar_registros():
    """
    Elimina todos los formularios e imagenes.
    """

    with open(FORMULARIOS, "w") as f:
        f.write("")

    for ruta in obtener_imagenes():
        try:
            os.unlink(ruta)

        except Exception as e:
            print(f"Error al eliminar {ruta}: {e}")


def predecir_imagen(linea: int):
    linea -= 1
    with open(FORMULARIOS, "r") as f:
        lineas = f.readlines()

    if 0 <= linea <= len(lineas) - 1:
        data = eval(lineas[linea])
        data[-1] = obtener_prediccion(data[-2])
        lineas[linea] = f"{data}\n"

        with open(FORMULARIOS, "w") as f:
            f.writelines(lineas)
    else:
        raise ValueError("Error: Número de línea fuera de rango.")
