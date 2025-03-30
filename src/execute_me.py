from core import main
import core.menu.file
import core.formulario.file
import core.sobre_nosotros.file
import core.sobre_nosotros.terminos.file
import core.sobre_nosotros.politicas.file
import core.sobre_nosotros.preguntas.file
import core.tabla.file


# Iniciar la ventana mostrando el menú
core.menu.file.Menu.mostrar()

# Asociar la accion de cerrar la ventana con cerrar todas las escenas
main.RAIZ.protocol("WM_DELETE_WINDOW", main.cerrar_escenas)

# Bucle de la ventana
main.RAIZ.mainloop()
