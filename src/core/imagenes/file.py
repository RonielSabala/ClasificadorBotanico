from PIL import Image, ImageTk


def obtener_imagen(ruta_imagen: str):
    return ImageTk.PhotoImage(Image.open(ruta_imagen))


def redimensionar_imagen(ruta_imagen: str):
    size = 128

    imagen = Image.open(ruta_imagen).convert("RGBA")
    base = Image.new("RGBA", (size, size), (0, 0, 0, 0))  # type: ignore

    ancho_original, alto_original = imagen.size
    ratio = min(size / ancho_original, size / alto_original)
    nuevo_ancho = int(ancho_original * ratio)
    nuevo_alto = int(alto_original * ratio)

    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

    pos_x = (size - nuevo_ancho) // 2
    pos_y = (size - nuevo_alto) // 2

    base.paste(imagen_redimensionada, (pos_x, pos_y), imagen_redimensionada)
    return ImageTk.PhotoImage(base)


RUTA = "core\\imagenes\\"

# Imagenes
ICONO = f"{RUTA}icono.png"
ESCUDO = f"{RUTA}escudo.png"
BANNER = f"{RUTA}banner.png"
VACIO = f"{RUTA}vacio.png"
F_ICONO = obtener_imagen(ICONO)
F_ESCUDO = obtener_imagen(ESCUDO)
F_BANNER = obtener_imagen(BANNER)
F_VACIO = redimensionar_imagen(VACIO)
