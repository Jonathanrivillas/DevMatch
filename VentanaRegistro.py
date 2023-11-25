import sys

from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QLineEdit, QApplication, QPushButton, QWidget, QComboBox, QVBoxLayout, QFileDialog, QMessageBox


class ventana5(QMainWindow):
    def __init__(self, anterior):
        super(ventana5, self).__init__()
        self.ventanaAnterior = anterior

        # Poner el titulo
        self.setWindowTitle("REGISTRARSE")
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
        self.letreroRegistrarse.setText("Registro")
        self.letreroRegistrarse.setFont(self.letra1)
        self.letreroRegistrarse.setStyleSheet("color: white;")
        self.letreroRegistrarse.move(285, 70)
        self.letreroRegistrarse.setFixedWidth(300)

        self.letreroNombre = QLabel(self)
        self.letreroNombre.setText("Nombre completo")
        self.letreroNombre.setFont(self.letra2)
        self.letreroNombre.setStyleSheet("color: white;")
        self.letreroNombre.move(70, 130)
        self.letreroNombre.setFixedWidth(200)

        self.editNombre = QLineEdit(self)
        self.editNombre.setFixedWidth(200)
        self.editNombre.move(70,160)
        self.editNombre.setFont(self.letra3)
        self.editNombre.setStyleSheet("background-color: white")

        self.letreroTipodeDocumento = QLabel(self)
        self.letreroTipodeDocumento.setText("Tipo de documento")
        self.letreroTipodeDocumento.setFont(self.letra2)
        self.letreroTipodeDocumento.setStyleSheet("color: white;")
        self.letreroTipodeDocumento.move(70, 220)
        self.letreroTipodeDocumento.setFixedWidth(200)

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Cédula")
        self.comboBox.addItem("Cédula de Extranjería")
        self.comboBox.addItem("Pasaporte")
        self.comboBox.setFont(self.letra3)
        self.comboBox.move(70, 250)  # Ajusta la posición según sea necesario
        self.comboBox.setFixedWidth(200)  # Establece el ancho según sea necesario
        self.comboBox.setStyleSheet("background-color: white;")

        self.letreroNumeroDeDocumento = QLabel(self)
        self.letreroNumeroDeDocumento.setText("Número de documento")
        self.letreroNumeroDeDocumento.setFont(self.letra2)
        self.letreroNumeroDeDocumento.setStyleSheet("color: white;")
        self.letreroNumeroDeDocumento.move(70, 300)
        self.letreroNumeroDeDocumento.setFixedWidth(150)

        self.editNumeroDeDocumento = QLineEdit(self)
        self.editNumeroDeDocumento.setFixedWidth(200)
        self.editNumeroDeDocumento.move(70,330)
        self.editNumeroDeDocumento.setFont(self.letra3)
        self.editNumeroDeDocumento.setStyleSheet("background-color: white")

        self.letreroCorreo = QLabel(self)
        self.letreroCorreo.setText("Correo")
        self.letreroCorreo.setFont(self.letra2)
        self.letreroCorreo.setStyleSheet("color: white; background-color: none")
        self.letreroCorreo.move(70, 370)
        self.letreroCorreo.setFixedWidth(200)

        self.editCorreo = QLineEdit(self)
        self.editCorreo.setFixedWidth(200)
        self.editCorreo.move(70,400)
        self.editCorreo.setStyleSheet("background-color: white")

        self.letreroCelular = QLabel(self)
        self.letreroCelular.setText("Celular")
        self.letreroCelular.setFont(self.letra2)
        self.letreroCelular.setStyleSheet("color: white; background-color: none")
        self.letreroCelular.move(70, 440)
        self.letreroCelular.setFixedWidth(200)

        self.editCelular= QLineEdit(self)
        self.editCelular.setFixedWidth(200)
        self.editCelular.move(70, 470)
        self.editCelular.setStyleSheet("background-color: white")

        self.letreroTipodeCliente = QLabel(self)
        self.letreroTipodeCliente.setText("Tipo de usuario")
        self.letreroTipodeCliente.setFont(self.letra2)
        self.letreroTipodeCliente.setStyleSheet("color: white; background-color: none")
        self.letreroTipodeCliente.move(400, 130)
        self.letreroTipodeCliente.setFixedWidth(200)

        self.comboBoxTipoCliente = QComboBox(self)
        self.comboBoxTipoCliente.addItem("Carpy")
        self.comboBoxTipoCliente.addItem("Cliente")
        self.comboBoxTipoCliente.setFont(self.letra3)
        self.comboBoxTipoCliente.move(400, 160)  # Ajusta la posición según sea necesario
        self.comboBoxTipoCliente.setFixedWidth(200)  # Establece el ancho según sea necesario
        self.comboBoxTipoCliente.setStyleSheet("background-color: white;")


        self.botonEnviar = QPushButton(self)
        self.botonEnviar.setText("Enviar")
        self.botonEnviar.setFont(self.letra2)
        self.botonEnviar.setFixedWidth(100)
        self.botonEnviar.move(510,510)
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

    def guardar_en_archivo(self, nombre, tipo_documento, numero_documento, correo, celular, tipo_cliente):
            # Define el nombre del archivo
            archivo = "registro.txt"

            # Abre el archivo en modo de escritura
            with open(archivo, "a") as f:
                # Escribe la información en el archivo
                f.write(f"Nombre: {nombre}\n")
                f.write(f"Tipo de Documento: {tipo_documento}\n")
                f.write(f"Número de Documento: {numero_documento}\n")
                f.write(f"Correo: {correo}\n")
                f.write(f"Celular: {celular}\n")
                f.write(f"Tipo de Cliente: {tipo_cliente}\n")
                f.write("\n")
    def accion_botonVolver(self):
        # Ocultamos la ventana actual
        self.hide()
        # Creamos una ventana nueva
        self.ventanaAnterior.show()

    def accion_botonEnviar(self):
        try:
            # Obtener la información ingresada por el usuario
            nombre = self.editNombre.text()
            tipo_documento = self.comboBox.currentText()
            numero_documento = self.editNumeroDeDocumento.text()
            correo = self.editCorreo.text()
            celular = self.editCelular.text()
            tipo_cliente = self.comboBoxTipoCliente.currentText()

            # Guardar la información en un archivo plano
            self.guardar_en_archivo(nombre, tipo_documento, numero_documento, correo, celular, tipo_cliente)

            # Mostrar mensaje de registro exitoso
            mensaje = f'SE HA ENVIADO CORRECTAMENTE SU REGISTRO.'
            ventana_emergente = QMessageBox(self)
            ventana_emergente.setWindowTitle('REGISTRO EXITOSO')
            ventana_emergente.setText(mensaje)
            ventana_emergente.setIcon(QMessageBox.Information)

            ventana_emergente.buttonClicked.connect(self.mostrar_ventanaAnterior)
            ventana_emergente.exec_()


        except Exception as e:
            print(f"Error: {str(e)}")

    def mostrar_ventanaAnterior(self):
    # Ocultar la ventana actual
        self.hide()

    # Crear una instancia de la ventana6 y mostrarla
        self.ventanaAnterior.show()
