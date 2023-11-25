import sys

from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget


class ventana12(QMainWindow):
    def __init__(self, anterior,):
        super(ventana12, self).__init__()
        self.ventanaAnterior = anterior
        # Poner el titulo
        self.setWindowTitle("Reseñas")
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

        self.letra1 = QFont()
        self.letra1.setFamily("Gabriola")
        self.letra1.setPointSize(18)

        self.letra2 = QFont()
        self.letra2.setFamily("Gabriola")
        self.letra2.setPointSize(14)

        self.letrero1 = QLabel(self)
        self.letrero1.setText("Calificación:")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setStyleSheet("color: white; background-color: none")
        self.letrero1.move(190, 100)
        self.letrero1.setFixedWidth(250)

        self.letrero2 = QLabel(self)
        self.letrero2.setText("⭐⭐⭐⭐")
        self.letrero2.setFont(self.letra1)
        self.letrero2.setStyleSheet("color: white; background-color: none")
        self.letrero2.move(190, 130)
        self.letrero2.setFixedWidth(250)

        self.letrero3 = QLabel(self)
        self.letrero3.setText("Calificación:")
        self.letrero3.setFont(self.letra1)
        self.letrero3.setStyleSheet("color: white; background-color: none")
        self.letrero3.move(190, 310)
        self.letrero3.setFixedWidth(250)

        self.letrero4 = QLabel(self)
        self.letrero4.setText("⭐⭐⭐")
        self.letrero4.setFont(self.letra1)
        self.letrero4.setStyleSheet("color: white; background-color: none")
        self.letrero4.move(190, 340)
        self.letrero4.setFixedWidth(250)

        self.letrero5 = QLabel(self)
        self.letrero5.setText('Es muy eficaz en su trabajo\n pero llegó un poco tarde')
        self.letrero5.setFont(self.letra2)
        self.letrero5.setStyleSheet("color: white; background-color: none")
        self.letrero5.move(190, 160)
        self.letrero5.setFixedWidth(500)
        self.letrero5.setFixedHeight(70)

        self.letrero6 = QLabel(self)
        self.letrero6.setText("Trabaja muy rápido y muy pulido \n sin embargo dejo un poco sucio el lugar de trabajo")
        self.letrero6.setFont(self.letra2)
        self.letrero6.setStyleSheet("color: white; background-color: none")
        self.letrero6.move(190, 350)
        self.letrero6.setFixedWidth(500)
        self.letrero6.setFixedHeight(100)

        self.letrero7 = QLabel(self)
        self.letrero7.setText("Usuario: Camila Andrea Muñoz")
        self.letrero7.setFont(self.letra1)
        self.letrero7.setStyleSheet("color: white; background-color: none")
        self.letrero7.move(190, 80)
        self.letrero7.setFixedWidth(500)

        self.letrero8 = QLabel(self)
        self.letrero8.setText("Usuario: Pedro Pablo Londoño")
        self.letrero8.setFont(self.letra1)
        self.letrero8.setStyleSheet("color: white; background-color: none")
        self.letrero8.move(190, 290)
        self.letrero8.setFixedWidth(500)

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/TRABAJO3.jpg")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(200)
        self.logoFondo.setFixedHeight(200)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(20, 70)

        self.logoFondo1 = QLabel(self)
        self.logo = QPixmap("Logo/TRABAJO4.jpg")
        # Establecemos el modo para escalar la imagen
        self.logoFondo1.setPixmap(self.logo)
        self.logoFondo1.setFixedWidth(300)
        self.logoFondo1.setFixedHeight(200)
        self.logoFondo1.setStyleSheet("background-color: none")
        self.logoFondo1.move(20, 290)

        self.botonVolver = QPushButton(self)
        self.botonVolver.setText("←")
        self.botonVolver.setFont(self.letra2)
        self.botonVolver.setFixedWidth(40)
        self.botonVolver.setFixedHeight(40)
        self.botonVolver.move(10, 10)
        self.botonVolver.setStyleSheet("color : #FFFFFF"
                                       "background-color : black;"
                                       "border-radius :20px;")

        self.botonVolver.clicked.connect(self.accion_botonVolver)

    def accion_botonVolver(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.ventanaAnterior.show()
