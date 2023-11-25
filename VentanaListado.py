import sys

from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QApplication, QPushButton, QToolBar, QAction, QComboBox
from PyQt5.QtCore import QSize
from VentanaPerfilCarpy import ventana8
from VentanaPerfilCarpy2 import ventana10

class Ventana7(QMainWindow):
    def __init__(self, anterior):
        super(Ventana7, self).__init__()

        self.ventanaAnterior = anterior
        # Poner el titulo
        self.setWindowTitle("CARPRENTRY IN YOUR HANDS")
        self.setWindowIcon(QIcon('Logo/carpy.png'))  # Reemplaza 'icono.png' con la ruta de tu propio archivo de icono

        # Establecemos una imagen de fondo para toda la ventaa

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
        self.ancho = 600
        self.alto = 500

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
        self.letra1.setPointSize(18)

        self.letra2 = QFont()
        self.letra2.setFamily("Gabriola")
        self.letra2.setPointSize(20)

        self.letra3 = QFont()
        self.letra3.setFamily("Arial")
        self.letra3.setPointSize(12)

        self.letra4 = QFont()
        self.letra4.setFamily("Gabriola")
        self.letra4.setPointSize(14)

        # Creamos la barra de herramientas
        self.barraHerramientas = QToolBar("Barra de Herramientas")
        # Establecemos el tamaño de los iconos de las opciones
        self.barraHerramientas.setIconSize(QSize(40, 40))
        # Agregamos la barra de Herramientas
        self.addToolBar(self.barraHerramientas)
        self.barraHerramientas.setStyleSheet('background-image: url(Logo/fondo humilde.jpeg);')

        # Creamos la opcion para la opcion 1
        self.perfil = QAction(QIcon("Logo/LOGOSALIDA.jpg"), "Cerrar sesión", self)
        self.barraHerramientas.addAction(self.perfil)

        # Activamos las opciones para la barra de herramientas
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.letreroNombre = QLabel(self)
        self.letreroNombre.setText("Usuario: Laura Sofía Tovar")
        self.letreroNombre.setFont(self.letra1)
        self.letreroNombre.setStyleSheet("color: white;")
        self.letreroNombre.move(10, 70)
        self.letreroNombre.setFixedWidth(600)

        self.letreroListado = QLabel(self)
        self.letreroListado.setText("Listado Carpys:")
        self.letreroListado.setFont(self.letra1)
        self.letreroListado.setStyleSheet("color: white;")
        self.letreroListado.move(10, 120)
        self.letreroListado.setFixedWidth(600)

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/FOTO EDWARD2.jpg")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(100)
        self.logoFondo.setFixedHeight(150)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(20, 140)

        self.logoFondo2 = QLabel(self)
        self.logo = QPixmap("Logo/FOTO KARINA.jpeg")
        # Establecemos el modo para escalar la imagen
        self.logoFondo2.setPixmap(self.logo)
        self.logoFondo2.setFixedWidth(120)
        self.logoFondo2.setFixedHeight(120)
        self.logoFondo2.setStyleSheet("background-color: none")
        self.logoFondo2.move(20, 300)

        self.letreroNombreCarpy1 = QLabel(self)
        self.letreroNombreCarpy1.setText("Edward Muñoz Arrieta")
        self.letreroNombreCarpy1.setFont(self.letra1)
        self.letreroNombreCarpy1.setStyleSheet("color: white;")
        self.letreroNombreCarpy1.move(130, 170)
        self.letreroNombreCarpy1.setFixedWidth(600)
        
        
        self.letreroNombreCarpy2 = QLabel(self)
        self.letreroNombreCarpy2.setText("Santiago Arango Galeano")
        self.letreroNombreCarpy2.setFont(self.letra1)
        self.letreroNombreCarpy2.setStyleSheet("color: white;")
        self.letreroNombreCarpy2.move(130, 320)
        self.letreroNombreCarpy2.setFixedWidth(600)

        self.letreroCelular1 = QLabel(self)
        self.letreroCelular1.setText("Celular: 3128836269")
        self.letreroCelular1.setFont(self.letra3)
        self.letreroCelular1.setStyleSheet("color: white; background-color: none")
        self.letreroCelular1.move(130, 200)
        self.letreroCelular1.setFixedWidth(500)

        self.letreroCelular2 = QLabel(self)
        self.letreroCelular2.setText("Celular: 3014424125")
        self.letreroCelular2.setFont(self.letra3)
        self.letreroCelular2.setStyleSheet("color: white; background-color: none")
        self.letreroCelular2.move(130, 350)
        self.letreroCelular2.setFixedWidth(500)

        self.letreroCalificacion1 = QLabel(self)
        self.letreroCalificacion1.setText("⭐⭐⭐⭐⭐")
        self.letreroCalificacion1.setFont(self.letra3)
        self.letreroCalificacion1.setStyleSheet("color: white; background-color: none")
        self.letreroCalificacion1.move(130, 230)
        self.letreroCalificacion1.setFixedWidth(500)

        self.letreroCalificacion2 = QLabel(self)
        self.letreroCalificacion2.setText("⭐⭐⭐")
        self.letreroCalificacion2.setFont(self.letra3)
        self.letreroCalificacion2.setStyleSheet("color: white; background-color: none")
        self.letreroCalificacion2.move(130, 380)
        self.letreroCalificacion2.setFixedWidth(500)

        self.botonVerPerfil = QPushButton(self)
        self.botonVerPerfil.setText("Ir al perfil")
        self.botonVerPerfil.setFont(self.letra4)
        self.botonVerPerfil.setFixedWidth(70)
        self.botonVerPerfil.move(330, 200)
        self.botonVerPerfil.setStyleSheet("color : #FFFFFF"
                                       "background-color : black;"
                                       "border-radius :20px;")

        self.botonVerPerfil2 = QPushButton(self)
        self.botonVerPerfil2.setText("Ir al perfil")
        self.botonVerPerfil2.setFont(self.letra4)
        self.botonVerPerfil2.setFixedWidth(70)
        self.botonVerPerfil2.move(330, 350)
        self.botonVerPerfil2.setStyleSheet("color : #FFFFFF"
                                       "background-color : black;"
                                       "border-radius :20px;")

        self.botonVerPerfil.clicked.connect(self.accion_botonVerPerfil1)
        self.botonVerPerfil2.clicked.connect(self.accion_botonVerPerfil2)


    def accion_botonVerPerfil1(self):
            # Ocultamos la ventana actual
            self.hide()
            # Creamos una ventana nueva
            self.VentanaPerfilCarpy = ventana8(self)
            # Validamos si el numero ingresado son espacios en blanco

            # Mostramos la ventana nueva
            self.VentanaPerfilCarpy.show()



    def accion_botonVerPerfil2(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.VentanaPerfil = ventana10(self)
        # Validamos si el numero ingresado son espacios en blanco

        # Mostramos la ventana nueva
        self.VentanaPerfil.show()

    def accion_barraHerramientas(self, opcion):
        # Ocultamos la ventana actual
        self.hide()
        # Validamos la opcion que se pulso
        if opcion.text() == "Cerrar sesión":
            self.ventanaAnterior.show()
