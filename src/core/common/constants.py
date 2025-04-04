# - Rutas:

_RUTA = "core\\"

# Carpetas
RUTA_DATA = f"{_RUTA}data\\"
RUTA_IMGS = f"{_RUTA}graficos\\imagenes\\"

# Data guardada
DATA_IMGS = f"{RUTA_DATA}imagenes"
FORMULARIOS = f"{RUTA_DATA}formularios.txt"

# Imagenes
RUTA_ICONO = f"{RUTA_IMGS}icono.png"
RUTA_ESCUDO = f"{RUTA_IMGS}escudo.png"
RUTA_BANNER = f"{RUTA_IMGS}banner.png"
RUTA_VACIO = f"{RUTA_IMGS}vacio.png"


# Tamaño por defecto de despliege las imagenes (en pixeles)
IMG_SIZE = 128


# Texto por defecto para seleccionar una imagen
DEFAULT_IMG = "<Selecciona una imagen>"


# Tabla de registros:


COLUMNAS: tuple[str, ...] = (
    " ",
    "Subido por",
    "Apellido",
    "Ubicación",
    "Flor",
    "Predicción",
)

FILA_MAX = 4
COLUMNA_MAX = len(COLUMNAS)
COLUMNA_FLOR = COLUMNAS.index("Flor")
