from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from VentanaInicioSesion import ventana3
from VentanaInicioCliente import ventana6
from VentanaRegistro import ventana5

class opciones(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        # Creamos un atributo que cree la ventana anterior
        self.ventanaAnterior = anterior
        #Creamos atributo de ventana carpy
        # Le ponemos un titulo a la ventana
        self.setWindowTitle("Opciones de inicio")
        # Poner el color de fondo de la ventana
        self.setWindowIcon(QIcon('Logo/carpy.png'))  # Reemplaza 'icono.png' con la ruta de tu propio archivo de icono

        self.imagen = QLabel(self)

        self.imagenPantalla = QPixmap("Logo/fondo humilde.jpeg")
                # Establecemos el modo para escalar la imagen
        self.imagen.setPixmap(self.imagenPantalla)

        self.imagen.setScaledContents(True)
        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagen.width(), self.imagen.height())
        # Establecemos la ventana imagen como la ventana central
        self.setCentralWidget(self.imagen)
        # Establecemos las propiedades de ancho y alto
        self.ancho = 600
        self.alto = 400

        # Establecer el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana aparezca en el centro de la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # La ventana no se le pueda modificar el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.letra1 = QFont()
        self.letra1.setFamily("Gabriola")
        self.letra1.setPointSize(22)

        self.letra2 = QFont()
        self.letra2.setFamily("Gabriola")
        self.letra2.setPointSize(14)

        self.letrero1 = QLabel(self)
        self.letrero1.setText("¿CÓMO DESEAS INGRESAR?")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: white;")
        self.letrero1.move(170, 70)
        self.letrero1.setFixedWidth(1000)

        self.botonVolver = QPushButton(self)
        self.botonVolver.setText("←")
        self.botonVolver.setFont(self.letra2)
        self.botonVolver.setFixedWidth(40)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.move(10, 10)
        self.botonVolver.setStyleSheet("color : black;"
                                       "background-color : white;"
                                       "border-radius :20px;")


        self.botonIngresarCliente = QPushButton(self)
        self.botonIngresarCliente.setText("Ingresar como cliente")
        self.botonIngresarCliente.setFont(self.letra2)
        self.botonIngresarCliente.setFixedWidth(170)
        self.botonIngresarCliente.move(300, 270)
        self.botonIngresarCliente.setStyleSheet("color : black;"
                                  "background-color : white;"
                                  "border-radius :20px;")

        self.botonIngresarCarpy = QPushButton(self)
        self.botonIngresarCarpy.setText("Ingresar como carpy")
        self.botonIngresarCarpy.setFont(self.letra2)
        self.botonIngresarCarpy.setFixedWidth(170)
        self.botonIngresarCarpy.move(100, 270)
        self.botonIngresarCarpy.setStyleSheet("color : black;"
                                  "background-color : white;"
                                  "border-radius :20px;")
        
        self.botonRegistrarse = QPushButton(self)
        self.botonRegistrarse.setText("Registrarse")
        self.botonRegistrarse.setFont(self.letra2)
        self.botonRegistrarse.setFixedWidth(120)
        self.botonRegistrarse.move(230, 320)
        self.botonRegistrarse.setStyleSheet("color : black;"
                                       "background-color : white;"
                                       "border-radius :20px;")

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/cliente.png")
                # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(130)
        self.logoFondo.setFixedHeight(110)
        self.logoFondo.setStyleSheet("background-color: none;")
        self.logoFondo.move(334, 130)

        self.logoCarpintero = QLabel(self)
        self.logo = QPixmap("Logo/carpintero.png")
                # Establecemos el modo para escalar la imagen
        self.logoCarpintero.setPixmap(self.logo)
        self.logoCarpintero.setFixedWidth(200)
        self.logoCarpintero.setFixedHeight(200)
        self.logoCarpintero.setStyleSheet("background-color: none;")
        self.logoCarpintero.move(50, 80)
        
        # Conectamos los botones
        self.botonIngresarCarpy.clicked.connect(self.accion_botonIngresarCarpy)
        self.botonVolver.clicked.connect(self.accion_botonVolver)
        self.botonIngresarCliente.clicked.connect(self.accion_botonIngresarCliente)
        self.botonRegistrarse.clicked.connect(self.accion_botonRegistrarse)
        
        self.botonIngresarCarpy.setCursor(Qt.PointingHandCursor)
        self.botonVolver.setCursor(Qt.PointingHandCursor)
        self.botonIngresarCliente.setCursor(Qt.PointingHandCursor)
        self.botonRegistrarse.setCursor(Qt.PointingHandCursor)

    def accion_botonVolver(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.ventanaAnterior.show()


    def accion_botonIngresarCarpy(self):
        # Ocultamos la ventana actual
        self.hide()

        # Creamos una instancia de la ventana3 (inicio de sesión)
        self.Ventana3 = ventana3(anterior=self, ventana_registro=None)

        # Creamos una instancia de la ventana5 (registro)
        ventana_registro = ventana5(anterior=self)

        # Asignamos la referencia de la ventana de registro a la ventana de inicio de sesión
        self.Ventana3.ventanaRegistro = ventana_registro

        # Mostramos la ventana de inicio de sesión
        self.Ventana3.show()

    def accion_botonIngresarCliente(self):
             # Ocultamos la ventana actual
             self.hide()
             # Creamos una ventana nueva
             self.VentanaInicioCliente = ventana6(self)
             # Mostramos la ventana nueva
             self.VentanaInicioCliente.show()

    def accion_botonRegistrarse(self):
                 # Ocultamos la ventana actual
                 self.hide()
                 self.VentanaRegistro = ventana5(self)
                 # Mostramos la ventana nueva
                 self.VentanaRegistro.show()

