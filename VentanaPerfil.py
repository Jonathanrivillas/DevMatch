import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget, QToolBar,QAction, QFileDialog
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from ventanaEditarPerfil import ventana9
class ventana4(QMainWindow):
    def __init__(self, anterior, usuario):
        super(ventana4, self).__init__()

        self.ventanaAnterior = anterior
        self.usuario = usuario  # Información sobre el usuario que ha iniciado sesión
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

        self.editarPerfil = QAction(QIcon("Logo/CARPINTERO.jpg"), "Editar perfil", self)
        #Lo de Editar usuario
        self.barraHerramientas.addAction(self.editarPerfil)

        # Activamos las opciones para la barra de herramientas
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.logoFondo = QLabel(self)
        self.logo = QPixmap("Logo/FOTO EDWARD.jpg")
        # Establecemos el modo para escalar la imagen
        self.logoFondo.setPixmap(self.logo)
        self.logoFondo.setFixedWidth(230)
        self.logoFondo.setFixedHeight(230)
        self.logoFondo.setStyleSheet("background-color: none")
        self.logoFondo.move(30, 80)

        # Crear un botón para subir una imagen
        self.botonSubirImagen = QPushButton("Publicar", self)
        self.botonSubirImagen.setFont(self.letra2)
        self.botonSubirImagen.move(40, 490)  # Ajusta la posición según sea necesario
        self.botonSubirImagen.clicked.connect(self.abrirDialogoImagen)

        # Crear un QLabel para mostrar la imagen
        self.labelImagen = QLabel(self)
        # Ajusta la posición y el tamaño según sea necesario
        self.labelImagen.setGeometry(250, 180, 200, 200)
    # Definimos la accion de publicar (Subir archivo)
        print(f'Diccionario de usuario: {usuario}')  # Imprime el diccionario para depurar

        self.letreroNombre = QLabel(self)
        self.letreroNombre.setText(usuario['Nombre'])  # O proporciona un valor predeterminado
        self.letreroNombre.setFont(self.letra1)
        self.letreroNombre.setStyleSheet("color: white;")
        self.letreroNombre.move(190, 100)
        self.letreroNombre.setFixedWidth(600)

        self.letreroCedula = QLabel(self)
        self.letreroCedula.setText(f"CC: {usuario['Número de Documento']}")
        self.letreroCedula.setFont(self.letra3)
        self.letreroCedula.setStyleSheet("color: white;")
        self.letreroCedula.move(190, 150)
        self.letreroCedula.setFixedWidth(600)

        self.letreroCorreo = QLabel(self)
        self.letreroCorreo.setText(f"Correo: {usuario['Correo']}")
        self.letreroCorreo.setFont(self.letra3)
        self.letreroCorreo.setStyleSheet("color: white;")
        self.letreroCorreo.move(190, 190)
        self.letreroCorreo.setFixedWidth(600)

        self.letreroCelular = QLabel(self)
        self.letreroCelular.setText(f"Celular: {usuario['Celular']}")
        self.letreroCelular.setFont(self.letra3)
        self.letreroCelular.setStyleSheet("color: white; background-color: none")
        self.letreroCelular.move(190, 230)
        self.letreroCelular.setFixedWidth(500)

        self.letreroInstagram = QLabel(self)
        self.letreroInstagram.setText(usuario['Instagram'])
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

        self.letreroFacebook = QLabel(self)
        self.letreroFacebook.setText(usuario['Facebook'])
        self.letreroFacebook.setFont(self.letra3)
        self.letreroFacebook.setStyleSheet("color: white; background-color: none")
        self.letreroFacebook.move(60, 370)
        self.letreroFacebook.setFixedWidth(500)

        self.letreroWpp = QLabel(self)
        self.letreroWpp.setText(str(usuario['Whatsapp']))
        self.letreroWpp.setFont(self.letra3)
        self.letreroWpp.setStyleSheet("color: white; background-color: none")
        self.letreroWpp.move(65, 415)
        self.letreroWpp.setFixedWidth(500)

        self.letreroCalificacion = QLabel(self)
        self.letreroCalificacion.setText("Calificacion: ⭐⭐⭐⭐⭐")
        self.letreroCalificacion.setFont(self.letra3)
        self.letreroCalificacion.setStyleSheet("color: white; background-color: none")
        self.letreroCalificacion.move(30, 290)
        self.letreroCalificacion.setFixedWidth(500)


    def abrirDialogoImagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Selecciona una imagen", "",
                                                 "Archivos de Imagen (.png *.jpg *.bmp * .jpeg);;Todos los archivos ()",
                                                 options=opciones)
        if archivo:
            # Cargar la imagen y establecerla en el QLabel
            pixmap = QPixmap(archivo)
            self.labelImagen.setPixmap(pixmap.scaled(1000, 1000))
            self.labelImagen.setScaledContents(True)
            self.labelImagen.move(300, 280)
            self.labelImagen.setFixedWidth(350)
            self.labelImagen.setFixedHeight(300)


    def accion_barraHerramientas(self, opcion):
        # Ocultamos la ventana actual
        self.hide()
        # Validamos la opcion que se pulso
        if opcion.text() == "Cerrar sesión":
            self.ventanaAnterior.show()
        if opcion.text() == "Editar perfil":

            self.ventanaEditar = ventana9(self)
            self.ventanaEditar.show()
            
            
    def accion_botonComentarios(self):
                # Ocultamos la ventana actual
        self.hide()      # Creamos una ventana nueva
        self.ventanaComentarios = ventana11(self)
        self.ventanaComentarios.show()
