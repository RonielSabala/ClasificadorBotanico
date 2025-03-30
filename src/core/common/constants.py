FLORES: tuple[str, ...] = (
    "rosa",
    "clavel",
    "girasol",
    "orquidea",
    "margarita",
)

COLUMNAS: tuple[str, ...] = (
    " ",
    "Subido por",
    "Apellido",
    "Ubicación",
    "Flor",
    "Predicción",
)

N_COLUMNAS = len(COLUMNAS)
COLUMNA_FLOR = COLUMNAS.index("Flor")
PREDICCION_PRESET = tuple((flor, 0) for flor in FLORES)
