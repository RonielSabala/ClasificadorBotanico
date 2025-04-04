import tkinter as tk
from tkinter import scrolledtext

# Escenas
from ....main import Page
from ..main import Contacto


info = """
Los presentes términos de uso (en lo que sigue, los "Términos de Uso") regulan los servicios del portal web "http://www.jbn.gob.do" (en lo que sigue, el "Portal") del organismo gubernamental "Jardín Botánico Nacional Dr. Rafael ma.Moscoso" (en lo que sigue, "Jardin Botanico Nacional"), creado en fecha 26 de Abril del año 2014, bajo la dirección de la División de Tecnologías de la Información y Comunicación (en lo que sigue, "Division TIC"), del Organismo Gubernamental, institución gubernamental con dependencia directa del Poder Ejecutivo, creada mediante el ley No. 456, de fecha 26 de diciembre del año 1976, con su domicilio y oficina principal en la Av. República de Colombia esq. Av. Los Próceres, Sector los Altos de Galá, Santo Domingo, D.N. República Dominicana.

El uso del Portal le otorga la condición de usuario del Portal (en lo que sigue, el "Usuario") e implica la aceptación plena y sin reservas de todas y cada una de las disposiciones establecidas en los Términos de Uso y las Políticas publicadas por el Organismo Gubernamental al momento en que el Usuario acceda al Portal. Por lo tanto, se hace necesario que el Usuario lea detenidamente estos términos en cada ocasión en que utilice el Portal, ya que este puede sufrir modificaciones sin previo aviso.

1.Objeto.- A través del Portal, el Organismo Gubernamental facilita a los Usuarios el acceso y el uso de los servicios, informaciones y contenidos (en lo que sigue, los "Servicios") colocados a disposición por el Organismo Gubernamental o por terceros.

2.Condiciones de Accesibilidad y Uso del Portal.

1.Carácter gratuito del acceso y uso del Portal.- La prestación de los Servicios, de parte del Jardín botánico Nacional, tiene carácter gratuito para el Usuario. Sin perjuicio de lo anterior, algunos de los Servicios suministrados por el Jardín Botánico Nacional a través del Portal podrían estar sujetos al pago de una tasa la cual estaría establecida en el mismo.

2.Registro del Usuario.- De manera general, la prestación de los Servicios no exige la suscripción o registro previo de parte del Usuario.

3.Veracidad de la información.- Toda información facilitada al Usuario mediante los Servicios deberá ser veraz. Por esto, el Usuario se compromete a garantizar el carácter auténtico de los datos que provea a consecuencia de los requisitos de los formularios necesarios para la suscripción de los Servicios. De igual forma, será responsabilidad del Usuario mantener toda la información facilitada al Jardín Botánico Nacional debidamente actualizada de manera tal que responda, en cada momento, a la situación real del Usuario. En todo caso el Usuario será el único responsable de las informaciones falsas o inexactas que realice y de los perjuicios que pueda causar el Jardín Botánico Nacional o a terceros por la información que suministre.

4.Propiedad Intelectual.- Todo el contenido de este Portal, ya sean textos, imágenes, recopilaciones, marcas, logotipos, combinaciones de colores, o cualquier otro elemento, su estructura y diseño, la selección y forma de presentación de los materiales incluidos en la misma, y los programas necesarios para su funcionamiento, acceso y uso, están protegidos por derechos de propiedad intelectual, de los cuales es titular el Jardín Botánico Nacional  o de terceros licenciantes, que el Usuario de este Portal debe respetar.

5.El Usuario del Portal deberá abstenerse de suprimir, alterar, eludir o manipular cualquier dispositivo de protección o sistema de seguridad que pueda estar instalado en el mismo.

3.Protección de los datos personales.- Para utilizar algunos de los Servicios, el Usuario debe facilitar previamente al Jardín Botánico Nacional algunos datos de carácter personal (en lo que sigue, los "Datos Personales").

1.El Jardín Botánico Nacional tratará de forma automática los Datos Personales con la finalidad y las condiciones, definidas en su Política de Privacidad. El Jardín Botánico Nacional  no garantiza la ausencia de virus ni de otros elementos en los Servicios prestados por terceros a través del Portal que puedan causar alteraciones en el sistema informático del Usuario (software y hardware) o en los documentos electrónicos y/o bases de datos de su sistema informático.

2.El Jardín Botánico Nacional ha adoptado los niveles de seguridad de protección que entiende necesarios y procura instalar los medios y medidas técnicas de protección que se vayan haciendo necesarias. Sin embargo, el Usuario debe estar consciente de que las medidas de seguridad en la Internet no son inviolables.

3.El Jardín Botánico Nacional puede utilizar cookies cuando un Usuario navega por los sitios y páginas Web del Portal. Las cookies que se puedan usar en los sitios y páginas Web del Portal se asocian únicamente con el navegador de un computador determinado (un Usuario anónimo), y no proporcionan en sí mismas el nombre y apellido del Usuario. Gracias a las "cookies", resulta posible que el Organismo Gubernamental reconozca los navegadores de los Usuarios registrados (luego de que éstos se hayan registrado por primera vez), esto ayuda que no tengan que registrarse cada vez que visita las áreas y los Servicios reservados exclusivamente a ellos. Las "cookies" utilizadas no pueden leer archivos "cookie" creados por otros proveedores. El Usuario tiene la posibilidad de configurar su navegador para ser avisado en su pantalla de la recepción de "cookies" y para impedir la instalación de las mismas en el disco duro.

4.Para utilizar el Portal no es indispensable la instalación de las "cookies" enviadas por el Jardín Botánico Nacional, sin perjuicio de que en tal caso puede ser necesario que el Usuario se registre cada vez que acceda a un Servicio que requiera un registro previo."""


class Terminos(Page):
    pagina_anterior = Contacto

    @classmethod
    def cargar(cls) -> None:
        # Header
        cls.colocar_retorno()
        cls.colocar_texto("", 0, pady=35)
        cls.colocar_texto("Términos De Uso", 30, pady=0, fg="#091518")
        cls.colocar_texto("", 0, pady=0)

        # Caja de texto
        box = scrolledtext.ScrolledText(cls.raiz, wrap=tk.WORD, width=50, height=12)
        box.pack(padx=85, pady=0, fill=tk.BOTH, expand=True)
        box.config(state=tk.NORMAL, font=("Arial", 10), bg="Gray95")
        box.insert(tk.END, info[1:])
        box.config(state=tk.DISABLED)
        cls.colocar_texto("", 0, pady=30)
