import tkinter as tk
from tkinter import font, PhotoImage
from typing import Any, Type


# Variables de la ventana principal.
# |
# v

RAIZ = tk.Tk()
RAIZ.title("jbn")
RAIZ.iconphoto(True, PhotoImage(file="core\\imagenes\\icono.png"))

WIDTH, HEIGTH = 750, 900
padx = int(1920 / 2 + WIDTH / 2 - WIDTH)
pady = int(1080 / 2 + HEIGTH / 2 - HEIGTH)
RAIZ.geometry(f"{WIDTH}x{HEIGTH}+{padx}+{pady}")
RAIZ.resizable(False, False)

# Contenedor para las escenas.
# |
# v

CONTENEDOR = tk.Frame(RAIZ)
CONTENEDOR.pack(fill="both", expand=True)
CONTENEDOR.grid_rowconfigure(0, weight=1)
CONTENEDOR.grid_columnconfigure(0, weight=1)


def obtener_conexion():
    pass


def hacer_reactivo(*botones):
    """
    Hace que cuando se pase el mouse por encima del boton
    se cambie el tipo de mouse.
    """

    def func(boton):
        boton.bind("<Enter>", lambda event: boton.config(cursor="hand2"))
        boton.bind("<Leave>", lambda event: boton.config(cursor="arrow"))

    for boton in botones:
        func(boton)


class Estilos:
    """
    Clase para almacenar estilos.
    """

    boton_primario = {
        "bd": 0,
        "font": ("Arial", 26, "bold"),
        "fg": "black",
        "bg": "goldenrod1",
        "activeforeground": "black",
        "activebackground": "goldenrod3",
        "cursor": "hand2",
        "padx": 5,
        "pady": 2,
        "relief": "flat",
    }

    boton_añadir = {
        "bd": 0,
        "font": ("Arial", 16, "bold"),
        "fg": "white",
        "bg": "SpringGreen4",
        "activeforeground": "white",
        "activebackground": "Dark Green",
        "cursor": "hand2",
        "padx": 10,
        "pady": 5,
        "relief": "flat",
    }

    boton_eliminar = {
        "bd": 0,
        "font": ("Arial", 16, "bold"),
        "fg": "white",
        "bg": "#b22222",
        "activeforeground": "white",
        "activebackground": "#8b0000",
        "cursor": "hand2",
        "padx": 10,
        "pady": 5,
        "relief": "flat",
    }

    texto_subrayado = {
        "font": font.Font(family="Arial", size=12, underline=True),
        "fg": "DodgerBlue3",
        "activeforeground": "goldenrod1",
        "relief": "sunken",
        "border": 0,
    }

    @staticmethod
    def fondo(escena: Type["Escena"]) -> dict[str, Any]:
        return {
            "bg": escena.color_fondo,
            "activebackground": escena.color_fondo,
        }


class Escena:
    raiz: tk.Frame
    main_element: None | tk.Entry = None
    escena_anterior: Type["Escena"] | None = None
    escena_posterior: Type["Escena"] | None = None
    color_fondo: str = "White"
    color_fondo_opaco: str = "Gray78"
    fue_cargada: bool = False

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        # Asignar un Frame del contenedor a cada subclase
        cls.raiz = tk.Frame(CONTENEDOR)
        cls.raiz.grid(row=0, column=0, sticky="nsew")

    @classmethod
    def cargar(cls) -> None:
        """
        Carga la escena con todos sus elementos.
        """

        ...

    @classmethod
    def cerrar(cls) -> None:
        """
        Cuando se va a cerrar la escena principal
        se llama a esta función para guardar información
        relevante de la escena en cuestión.
        """

        ...

    @classmethod
    def salir(cls) -> None:
        """
        Esta función se llama cada vez que se pasa
        de la escena actual a una escena anterior.
        """

        ...

    @classmethod
    def mostrar(cls) -> None:
        """
        Cambia la escena a la escena usada.
        """

        if cls.fue_cargada is False:
            cls.cargar()
            cls.fue_cargada = True

        cls.raiz.tkraise()
        cls.raiz.focus_set()
        cls.raiz.config(bg=cls.color_fondo)
        item = cls.main_element
        if item is not None:
            item.focus_set()

            if isinstance(item, tk.Entry):
                item.icursor(tk.END)

    @classmethod
    def resetear(cls) -> None:
        """
        Resetea la escena dejandola en blanco.
        """

        cls.raiz.destroy()
        cls.raiz = tk.Frame(CONTENEDOR)
        cls.raiz.grid(row=0, column=0, sticky="nsew")

    @classmethod
    def configurar_escenas(cls):
        """
        Configura las relaciones entre las escenas
        anteriores y posteriores de las escenas
        involucradas en la escena actual.
        """
        ...

    @classmethod
    def colocar_texto(
        cls, texto: str, tamaño: int, pady: int = 10, fg: str = "cornsilk2"
    ) -> None:
        """
        Coloca un texto en la escena.
        """

        tk.Label(
            cls.raiz,
            text=texto,
            font=("Arial", tamaño),
            bg=cls.color_fondo,
            fg=fg,
            pady=pady,
        ).pack()

    @classmethod
    def colocar_textoXY(
        cls,
        texto: str,
        tamaño: int = 10,
        coords: tuple[float, float] = (0.5, 0.5),
        anchor: str = "se",
        fg: str = "white",
    ) -> None:
        """
        Coloca un texto con coordenadas relativas.
        """

        label = tk.Label(
            cls.raiz,
            text=texto,
            font=("Arial", tamaño),
            bg=cls.color_fondo,
            fg=fg,
        )

        label.place(relx=coords[0], rely=coords[1], anchor=anchor)  # type: ignore

    @classmethod
    def colocar_retorno(cls, fg: str = "Black") -> None:
        """
        Coloca un botón de retorno para ir a la escena anterior.

        También existe la posibilidad de presionar ESC para ejecutar
        la misma funcionalidad
        """

        if cls.escena_anterior is None:
            return

        def escape(event) -> None:
            cls.escena_anterior.mostrar()  # type: ignore
            cls.salir()

        texto = tk.Label(
            cls.raiz,
            text="Volver",
            font=("Arial", 12),
            bg=cls.color_fondo,
            fg=fg,
        )

        boton = tk.Button(
            cls.raiz,
            text="↵",
            font=("Arial", 25),
            bg=cls.color_fondo,
            fg=fg,
            activebackground=cls.color_fondo_opaco,
            command=lambda: escape(None),
            width=2,
            border=0,
            relief="flat",
        )

        cls.raiz.bind("<Escape>", escape)
        texto.place(relx=0.048, rely=0.13, anchor="nw")
        boton.place(relx=0.05, rely=0.05, anchor="nw")
        hacer_reactivo(boton)

    @classmethod
    def colocar_footer(cls):
        cls.colocar_textoXY(
            "Jardín Botánico Nacional\n©2025 Todos los derechos reservados.",
            9,
            (0.5, 0.98),
            anchor="center",
            fg="black",
        )

    @classmethod
    def obtener_grid(cls):
        return tk.Frame(cls.raiz, bg=cls.color_fondo)


def cargar_escenas():
    """
    Carga todas las escenas.
    """

    for escena in Escena.__subclasses__():
        escena.cargar()


def cerrar_escenas():
    """
    Cierra todas las escenas.
    """

    for escena in Escena.__subclasses__():
        escena.cerrar()
