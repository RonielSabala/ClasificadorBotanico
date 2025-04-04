import tkinter as tk
from tkinter import PhotoImage
from typing import Type

from .common.constants import RUTA_ICONO
from .common import estilos as Estilos


# - Variables para la ventana principal:

RAIZ = tk.Tk()
RAIZ.title("jbn")
RAIZ.iconphoto(True, PhotoImage(file=RUTA_ICONO))

WIDTH, HEIGTH = 750, 900
padx = int(1920 / 2 + WIDTH / 2 - WIDTH)
pady = int(1080 / 2 + HEIGTH / 2 - HEIGTH)
RAIZ.geometry(f"{WIDTH}x{HEIGTH}+{padx}+{pady}")
RAIZ.resizable(False, False)

# Contenedor para las escenas
CONTENEDOR = tk.Frame(RAIZ)
CONTENEDOR.pack(fill="both", expand=True)
CONTENEDOR.grid_rowconfigure(0, weight=1)
CONTENEDOR.grid_columnconfigure(0, weight=1)


class Escena:
    raiz: tk.Frame
    fue_cargada: bool = False
    escena_anterior: Type["Escena"] | None = None
    escena_posterior: Type["Escena"] | None = None
    color_fondo: str = "White"
    color_fondo_opaco: str = "Gray78"
    main_element: None | tk.Entry = None

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
        Muestra la escena.
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
        Coloca un texto con coordenadas relativas en la escena.
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
        Coloca un botón de retorno para ir a la escena
        anterior. Si se presiona ESC dicho botón es
        activado.
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
            fg=fg,
            bg=cls.color_fondo,
        )
        boton = tk.Button(
            cls.raiz,
            fg=fg,
            command=lambda: escape(None),
            activebackground=cls.color_fondo_opaco,
            **Estilos.btn_retorno,
        )

        cls.raiz.bind("<Escape>", escape)
        texto.place(relx=0.048, rely=0.13, anchor="nw")
        boton.place(relx=0.05, rely=0.05, anchor="nw")

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


def cerrar_escenas():
    """
    Cierra todas las escenas.
    """

    for escena in Escena.__subclasses__():
        escena.cerrar()
