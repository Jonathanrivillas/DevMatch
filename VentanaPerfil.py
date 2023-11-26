import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget, QToolBar, QAction, QFileDialog
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from ventanaEditarPerfil import ventana9

class ventana4(QMainWindow):
    def __init__(self, anterior, usuario):
        super(ventana4, self).__init__()

        self.ventanaAnterior = anterior
        self.usuario = usuario  # Información sobre el usuario que ha iniciado sesión
        # Poner el título
        self.ruta_imagen = usuario.get('Ruta de la Imagen', '')
              

        self.setWindowTitle("Perfil carpy")
        self.setWindowIcon(QIcon('Logo/carpy.png'))
        

        
        


        self.imagen = QLabel(self)
        self.imagenPantalla = QPixmap("Logo/fondo humilde.jpeg")
        self.imagen.setPixmap(self.imagenPantalla)
        self.imagen.setScaledContents(True)
        self.resize(self.imagen.width(), self.imagen.height())
        self.setCentralWidget(self.imagen)

        self.ancho = 700
        self.alto = 600
        self.resize(self.ancho, self.alto)
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

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

        self.barraHerramientas = QToolBar("Barra de Herramientas")
        self.barraHerramientas.setIconSize(QSize(40, 40))
        self.addToolBar(self.barraHerramientas)
        self.barraHerramientas.setStyleSheet('background-image: url(Logo/fondo humilde.jpeg);')

        self.perfil = QAction(QIcon("Logo/LOGOSALIDA.jpg"), "Cerrar sesión", self)
        self.barraHerramientas.addAction(self.perfil)

        self.editarPerfil = QAction(QIcon("Logo/CARPINTERO.jpg"), "Editar perfil", self)
        self.barraHerramientas.addAction(self.editarPerfil)
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraHerramientas)

        self.imagenPerfil = QLabel(self)
        self.foto = QPixmap("Logo/FOTO EDWARD.jpg")
        self.imagenPerfil.setPixmap(self.foto)
        self.imagenPerfil.setFixedWidth(230)
        self.imagenPerfil.setFixedHeight(230)
        self.imagenPerfil.setStyleSheet("background-color: none;")
        self.imagenPerfil.move(30, 80)


        self.botonSubirImagen = QPushButton("Publicar", self)
        self.botonSubirImagen.setFont(self.letra2)
        self.botonSubirImagen.move(40, 490)
        self.botonSubirImagen.clicked.connect(self.abrirDialogoImagen)

        
        

        
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
        self.letreroCelular.setStyleSheet("color: white; background-color: none;")
        self.letreroCelular.move(190, 230)
        self.letreroCelular.setFixedWidth(500)

        self.letreroInstagram = QLabel(self)
        self.letreroInstagram.setText(usuario['Instagram'])
        self.letreroInstagram.setFont(self.letra3)
        self.letreroInstagram.setStyleSheet("color: white; background-color: none;")
        self.letreroInstagram.move(60, 330)
        self.letreroInstagram.setFixedWidth(500)

        self.logoFondo1 = QLabel(self)
        self.logo1 = QPixmap("Logo/INSTAGRAM LOGO.png")
        # Establecemos el modo para escalar la imagen
        self.logoFondo1.setPixmap(self.logo1)
        self.logoFondo1.setFixedWidth(50)
        self.logoFondo1.setFixedHeight(50)
        self.logoFondo1.setStyleSheet("background-color: none;")
        self.logoFondo1.move(25, 320)

        self.logoFondo2 = QLabel(self)
        self.logo2 = QPixmap("Logo/LOGO FACEBOOK.png")
        # Establecemos el modo para escalar la imagen
        self.logoFondo2.setPixmap(self.logo2)
        self.logoFondo2.setFixedWidth(80)
        self.logoFondo2.setFixedHeight(80)
        self.logoFondo2.setStyleSheet("background-color: none;")
        self.logoFondo2.move(0, 350)

        self.logoFondo3 = QLabel(self)
        self.logo3 = QPixmap("Logo/LOGO WPP.png")
        # Establecemos el modo para escalar la imagen
        self.logoFondo3.setPixmap(self.logo3)
        self.logoFondo3.setFixedWidth(40)
        self.logoFondo3.setFixedHeight(40)
        self.logoFondo3.setStyleSheet("background-color: none;")
        self.logoFondo3.move(25, 410)

        self.letreroFacebook = QLabel(self)
        self.letreroFacebook.setText(usuario['Facebook'])
        self.letreroFacebook.setFont(self.letra3)
        self.letreroFacebook.setStyleSheet("color: white; background-color: none;")
        self.letreroFacebook.move(60, 370)
        self.letreroFacebook.setFixedWidth(500)

        self.letreroWpp = QLabel(self)
        self.letreroWpp.setText(str(usuario['Whatsapp']))
        self.letreroWpp.setFont(self.letra3)
        self.letreroWpp.setStyleSheet("color: white; background-color: none;")
        self.letreroWpp.move(65, 415)
        self.letreroWpp.setFixedWidth(500)

        self.letreroCalificacion = QLabel(self)
        self.letreroCalificacion.setText("Calificacion: ⭐⭐⭐⭐⭐")
        self.letreroCalificacion.setFont(self.letra3)
        self.letreroCalificacion.setStyleSheet("color: white; background-color: none;")
        self.letreroCalificacion.move(30, 290)
        self.letreroCalificacion.setFixedWidth(500)

        self.mostrar_imagen_perfil()

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

    def mostrar_imagen_perfil(self):
        if self.ruta_imagen:
            print(f'Ruta de la imagen: {self.ruta_imagen}')  # Mensaje de depuración
            try:
                pixmap = QPixmap()
                pixmap.load(self.ruta_imagen)
                # Actualizar la imagen en la posición de "FOTO EDWARD"
                self.imagenPerfil.setPixmap(pixmap.scaled(230, 230))
                self.imagenPerfil.setScaledContents(True)
                self.update()  # Actualizar la interfaz gráfica
            except Exception as e:
                print(f'Error al cargar la imagen: {e}')
        else:
            print('La ruta de la imagen está vacía.')  # Mensaje de depuración
            # Si no hay una imagen seleccionada, podrías mostrar una imagen predeterminada o dejar el QLabel vacío
            self.imagenPerfil.clear()
            
    def abrirDialogoImagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Selecciona una imagen", "",
                                                "Archivos de Imagen (.png *.jpg *.bmp * .jpeg);;Todos los archivos ()",
                                                options=opciones)
        if archivo:
            # Actualizar la ruta de la imagen en los datos del usuario
            self.ruta_imagen = archivo
            # Obtener el nombre de usuario del diccionario de usuario
            nombre_usuario = self.usuario.get('Nombre', '')
            if nombre_usuario:
                # Guardar la ruta en un archivo
                self.guardar_ruta_imagen_en_archivo(nombre_usuario, archivo)
                # Mostrar la nueva imagen
                self.mostrar_imagen_perfil()
            
    def guardar_ruta_imagen_en_archivo(self, nombre_usuario, ruta_imagen):
        nombre_archivo = f"registro_{nombre_usuario}.txt"
        try:
            with open(nombre_archivo, 'a') as archivo:
                archivo.write(f'Ruta de la Imagen: {ruta_imagen}\n')
                print(f'Ruta de la imagen guardada en {nombre_archivo}')
        except Exception as e:
            print(f"Error al guardar la ruta de la imagen: {e}")
            
