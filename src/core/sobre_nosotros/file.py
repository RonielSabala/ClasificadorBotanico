import tkinter as tk

# Escenas
from ..main import Escena, hacer_reactivo
from ..menu.file import Menu
from ..imagenes.file import F_ESCUDO, F_ICONO


class SobreNosotros(Escena):
    escena_anterior = Menu

    # - Estilos:

    estilo_icono = {
        "font": ("Arial", 32),
        "fg": "DodgerBlue4",
    }
    estilo_titulo = {
        "font": ("Arial", 16, "bold"),
        "justify": "left",
        "anchor": "w",
        "padx": 7,
        "pady": 10,
    }
    estilo_info = {
        "width": 0,
        "border": 0,
        "font": ("Arial", 12),
        "justify": "left",
    }
    estilo_link = {
        "font": ("Arial", 13),
        "width": 0,
        "border": 0,
        "relief": "sunken",
        "fg": "SpringGreen4",
        "activeforeground": "violetred3",
        "activebackground": "White",
        "padx": 0,
        "pady": 0,
    }

    @classmethod
    def obtener_separacion(cls, frame, tamaño: int):
        return tk.Label(
            frame,
            text="|",
            font=("Arial", tamaño),
            fg="Gray20",
            bg=cls.color_fondo,
            padx=0,
        )

    @classmethod
    def cargar(cls) -> None:
        from .terminos.file import Terminos
        from .politicas.file import Politicas
        from .preguntas.file import Preguntas

        cls.colocar_retorno()
        cls.colocar_footer()

        # Grid del header
        grid_header = cls.obtener_grid()
        grid_header.pack(fill="none", padx=85, pady=40)
        grid_header.grid_rowconfigure(0, pad=45)
        grid_header.grid_columnconfigure(1, pad=0)

        # Grid del contenido
        grid = cls.obtener_grid()
        grid.pack(fill="none", expand=True, padx=85, pady=35)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_rowconfigure(1, pad=50)
        grid.grid_columnconfigure(1, pad=40)

        # Grid de los links
        grid_links = cls.obtener_grid()
        grid_links.pack(fill="y", padx=0, pady=100)

        # - Header:

        escudo = tk.Label(grid_header, image=F_ESCUDO, bg=cls.color_fondo)
        sep_header = cls.obtener_separacion(grid_header, 25)
        icono = tk.Label(grid_header, image=F_ICONO, bg=cls.color_fondo)
        titulo = tk.Label(
            grid_header,
            text="Jardín Botánico Nacional",
            font=("Arial", 30),
            bg=cls.color_fondo,
        )
        sub_titulo = tk.Label(
            grid_header,
            text="Dr. Rafael M. Moscoso",
            font=("Arial", 15),
            bg=cls.color_fondo,
        )

        # Estilos
        estilo_general = {"bg": cls.color_fondo}
        cls.estilo_icono.update(estilo_general)
        cls.estilo_titulo.update(estilo_general)
        cls.estilo_info.update(estilo_general)
        cls.estilo_link.update(estilo_general)

        # - Contenido:

        direccion = tk.Label(
            grid,
            text="📍",
            **cls.estilo_icono,
        )
        texto_direccion = tk.Label(
            grid,
            text="Dirección",
            **cls.estilo_titulo,
        )
        info_direccion = tk.Label(
            grid,
            text="Av. República de Colombia esq. Av. Los Próceres,\n"
            + "Sector los Altos de Galá, Santo Domingo, D.N.\n"
            + "República Dominicana",
            **cls.estilo_info,
        )

        telefono = tk.Label(
            grid,
            text="📞",
            **cls.estilo_icono,
        )
        texto_telefono = tk.Label(
            grid,
            text="Tel.",
            **cls.estilo_titulo,
        )
        info_telefono = tk.Label(
            grid,
            text="(809) 385-2611 Ext. 221",
            **cls.estilo_info,
        )

        email = tk.Label(
            grid,
            text="📧",
            **cls.estilo_icono,
        )
        texto_email = tk.Label(
            grid,
            text="Email",
            **cls.estilo_titulo,
        )
        info_email = tk.Label(
            grid,
            text="jardinbotanico@jbn.gob.do",
            **cls.estilo_info,
        )

        # - Links:

        terminos = tk.Button(
            grid_links,
            text="Términos De Uso",
            command=Terminos.mostrar,
            **cls.estilo_link,
        )
        politicas = tk.Button(
            grid_links,
            text="Políticas De Privacidad",
            command=Politicas.mostrar,
            **cls.estilo_link,
        )
        preguntas = tk.Button(
            grid_links,
            text="Preguntas Frecuentes",
            command=Preguntas.mostrar,
            **cls.estilo_link,
        )

        # Separadores para los links
        sep1 = cls.obtener_separacion(grid_links, 16)
        sep2 = cls.obtener_separacion(grid_links, 16)

        # - Configuración:

        hacer_reactivo(terminos, politicas, preguntas)

        # Header
        escudo.grid(row=0, column=0, sticky="nse")
        sep_header.grid(row=0, column=1, sticky="ns")
        icono.grid(row=0, column=2, sticky="nsw")
        titulo.grid(row=1, columnspan=3, sticky="nsew")
        sub_titulo.grid(row=2, columnspan=3, sticky="nsew", pady=6)

        # Dirección
        direccion.grid(row=0, column=0, sticky="nsew")
        texto_direccion.grid(row=0, column=1, sticky="nsew")
        info_direccion.grid(row=0, column=2, sticky="nsew")

        # Telefono
        telefono.grid(row=1, column=0, sticky="nsew")
        texto_telefono.grid(row=1, column=1, sticky="nsew")
        info_telefono.grid(row=1, column=2, sticky="nsw")

        # Email
        email.grid(row=2, column=0, sticky="nse")
        texto_email.grid(row=2, column=1, sticky="nsew")
        info_email.grid(row=2, column=2, sticky="nsw")

        # Links
        terminos.grid(row=0, column=0, sticky="nse")
        sep1.grid(row=0, column=1, sticky="ns")
        politicas.grid(row=0, column=2, sticky="ns")
        sep2.grid(row=0, column=3, sticky="ns")
        preguntas.grid(row=0, column=4, sticky="nsw")
