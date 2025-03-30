import tkinter as tk
from tkinter import font
from tkinter import messagebox
from typing import Sequence
import math

# Escenas
from ..main import Escena, Estilos, hacer_reactivo
from ..formulario.file import Formulario
from ..menu.file import Menu
from ..imagenes.file import F_ICONO
from ..data.file import es_ruta, obtener_formularios, limpiar_registros, predecir_imagen
from ..imagenes.file import redimensionar_imagen, F_VACIO
from ..common.constants import COLUMNAS, N_COLUMNAS, COLUMNA_FLOR


N_LIMIT = 4


class Tabla(Escena):
    escena_anterior = Menu

    # Estilos
    estilo_flecha = {
        "fg": "Black",
        "bg": "white",
        "activeforeground": "DodgerBlue4",
        "activebackground": "white",
        "border": 0,
        "relief": "sunken",
    }

    # Variables
    _registros: list[Sequence]
    registros: list[Sequence]
    pagina: int = 0
    max_pagina: int = 0
    flecha_derecha: tk.Button
    flecha_izquierda: tk.Button
    var_filtro = tk.StringVar()
    ultimo_filtro = (None, None)
    categoria: str = COLUMNAS[1]
    cabezales: list[tk.Button] = []

    @classmethod
    def mostrar(cls) -> None:
        cls.configurar_escenas()
        cls.obtener_registros()
        cls.actualizar_registros()
        cls.actualizar_tabla()

    @classmethod
    def configurar_escenas(cls):
        Formulario.escena_anterior = cls

    @classmethod
    def salir(cls):
        cls.var_filtro.set("")
        cls.ultimo_filtro = None, None
        cls.main_element = None

    @classmethod
    def obtener_registros(cls) -> None:
        cls._registros = [()]
        for i, registro in enumerate(obtener_formularios(), start=1):
            cls._registros.append([f"{i}."] + registro)

    @classmethod
    def actualizar_registros(cls) -> None:
        if cls.ultimo_filtro[0] is None:
            registros = cls._registros.copy()
        else:
            # Filtrar los registros
            filtro = cls.var_filtro.get().lower()
            columna = COLUMNAS.index(cls.categoria)
            registros = [
                x
                for x in cls._registros
                if len(x) == 0 or filtro in str(x[columna]).lower()
            ]

        # - Completar los registros:

        n = len(registros)
        if n > N_LIMIT:
            for _ in range(N_LIMIT - (n - 1) % (N_LIMIT - 1) - 1):
                registros.append([" "] * N_COLUMNAS)

        cls.pagina = int(len(registros) != 1)
        cls.max_pagina = math.ceil((n - 1) / (N_LIMIT - 1))
        cls.registros = registros

    @classmethod
    def actualizar_tabla(cls):
        """
        Actualiza la tabla.
        """

        cls.fue_cargada = False
        cls.resetear()
        super().mostrar()

    @classmethod
    def pagina_anterior(cls):
        if cls.pagina == 1:
            cls.flecha_izquierda.config(state=tk.DISABLED)
            return

        cls.pagina -= 1
        cls.actualizar_tabla()

    @classmethod
    def pagina_siguiente(cls):
        if cls.pagina == cls.max_pagina:
            cls.flecha_derecha.config(state=tk.DISABLED)
            return

        cls.pagina += 1
        cls.actualizar_tabla()

    @classmethod
    def eliminar_registros(cls):
        if len(cls._registros) <= 1:
            return

        eleccion = messagebox.askyesno(
            "Confirmación",
            "¿Estas seguro de que quieres eliminar todo?\n"
            + "Esta acción no puede deshacerse.",
        )

        if not eleccion:
            return

        limpiar_registros()
        Menu.mostrar()

    @classmethod
    def cambiar_categoria(cls, nuevo_valor: str) -> None:
        if (ultimo_valor := cls.categoria) == nuevo_valor:
            return

        cls.categoria = nuevo_valor

        # Cambiar el estilo de los cabezales
        for cabezal in cls.cabezales:
            if (texto := cabezal["text"]) in (ultimo_valor, nuevo_valor):
                cabezal.config(
                    font=font.Font(
                        family="Arial",
                        size=16,
                        weight="bold",
                        underline=texto == nuevo_valor,
                    )
                )

    @classmethod
    def filtrar_registros(cls) -> None:
        temp = cls.registros.copy()
        filtro = cls.var_filtro.get(), cls.categoria
        if filtro != cls.ultimo_filtro:
            cls.ultimo_filtro = filtro
            cls.actualizar_registros()

            if temp == cls.registros:
                return

            cls.actualizar_tabla()

    @classmethod
    def boton_clasificar(cls, raiz, index: int) -> tk.Frame:
        bg = "white"
        grid = tk.Frame(raiz, bg=bg)
        grid.rowconfigure(0, weight=1)

        tk.Label(grid, text=f"N/A", font=("Arial", 13), bg=bg).grid(
            row=0, column=0, pady=5
        )

        def clasificar(linea: int) -> None:
            pagina = cls.pagina
            predecir_imagen(linea)
            cls.obtener_registros()
            cls.actualizar_registros()
            cls.pagina = pagina
            cls.actualizar_tabla()

        boton = tk.Button(
            grid,
            text="Clasificar",
            command=lambda valor=index: clasificar(valor),
            **Estilos.boton_primario,
        )
        boton.config(
            font=("Arial", 16, "bold"),
            fg="Black",
            bg=bg,
            activebackground=bg,
            activeforeground="VioletRed3",
        )
        boton.grid(row=2, column=0)

        return grid

    @classmethod
    def tabla_prediccion(cls, raiz, data) -> tk.Frame:
        grid = tk.Frame(raiz)

        # Cabezales
        for i, texto in enumerate(("Tag", "Probabilidad")):
            tk.Label(
                grid,
                text=texto,
                font=("Arial", 12 if i == 0 else 10, "bold"),
                fg="White" if i == 0 else "GoldenRod1",
                bg="Gray15",
            ).grid(row=0, column=i, sticky="nsew", padx=0)

        # Contenido
        for i, prediccion in enumerate(
            sorted(data, key=lambda item: item[1], reverse=True)
        ):
            for j, dato in enumerate(prediccion):
                if j == 0:
                    dato = dato.capitalize()
                else:
                    dato = f"{dato:.2%} " + ("✔" if i == 0 else "✗")

                tk.Label(
                    grid,
                    text=dato,
                    font=("Arial", 10),
                    fg="Black" if i == 0 else f"Gray{60 + 8*i}",
                    bg="GoldenRod1" if i == 0 else "White",
                ).grid(row=i + 1, column=j, sticky="nsew")

        return grid

    @classmethod
    def cargar(cls) -> None:
        cls.cabezales = []
        cls.colocar_retorno()
        cls.colocar_footer()
        tk.Label(cls.raiz, image=F_ICONO, bg=cls.color_fondo).pack(padx=20, pady=15)
        cls.colocar_texto("Registros", 32, pady=0, fg="#091518")
        cls.colocar_texto("", 0, pady=2)

        # Creación del grid
        grid = cls.obtener_grid()
        grid.pack(fill="both", padx=20, pady=0)

        # - Dibujar el grid principal:

        # Buscador
        buscador = tk.Entry(
            grid,
            textvariable=cls.var_filtro,
            font=("Arial", 18),
            selectforeground="Black",
            selectbackground="GoldenRod1",
            width=30,
        )
        buscador.grid(row=0, column=1, columnspan=3, sticky="nsew", padx=0, pady=10)
        buscador.bind("<Escape>", lambda event: cls.raiz.focus_set())
        buscador.bind("<Return>", lambda event: boton_buscar.invoke())
        if cls.ultimo_filtro[0] is not None:
            cls.main_element = buscador

        # Buscar
        boton_buscar = tk.Button(
            grid,
            text="Buscar",
            font=("Arial", 13),
            command=lambda: cls.filtrar_registros(),
            cursor="hand2",
        )
        boton_buscar.grid(row=0, column=4, sticky="w")

        # Dibujar filas
        index = (N_LIMIT - 1) * (cls.pagina - 1)
        for fila, data in enumerate(cls.registros[index : index + N_LIMIT + 1]):
            if fila == 0:
                data = COLUMNAS

            elif fila == N_LIMIT:
                break

            # Dibujar fila
            for columna, sub_data in enumerate(data):
                # Color de las filas
                fg, bg = "Black", cls.color_fondo
                if columna > 0:
                    if fila == 0:
                        # Cabezales
                        fg, bg = "white", "Dodgerblue4"
                    elif columna != N_COLUMNAS - 1 and sub_data != " ":
                        # Registros
                        bg = "Gray96" if fila % 2 else "Gray92"

                # Crear una imagen
                if fila > 0 and columna == COLUMNA_FLOR:
                    img = (
                        redimensionar_imagen(sub_data) if es_ruta(sub_data) else F_VACIO
                    )

                    elemento = tk.Label(grid, image=img)
                    elemento.image = img  # type: ignore

                # Crear un label o botón
                else:
                    fuente = "Arial", 16, "bold"

                    # Botón de predecir
                    if sub_data is None:
                        elemento = cls.boton_clasificar(
                            grid, int(cls.registros[index + fila][0][:-1])
                        )

                        elemento.grid(row=fila + 1, column=columna, padx=0, pady=1)

                        continue

                    # Predicciones
                    elif sub_data != " " and fila > 0 and columna == N_COLUMNAS - 1:
                        elemento = cls.tabla_prediccion(grid, sub_data)
                        elemento.config(bg=bg)
                        elemento.grid(row=fila + 1, column=columna)
                        continue

                    # Crear un label
                    elif fila > 0 or columna in (0, COLUMNA_FLOR, N_COLUMNAS - 1):
                        elemento = tk.Label(grid)
                        if fila > 0:
                            fuente = "Segoe UI Emoji", 13
                            if columna > 0:
                                elemento.config(cursor="xterm")

                    # Crear un botón
                    else:
                        if cls.categoria == sub_data:
                            fuente += ("underline",)

                        elemento = tk.Button(
                            grid,
                            border=0,
                            activeforeground="Black",
                            activebackground="DodgerBlue4",
                            cursor="hand2",
                            command=lambda valor=sub_data: cls.cambiar_categoria(valor),
                        )

                        cls.cabezales.append(elemento)

                    elemento.config(
                        text=sub_data,
                        font=fuente,
                        relief="flat",
                    )

                    # Anchor
                    if columna in (0, 1):
                        elemento.config(
                            anchor=(
                                "center"
                                if fila in (0, N_LIMIT)
                                else ("e" if columna == 0 else "w")
                            ),
                            padx=15,
                        )

                elemento.config(fg=fg, bg=bg)
                elemento.grid(
                    row=fila + 1,
                    column=columna,
                    sticky="nsew",
                    pady=1,
                )

        # - Creación del grid de navegación:

        grid_nav = cls.obtener_grid()
        grid_nav.pack(fill="none", padx=35, pady=0)

        # Flechas
        cls.flecha_izquierda = tk.Button(
            grid_nav,
            text="<",
            command=cls.pagina_anterior,
            font=("Arial", 24),
            **cls.estilo_flecha,
        )
        cls.flecha_izquierda.grid(row=0, column=0, sticky="nsew", padx=0, pady=5)

        # Número de páginas
        tk.Label(
            grid_nav,
            text=f"página {cls.pagina} de {cls.max_pagina}",
            fg="Black",
            bg=cls.color_fondo,
            font=("Arial", 14),
        ).grid(row=0, column=1, sticky="nsew", padx=0, pady=5)

        cls.flecha_derecha = tk.Button(
            grid_nav,
            text=">",
            command=cls.pagina_siguiente,
            font=("Arial", 24),
            **cls.estilo_flecha,
        )
        cls.flecha_derecha.grid(row=0, column=2, sticky="nsew", padx=0, pady=5)

        # - Configuración de las flechas:

        if cls.pagina <= 1:
            cls.flecha_izquierda.config(state=tk.DISABLED)
        else:
            hacer_reactivo(cls.flecha_izquierda)

        if cls.pagina >= cls.max_pagina:
            cls.flecha_derecha.config(state=tk.DISABLED)
        else:
            hacer_reactivo(cls.flecha_derecha)

        cls.colocar_texto("", 0, pady=2)

        # Boton Añadir
        boton_añadir = tk.Button(
            cls.raiz,
            text="✚ Añadir",
            command=Formulario.mostrar,
            **Estilos.boton_añadir,
        )
        boton_añadir.pack(pady=0)

        # Boton eliminar
        boton_eliminar = tk.Button(
            cls.raiz,
            text="✘ Eliminar (TODO)",
            command=cls.eliminar_registros,
            **Estilos.boton_eliminar,
        )
        boton_eliminar.pack(pady=12)
