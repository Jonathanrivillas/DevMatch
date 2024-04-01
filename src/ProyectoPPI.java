import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

public class ProyectoPPI {

    public static void main(String[] args) {
        // Crear una nueva instancia de JFrame
        JFrame ventana = new JFrame("DevMatch");

        // Obtener el tamaño de la pantalla
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

        // Establecer el tamaño de la ventana como el tamaño de la pantalla
        ventana.setSize(screenSize);

        // Hacer que la ventana se cierre correctamente al hacer clic en el botón de cierre
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Cargar la imagen para el icono de la ventana
        ImageIcon iconoVentana = new ImageIcon("C:/Users/Jonat/Downloads/8970746.png");

        // Establecer la imagen como icono de la ventana
        ventana.setIconImage(iconoVentana.getImage());

        // Crear un JPanel para contener todos los componentes
        JPanel panelPrincipal = new JPanel() {
            // Override el método paintComponent para dibujar el fondo de la ventana
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                // Cargar una imagen para usarla como fondo
                ImageIcon imagenFondo = new ImageIcon("C:/Users/Jonat/Downloads/estadio-futbol-noche-generativo-ai.jpg");

                // Dibujar la imagen de fondo
                g.drawImage(imagenFondo.getImage(), 0, 0, getWidth(), getHeight(), null);
            }
        };
        // Establecer el layout en el panel principal
        panelPrincipal.setLayout(new GridBagLayout());

        // Crear un JLabel para mostrar texto en la ventana
        JLabel etiqueta = new JLabel("¡Bienvenido DevMatcher!");
        etiqueta.setForeground(Color.BLACK); // Cambiar el color del texto a blanco

        // Crear los JLabel para los campos de texto
        JLabel labelUsuario = new JLabel("Usuario:");
        labelUsuario.setForeground(Color.BLACK); // Cambiar el color del texto
        JLabel labelContraseña = new JLabel("Contraseña:");
        labelContraseña.setForeground(Color.BLACK); // Cambiar el color del texto

        // Crear los JTextField para ingresar usuario y contraseña
        JTextField campoUsuario = new JTextField(20);
        JPasswordField campoContraseña = new JPasswordField(20); // Cambia JTextField a JPasswordField

        // Crear un JCheckBox para mostrar/ocultar la contraseña
        JCheckBox mostrarContraseña = new JCheckBox("Mostrar contraseña");
        mostrarContraseña.setForeground(Color.BLACK); // Cambiar el color del texto a blanco
        mostrarContraseña.setFont(new Font("Arial", Font.PLAIN, 10)); // Establecer una fuente más pequeña

        // Ajustar el tamaño del JCheckBox para que se muestre todo el texto
        mostrarContraseña.setPreferredSize(new Dimension(120, mostrarContraseña.getPreferredSize().height));

        mostrarContraseña.addItemListener(new ItemListener() {
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    campoContraseña.setEchoChar((char) 0); // Mostrar contraseña
                } else {
                    campoContraseña.setEchoChar('*'); // Ocultar contraseña
                }
            }
        });

        // Crear el botón de inicio de sesión
        JButton botonIniciarSesion = new JButton("Iniciar sesión");
        botonIniciarSesion.addActionListener((ActionEvent e) -> {
            // Lógica para iniciar sesión
            String usuario = campoUsuario.getText();
            String contraseña = new String(campoContraseña.getPassword());
            // Aquí puedes agregar la lógica para verificar las credenciales de inicio de sesión
            
            // Redirigir a otra ventana
            ventana.dispose(); // Cierra la ventana actual
            SeleccionDeUsuarios seleccionDeUsuarios = new SeleccionDeUsuarios(); // Instancia la nueva ventana
            seleccionDeUsuarios.setVisible(true); // Hace visible la nueva ventana
        });

        // Configurar las restricciones para el JLabel y JTextField de Usuario
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 1;
        gbc.anchor = GridBagConstraints.EAST; // Alinear a la derecha
        gbc.insets = new Insets(5, 5, 5, 5); // Agregar espacio alrededor del componente
        panelPrincipal.add(labelUsuario, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST; // Alinear a la izquierda
        panelPrincipal.add(campoUsuario, gbc);

        // Configurar las restricciones para el JLabel y JPasswordField de Contraseña
        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.anchor = GridBagConstraints.EAST; // Alinear a la derecha
        panelPrincipal.add(labelContraseña, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST; // Alinear a la izquierda
        panelPrincipal.add(campoContraseña, gbc);

        // Configurar las restricciones para el JCheckBox de mostrar/ocultar contraseña
        gbc.gridx = 4;
        gbc.gridy = 4;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER; // Alinear a la izquierda
        panelPrincipal.add(mostrarContraseña, gbc);

        // Configurar las restricciones para el botón de inicio de sesión
        gbc.gridx = 0;
        gbc.gridy = 7; // Alinear con la siguiente fila
        gbc.gridwidth = 2; // Ocupa 2 columnas
        gbc.anchor = GridBagConstraints.CENTER; // Centrar horizontalmente
        panelPrincipal.add(botonIniciarSesion, gbc);

        // Agregar el JLabel con el mensaje de bienvenida
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2; // Ocupa 2 columnas
        gbc.anchor = GridBagConstraints.CENTER; // Centrar horizontalmente
        gbc.insets = new Insets(0, 0, 0, 0); // Agregar espacio alrededor del componente
        panelPrincipal.add(etiqueta, gbc);

         // Crear el botón de registro
        JButton botonRegistrarse = new JButton("Registrarse");
        botonRegistrarse.addActionListener((ActionEvent e) -> {
            // Abrir la ventana de registro
            Registro registroVentana = new Registro();
            registroVentana.setVisible(true);
        });

        // Configurar restricciones para el botón de registro
        gbc.gridx = 0;
        gbc.gridy = 8;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        panelPrincipal.add(botonRegistrarse, gbc);


        // Agregar el panel principal a la ventana
        ventana.add(panelPrincipal);

        // Hacer visible la ventana
        ventana.setVisible(true);
    }
}
    