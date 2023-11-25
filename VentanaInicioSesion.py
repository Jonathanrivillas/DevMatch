import sys

from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget
from VentanaPerfil import ventana4
from VentanaRegistro import ventana5

class ventana3(QMainWindow):
    def __init__(self, anterior, ):
        super().__init__()

        # Creamos un atributo que cree la ventana anterior
        self.ventanaAnterior = anterior
        # Poner el titulo
        self.setWindowTitle("INICIO DE SESIÓN")
        self.setWindowIcon(QIcon('Logo/carpy.png'))  # Reemplaza 'icono.png' con la ruta de tu propio archivo de icono

        #Imagen de fondo
        self.imagen = QLabel(self)

        self.imagenPantalla = QPixmap("Logo/fondo humilde.jpeg")
                # Establecemos el modo para escalar la imagen
        self.imagen.setPixmap(self.imagenPantalla)

        self.imagen.setScaledContents(True)
        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagen.width(), self.imagen.height())
        # Establecemos la ventana imagen como la ventana central
        self.setCentralWidget(self.imagen)



        # Establecemos ancho y alto
        self.ancho = 700
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Para que no se pueda mover el tamaño de la ventana
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Centramos la ventana en la pantalla
        self.pantalla = self.frameGeometry()

        self.centro = QDesktopWidget().availableGeometry().center()

        self.pantalla.moveCenter(self.centro)

        self.move(self.pantalla.topLeft())

        self.letra1 = QFont()
        self.letra1.setFamily("Gabriola")
        self.letra1.setPointSize(20)

        self.letra2 = QFont()
        self.letra2.setFamily("Gabriola")
        self.letra2.setPointSize(14)



        self.letrero2 = QLabel(self)
        self.letrero2.setText("Correo")
        self.letrero2.setFont(self.letra2)
        self.letrero2.setStyleSheet("color: white; background-color: none")
        self.letrero2.move(230, 270)
        self.letrero2.setFixedWidth(250)

        self.editEmail = QLineEdit(self)
        self.editEmail.setFixedWidth(250)
        self.editEmail.move(230,300)
        self.editEmail.setStyleSheet("background-color: white")

        self.letrero3 = QLabel(self)
        self.letrero3.setText("Contraseña")
        self.letrero3.setFont(self.letra2)
        self.letrero3.setStyleSheet("color: white; background-color: none")
        self.letrero3.move(230, 350)
        self.letrero3.setFixedWidth(250)

        self.editPassword = QLineEdit(self)
        self.editPassword.setFixedWidth(250)
        self.editPassword.move(230,380)
        self.editPassword.setStyleSheet("background-color: white")
        self.editPassword.setEchoMode(QLineEdit.Password)

        self.botonIniciarSesion = QPushButton(self)
        self.botonIniciarSesion.setText("Iniciar sesión")
        self.botonIniciarSesion.setFont(self.letra2)
        self.botonIniciarSesion.setFixedWidth(120)
        self.botonIniciarSesion.move(300,450)
        self.botonIniciarSesion.setStyleSheet("color : #FFFFFF"
                                  "background-color : black;"
                                  "border-radius :20px;")

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/carpy.png")
                # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(250)
        self.logoFondo.setFixedHeight(250)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(220, 20)


        self.botonVolver = QPushButton(self)
        self.botonVolver.setText("←")
        self.botonVolver.setFont(self.letra2)
        self.botonVolver.setFixedWidth(40)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.move(10, 10)
        self.botonVolver.setStyleSheet("color : #FFFFFF"
                                       "background-color : black;"
                                       "border-radius :20px;")


        self.botonIniciarSesion.clicked.connect(self.accion_botonIniciarSesion)
        self.botonVolver.clicked.connect(self.accion_botonVolver)

    def accion_botonIniciarSesion(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.VentanaPerfil = ventana4(self)
        # Validamos si el numero ingresado son espacios en blanco

        # Mostramos la ventana nueva
        self.VentanaPerfil.show()
    def accion_botonVolver(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.ventanaAnterior.show()

