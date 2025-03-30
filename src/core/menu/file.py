import tkinter as tk
from tkinter import font

# Escenas
from ..imagenes.file import F_BANNER
from ..main import (
    RAIZ,
    Escena,
    Estilos,
    cerrar_escenas,
    hacer_reactivo,
)


class Menu(Escena):
    @classmethod
    def mostrar(cls) -> None:
        cls.configurar_escenas()
        super().mostrar()

    @classmethod
    def cerrar(cls) -> None:
        RAIZ.destroy()

    @classmethod
    def configurar_escenas(cls):
        from ..formulario.file import Formulario

        Formulario.escena_anterior = cls

    @classmethod
    def cargar(cls) -> None:
        from ..formulario.file import Formulario
        from ..sobre_nosotros.file import SobreNosotros
        from ..tabla.file import Tabla

        cls.colocar_footer()

        # - Header:

        tk.Label(cls.raiz, image=F_BANNER, bg=cls.color_fondo).pack(padx=10, pady=5)
        cls.colocar_textoXY(
            "Presidencia de la República: www.presidencia.gob.do",
            9,
            (0.5, 0.01),
            anchor="center",
            fg="black",
        )
        cls.colocar_texto("Flor survey", 35, pady=10, fg="#091518")
        cls.colocar_texto(
            "Estamos realizando una investigación a nivel nacional para calcular\n"
            + "la cantidad de flores de cada tipo que tienen las personas en sus\n"
            + "hogares.",
            12,
            pady=25,
            fg="#091518",
        )
        cls.colocar_texto("_" * 70, 10, pady=0, fg="#091518")
        cls.colocar_texto(
            "¿Te gustaría participar?",
            15,
            pady=25,
            fg="#091518",
        )
        cls.colocar_texto(
            "Solo tienes que completar la siguiente encuesta:",
            13,
            pady=3,
            fg="#091518",
        )
        cls.colocar_texto("", 13, pady=15, fg="#091518")

        # - Creación de los botones:

        boton_formulario = tk.Button(
            cls.raiz,
            text="Llenar encuesta",
            command=Formulario.mostrar,
            **Estilos.boton_primario,
        )
        boton_registros = tk.Button(
            cls.raiz,
            text="📝",
            font=("Arial", 50),
            fg="ivory4",
            activeforeground="Gray20",
            width=2,
            border=0,
            command=Tabla.mostrar,
            **Estilos.fondo(cls),
        )
        boton_sobre_nosotros = tk.Button(
            cls.raiz,
            text="❀",
            font=("Arial", 50),
            fg="springGreen4",
            activeforeground="violetred4",
            width=2,
            border=0,
            command=SobreNosotros.mostrar,
            **Estilos.fondo(cls),
        )
        boton_salir = tk.Button(
            cls.raiz,
            text="Salir",
            font=font.Font(family="Arial", size=18, underline=True),
            fg="Red3",
            activeforeground="black",
            relief="sunken",
            border=0,
            command=cerrar_escenas,
            **Estilos.fondo(cls),
        )

        # - Configuraciones de los botones:

        boton_formulario.pack(pady=0)

        # Botón registros
        x, y = 0.5, 0.73
        boton_registros.place(relx=x, rely=y, anchor="center")
        cls.colocar_textoXY(
            "Registros", 14, (x - 0.01, y + 0.06), anchor="center", fg="black"
        )

        # Botón de sobre nosotros
        x, y = 0.1, 0.9
        boton_sobre_nosotros.place(relx=x, rely=y, anchor="center")
        cls.colocar_textoXY(
            "Sobre\nnosotros", 14, (x, y + 0.06), anchor="center", fg="black"
        )

        # Botón de salir
        x, y = 0.92, 0.94
        boton_salir.place(relx=x, rely=y, anchor="center")
        cls.colocar_textoXY(
            "⥱", 25, (x, y + 0.04), anchor="center", fg=boton_salir.cget("fg")
        )

        # Botones reactivos
        hacer_reactivo(
            boton_salir,
            boton_registros,
            boton_sobre_nosotros,
        )
