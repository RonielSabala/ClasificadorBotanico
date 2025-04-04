from app.UI import main
from app.UI.pages.menu.main import Menu


# Iniciar la ventana mostrando el menú
Menu.mostrar()

# Asociar la accion de cerrar la ventana con cerrar todas las páginas
main.RAIZ.protocol("WM_DELETE_WINDOW", main.close_pages)

# Bucle de la ventana
main.RAIZ.mainloop()
