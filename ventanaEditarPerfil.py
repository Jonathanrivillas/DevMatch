import sys

from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget, \
    QComboBox, QVBoxLayout, QFileDialog, QMessageBox


class ventana9(QMainWindow):
    def __init__(self, anterior):
        super(ventana9, self).__init__()
        self.ventanaAnterior = anterior

        # Poner el titulo
        self.setWindowTitle("EDITAR PERFIL")
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
        self.letra2.setPointSize(16)

        self.letra3 = QFont()
        self.letra3.setFamily("Arial")
        self.letra3.setPointSize(10)

        # Creamos el letrero registro
        self.letreroRegistrarse = QLabel(self)
        self.letreroRegistrarse.setText("Editar Perfil")
        self.letreroRegistrarse.setFont(self.letra1)
        self.letreroRegistrarse.setStyleSheet("color: white;")
        self.letreroRegistrarse.move(285, 70)
        self.letreroRegistrarse.setFixedWidth(300)

        self.letreroNombre = QLabel(self)
        self.letreroNombre.setText("NOMBRE COMPLETO")
        self.letreroNombre.setFont(self.letra2)
        self.letreroNombre.setStyleSheet("color: white;")
        self.letreroNombre.move(30, 110)
        self.letreroNombre.setFixedWidth(300)

        self.editNombre = QLineEdit(self)
        self.editNombre.setFixedWidth(200)
        self.editNombre.move(30, 140)
        self.editNombre.setFont(self.letra3)
        self.editNombre.setStyleSheet("background-color: white")

        self.letreroTipodeDocumento = QLabel(self)
        self.letreroTipodeDocumento.setText("SELECCIONA TIPO DE DOCUMENTO")
        self.letreroTipodeDocumento.setFont(self.letra2)
        self.letreroTipodeDocumento.setStyleSheet("color: white;")
        self.letreroTipodeDocumento.move(30, 190)
        self.letreroTipodeDocumento.setFixedWidth(300)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Cédula")
        self.comboBox.addItem("Cédula de Extranjería")
        self.comboBox.addItem("Pasaporte")
        self.comboBox.setFont(self.letra3)
        self.comboBox.move(30, 220)  # Ajusta la posición según sea necesario
        self.comboBox.setFixedWidth(200)  # Establece el ancho según sea necesario
        self.comboBox.setStyleSheet("background-color: white;")

        self.letreroNumeroDeDocumento = QLabel(self)
        self.letreroNumeroDeDocumento.setText("INGRESE EL NUMERO DEL DOCUMENTO")
        self.letreroNumeroDeDocumento.setFont(self.letra2)
        self.letreroNumeroDeDocumento.setStyleSheet("color: white;")
        self.letreroNumeroDeDocumento.move(30, 270)
        self.letreroNumeroDeDocumento.setFixedWidth(300)

        self.editNumeroDeDocumento = QLineEdit(self)
        self.editNumeroDeDocumento.setFixedWidth(200)
        self.editNumeroDeDocumento.move(30, 300)
        self.editNumeroDeDocumento.setFont(self.letra3)
        self.editNumeroDeDocumento.setStyleSheet("background-color: white")

        self.letreroCorreo = QLabel(self)
        self.letreroCorreo.setText("CORREO")
        self.letreroCorreo.setFont(self.letra2)
        self.letreroCorreo.setStyleSheet("color: white; background-color: none")
        self.letreroCorreo.move(30, 340)
        self.letreroCorreo.setFixedWidth(200)

        self.editCorreo = QLineEdit(self)
        self.editCorreo.setFixedWidth(200)
        self.editCorreo.move(30, 370)
        self.editCorreo.setStyleSheet("background-color: white")

        self.letreroCelular = QLabel(self)
        self.letreroCelular.setText("CELULAR")
        self.letreroCelular.setFont(self.letra2)
        self.letreroCelular.setStyleSheet("color: white; background-color: none")
        self.letreroCelular.move(30, 410)
        self.letreroCelular.setFixedWidth(200)

        self.editCelular = QLineEdit(self)
        self.editCelular.setFixedWidth(200)
        self.editCelular.move(30, 440)
        self.editCelular.setStyleSheet("background-color: white")

        self.botonEnviar = QPushButton(self)
        self.botonEnviar.setText("Enviar")
        self.botonEnviar.setFont(self.letra2)
        self.botonEnviar.setFixedWidth(100)
        self.botonEnviar.move(510, 510)
        self.botonEnviar.setStyleSheet("color : #FFFFFF"
                                       "background-color : black;"
                                       "border-radius :20px;")

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

        self.botonEnviar.clicked.connect(self.accion_botonEnviar)

    def accion_botonVolver(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.ventanaAnterior.show()

    def accion_botonEnviar(self):
        # Obtener la calificación seleccionada del QComboBox
        mensaje = f'SE HA ACTUALIZADO CORRECTAMENTE SU PERFIL'

        # Crear una ventana emergente (QMessageBox) para mostrar el mensaje de calificación
        ventana_emergente = QMessageBox(self)
        ventana_emergente.setWindowTitle('ACTUALIZACION EXITOSA')
        ventana_emergente.setText(mensaje)
        ventana_emergente.setIcon(QMessageBox.Information)

        ventana_emergente.buttonClicked.connect(self.mostrar_ventanaAnterior)

        ventana_emergente.exec_()

    def mostrar_ventanaAnterior(self):
        # Ocultar la ventana actual
        self.hide()

        # Crear una instancia de la ventana6 y mostrarla
        self.ventanaAnterior.show()
