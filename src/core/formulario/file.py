import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil

# Escenas
from ..main import Escena, Estilos, hacer_reactivo
from ..menu.file import Menu
from ..imagenes.file import F_ICONO
from ..data.file import (
    n_archivos,
    agregar_registro,
    obtener_ruta,
)
from .validaciones import (
    validar_nombre,
    validar_apellido,
    validar_ubicacion,
    validar_imagen,
    DEFAULT_TEXT,
)


# Variables
var_nombre = tk.StringVar()
var_apellido = tk.StringVar()
var_ubicacion = tk.StringVar()
var_imagen = tk.StringVar()
ruta_imagen = ""


# Validación de campos.


def guardar_formulario() -> None:
    """
    Guarda y valida la información del formulario.
    """

    nombre = var_nombre.get()
    apellido = var_apellido.get()
    ubicacion = var_ubicacion.get()

    # Validar campos
    if not (
        validar_nombre(nombre)
        and validar_apellido(apellido)
        and validar_ubicacion(ubicacion)
        and validar_imagen(ruta_imagen)
    ):
        return

    try:
        extension = ruta_imagen.split(".")[-1]
        ruta = obtener_ruta(f"flor_survey_{n_archivos()}.{extension}")
        data = [
            nombre,
            apellido,
            ubicacion,
            ruta,
            None,
        ]

        agregar_registro(str(data))
        shutil.copy(ruta_imagen, ruta)

    except Exception as e:
        messagebox.showerror(
            f"Error",
            f"Se produjo el siguiente error al guardar el formulario: {e}",
        )

        return

    # Cambiar de escena
    if escena := Formulario.escena_anterior:
        escena.mostrar()


class Formulario(Escena):
    escena_anterior = Menu

    @classmethod
    def mostrar(cls) -> None:
        global ruta_imagen

        ruta_imagen = ""
        var_nombre.set("")
        var_apellido.set("")
        var_ubicacion.set("")
        var_imagen.set(DEFAULT_TEXT)
        super().mostrar()

    @classmethod
    def cargar(cls) -> None:
        global ruta_imagen

        cls.colocar_retorno("Black")
        cls.colocar_footer()

        # Header
        tk.Label(cls.raiz, image=F_ICONO, bg=cls.color_fondo).pack(padx=10, pady=15)
        cls.colocar_texto("Formulario", 35, pady=15, fg="#091518")
        cls.colocar_texto("", 0, pady=15)

        # Creación de los campos y botones.
        # |
        # v

        # Estilo de los textos
        tamaño = 22
        color = "Black"
        estilo_campo = {
            "width": 22,
            "font": ("Arial", 18),
            "fg": "black",
            "bg": cls.color_fondo,
            "selectforeground": "Black",
            "selectbackground": "GoldenRod1",
        }

        # Campos
        campo_nombre = tk.Entry(
            cls.raiz,
            textvariable=var_nombre,
            **estilo_campo,
        )
        campo_apellido = tk.Entry(
            cls.raiz,
            textvariable=var_apellido,
            **estilo_campo,
        )
        campo_ubicacion = tk.Entry(
            cls.raiz,
            textvariable=var_ubicacion,
            **estilo_campo,
        )
        campo_imagen = tk.Entry(
            cls.raiz,
            textvariable=var_imagen,
            state="readonly",
            cursor="arrow",
            **estilo_campo,
        )
        boton_guardar = tk.Button(
            cls.raiz,
            text="Guardar",
            command=lambda: guardar_formulario(),
            **Estilos.boton_primario,
        )

        # Configuraciones de los campos y botones.
        # |
        # v

        # Establecer el campo principal
        cls.main_element = campo_nombre

        # Campo de usuario
        cls.colocar_texto("Nombre", tamaño, fg=color)
        campo_nombre.pack()
        campo_nombre.bind("<Escape>", lambda event: cls.raiz.focus_set())
        campo_nombre.bind("<Down>", lambda event: campo_apellido.focus_set())
        campo_nombre.bind("<Return>", lambda event: campo_apellido.focus_set())

        # Campo de appellido
        cls.colocar_texto("", 2)
        cls.colocar_texto("Apellido", tamaño, fg=color)
        campo_apellido.pack()
        campo_apellido.bind("<Escape>", lambda event: cls.raiz.focus_set())
        campo_apellido.bind("<Up>", lambda event: campo_nombre.focus_set())
        campo_apellido.bind("<Down>", lambda event: campo_ubicacion.focus_set())
        campo_apellido.bind("<Return>", lambda event: campo_ubicacion.focus_set())

        # Campo de ubicación
        cls.colocar_texto("", 2)
        cls.colocar_texto("Ubicación", tamaño, fg=color)
        campo_ubicacion.pack()
        campo_ubicacion.bind("<Escape>", lambda event: cls.raiz.focus_set())
        campo_ubicacion.bind("<Up>", lambda event: campo_apellido.focus_set())

        # - Campo de imagen:

        def seleccionar_imagen():
            global ruta_imagen

            ruta_imagen = filedialog.askopenfilename(
                title="Selecciona una imagen",
                filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")],
            )

            if not ruta_imagen:
                return

            campo_imagen.config(state="normal")
            campo_imagen.delete(0, tk.END)
            campo_imagen.insert(0, ruta_imagen.split("/")[-1])
            campo_imagen.config(state="readonly")

        cls.colocar_texto("", 2)
        cls.colocar_texto("Imagen", tamaño, fg=color)
        campo_imagen.pack(padx=10, pady=10)
        campo_imagen.bind("<Button-1>", lambda event: seleccionar_imagen())
        campo_imagen.bind("<Escape>", lambda event: cls.raiz.focus_set())
        campo_imagen.bind("<Up>", lambda event: campo_ubicacion.focus_set())
        campo_imagen.bind("<Return>", lambda event: boton_guardar.invoke())
        hacer_reactivo(campo_imagen)

        # Botón de guardar
        boton_guardar.pack(pady=40)
