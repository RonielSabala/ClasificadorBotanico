from core import main
from core.menu.file import Menu


# Iniciar la ventana mostrando el menú
Menu.mostrar()

# Asociar la accion de cerrar la ventana con cerrar todas las escenas
main.RAIZ.protocol("WM_DELETE_WINDOW", main.cerrar_escenas)

# Bucle de la ventana
main.RAIZ.mainloop()
