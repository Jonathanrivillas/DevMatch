import sys

from Opciones import opciones
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QApplication, QPushButton
from PyQt5.QtCore import Qt


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

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

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/carpy.png")
                # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(250)
        self.logoFondo.setFixedHeight(250)
        self.logoFondo.setStyleSheet("background-color: none;")
        self.logoFondo.move(165, 20)

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



        self.letrero2 = QLabel(self)
        self.letrero2.setText("Bienvenido a carpentry in your hands☻")
        self.letrero2.setFont(self.letra2)
        self.letrero2.setStyleSheet("color: white;")
        self.letrero2.move(140, 270)
        self.letrero2.setFixedWidth(600)


        self.boton1 = QPushButton(self)
        self.boton1.setText("Ir a la selección de usuarios")
        self.boton1.setFont(self.letra1)
        self.boton1.setFixedWidth(250)
        self.boton1.move(170,350)
        self.boton1.setStyleSheet("color : black;"
                                  "background-color : white;"
                                  "border-radius :20px;")
        self.boton1.setCursor(Qt.PointingHandCursor)

        self.boton1.clicked.connect(self.accion_boton1)

    def accion_boton1(self):
         # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.Opciones = opciones(self)
        # Mostramos la ventana nueva
        self.Opciones.show()

if __name__ == '__main__':
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Creamos un objeto de tipo ventana 1 con el nombre de ventana1
    ventana1 = Ventana1()

    # Hacer que el objeto ventana 1 se muestre
    ventana1.show()
    # Para que se pueda cerrar
    sys.exit(app.exec_())