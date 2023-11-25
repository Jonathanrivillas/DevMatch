import sys
from PyQt5.QtGui import QFont, QPixmap, QTextOption
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget, \
    QToolBar, QAction, QFileDialog, QComboBox, QMessageBox, QSizePolicy
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from VentanaComentarios import ventana11
from VentanaComentarios2 import ventana12


class ventana10(QMainWindow):
    def __init__(self, anterior):
        super(ventana10,  self).__init__()

        self.ventanaAnterior = anterior
        # Poner el titulo
        self.setWindowTitle("Perfil carpy")
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
        self.letra1.setPointSize(24)

        self.letra2 = QFont()
        self.letra2.setFamily("Gabriola")
        self.letra2.setPointSize(14)

        self.letra3 = QFont()
        self.letra3.setFamily("Arial")
        self.letra3.setPointSize(14)

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

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/FOTO KARINA2.jpg")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(300)
        self.logoFondo.setFixedHeight(200)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(20, 60)

        self.letreroNombre = QLabel(self)
        self.letreroNombre.setText("Santiago Arango Galeano")
        self.letreroNombre.setFont(self.letra1)
        self.letreroNombre.setStyleSheet("color: white;")
        self.letreroNombre.move(170, 100)
        self.letreroNombre.setFixedWidth(600)

        self.letreroCedula = QLabel(self)
        self.letreroCedula.setText("CC: 1003002719")
        self.letreroCedula.setFont(self.letra3)
        self.letreroCedula.setStyleSheet("color: white;")
        self.letreroCedula.move(170, 160)
        self.letreroCedula.setFixedWidth(600)

        self.letreroCorreo = QLabel(self)
        self.letreroCorreo.setText("Correo: santiagoarangogaleano.1204@gmail.com")
        self.letreroCorreo.setFont(self.letra3)
        self.letreroCorreo.setStyleSheet("color: white;")
        self.letreroCorreo.move(170, 190)
        self.letreroCorreo.setFixedWidth(600)

        self.letreroCelular = QLabel(self)
        self.letreroCelular.setText("Celular: 3014424125")
        self.letreroCelular.setFont(self.letra3)
        self.letreroCelular.setStyleSheet("color: white; background-color: none")
        self.letreroCelular.move(170, 220)
        self.letreroCelular.setFixedWidth(500)

        self.letreroInstagram = QLabel(self)
        self.letreroInstagram.setText("S_arango1204")
        self.letreroInstagram.setFont(self.letra3)
        self.letreroInstagram.setStyleSheet("color: white; background-color: none")
        self.letreroInstagram.move(60, 330)
        self.letreroInstagram.setFixedWidth(500)

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/INSTAGRAM LOGO.png")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(50)
        self.logoFondo.setFixedHeight(50)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(25, 320)

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/LOGO FACEBOOK.png")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(80)
        self.logoFondo.setFixedHeight(80)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(0, 350)

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/LOGO WPP.png")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(40)
        self.logoFondo.setFixedHeight(40)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(25, 410)

        self.letreroInstagram = QLabel(self)
        self.letreroInstagram.setText("Santiago Arango")
        self.letreroInstagram.setFont(self.letra3)
        self.letreroInstagram.setStyleSheet("color: white; background-color: none")
        self.letreroInstagram.move(60, 370)
        self.letreroInstagram.setFixedWidth(500)

        self.letreroWpp = QLabel(self)
        self.letreroWpp.setText("3014424101")
        self.letreroWpp.setFont(self.letra3)
        self.letreroWpp.setStyleSheet("color: white; background-color: none")
        self.letreroWpp.move(65, 415)
        self.letreroWpp.setFixedWidth(500)

        self.letreroCalificacion = QLabel(self)
        self.letreroCalificacion.setText("Calificacion: ⭐⭐⭐")
        self.letreroCalificacion.setFont(self.letra3)
        self.letreroCalificacion.setStyleSheet("color: white; background-color: none")
        self.letreroCalificacion.move(30, 290)
        self.letreroCalificacion.setFixedWidth(500)

        self.letreroCalificacion = QLabel(self)
        self.letreroCalificacion.setText("Calificar")
        self.letreroCalificacion.setFont(self.letra3)
        self.letreroCalificacion.setStyleSheet("color: white; background-color: none")
        self.letreroCalificacion.move(30, 470)
        self.letreroCalificacion.setFixedWidth(500)

        self.letreroReseña = QLabel(self)
        self.letreroReseña.setText("Reseñar:")
        self.letreroReseña.setFont(self.letra3)
        self.letreroReseña.setStyleSheet("color: white; background-color: none")
        self.letreroReseña.move(300, 290)
        self.letreroReseña.setFixedWidth(500)

        self.editResena = QLineEdit(self)
        self.editResena.setFixedWidth(250)
        self.editResena.setFixedHeight(150)
        self.editResena.move(300, 320)
        self.editResena.setStyleSheet("background-color: white")
        self.editResena.setFont(self.letra2)

        # Establecer el alineamiento del texto en la esquina superior izquierda
        self.editResena.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # Permitir que el texto se ajuste al tamaño del cuadro de edición

        # Configurar el cuadro de edición para que el texto se ajuste automáticamente al tamaño
        self.editResena.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("⭐⭐⭐⭐⭐")
        self.comboBox.addItem("⭐⭐⭐⭐")
        self.comboBox.addItem("⭐⭐⭐")
        self.comboBox.addItem("⭐⭐")
        self.comboBox.addItem("⭐")
        self.comboBox.setFont(self.letra3)
        self.comboBox.move(30, 500)  # Ajusta la posición según sea necesario
        self.comboBox.setFixedWidth(200)  # Establece el ancho según sea necesario
        self.comboBox.setStyleSheet("background-color: white;")

        self.botonCalificar = QPushButton(self)
        self.botonCalificar.setText("Enviar Calificación")
        self.botonCalificar.setFont(self.letra2)
        self.botonCalificar.setFixedWidth(170)
        self.botonCalificar.move(30, 550)
        self.botonCalificar.setStyleSheet("color : #FFFFFF"
                                          "background-color : black;"
                                          "border-radius :20px;")
        self.botonResenar = QPushButton(self)
        self.botonResenar.setText("Enviar Reseña")
        self.botonResenar.setFont(self.letra2)
        self.botonResenar.setFixedWidth(170)
        self.botonResenar.move(300, 500)
        self.botonResenar.setStyleSheet("color : #FFFFFF"
                                        "background-color : black;"
                                        "border-radius :20px;")


        self.botonComentarios = QPushButton(self)
        self.botonComentarios.setText("Ver reseñas")
        self.botonComentarios.setFont(self.letra2)
        self.botonComentarios.setFixedWidth(170)
        self.botonComentarios.move(300, 550)
        self.botonComentarios.setStyleSheet("color : #FFFFFF"
                                          "background-color : black;"
                                          "border-radius :20px;")

        # Convierte el texto a formato UTF-8 antes de conectar la señal
        self.botonResenar.setText("Enviar Reseñar")

        self.botonResenar.clicked.connect(self.accion_botonResenar)

        self.botonComentarios.clicked.connect(self.accion_botonComentarios)
        self.botonCalificar.clicked.connect(self.accion_botonCalificar)

    def accion_botonResenar(self):
        # Obtener la calificación seleccionada del QComboBox
        resena = self.editResena.text()
        mensaje = f'Se ha enviado correctamente su reseña: {resena}.'

        # Crear una ventana emergente (QMessageBox) para mostrar el mensaje de calificación
        ventana_emergente2 = QMessageBox(self)
        ventana_emergente2.setWindowTitle('Calificación')
        ventana_emergente2.setText(mensaje)
        ventana_emergente2.exec_()

    def accion_botonCalificar(self):
        # Obtener la calificación seleccionada del QComboBox
        calificacion = self.comboBox.currentText()
        mensaje = f'Se ha calificado el servicio con {calificacion} estrellas.'

        # Crear una ventana emergente (QMessageBox) para mostrar el mensaje de calificación
        ventana_emergente = QMessageBox(self)
        ventana_emergente.setWindowTitle('Calificación')
        ventana_emergente.setText(mensaje)
        ventana_emergente.setIcon(QMessageBox.Information)
        ventana_emergente.exec_()


    def accion_barraHerramientas(self, opcion):
        # Ocultamos la ventana actual
        self.hide()
        # Validamos la opcion que se pulso
        if opcion.text() == "Cerrar sesión":
            self.ventanaAnterior.show()

    def accion_botonComentarios(self):
                # Ocultamos la ventana actual
                self.hide()
                # Creamos una ventana nueva
                self.ventanaComentarios2 = ventana12(self)
                self.ventanaComentarios2.show()
