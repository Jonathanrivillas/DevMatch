import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Registro extends JFrame {
    public Registro() {
        // Configuración de la ventana de registro
        setTitle("Registro");
        setExtendedState(JFrame.MAXIMIZED_BOTH); // Establece la ventana para que se maximice en la pantalla
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null); // Centrar la ventana en la pantalla

        // Crear un panel para los componentes de registro
        JPanel panelRegistro = new JPanel();
        panelRegistro.setLayout(new GridBagLayout());

        // Crear componentes de registro
        JLabel labelNombre = new JLabel("Nombre:");
        JTextField campoNombre = new JTextField(20);
        JLabel labelEmail = new JLabel("Correo electrónico:");
        JTextField campoEmail = new JTextField(20);
        JLabel labelContraseña = new JLabel("Contraseña:");
        JPasswordField campoContraseña = new JPasswordField(20);
        JButton botonRegistrar = new JButton("Registrar");

        // Configurar restricciones para los componentes de registro
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.EAST;
        gbc.insets = new Insets(5, 5, 5, 5);
        panelRegistro.add(labelNombre, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panelRegistro.add(campoNombre, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.EAST;
        panelRegistro.add(labelEmail, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panelRegistro.add(campoEmail, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.EAST;
        panelRegistro.add(labelContraseña, gbc);

        gbc.gridx = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panelRegistro.add(campoContraseña, gbc);

        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        panelRegistro.add(botonRegistrar, gbc);

        // Acción del botón de registro
        botonRegistrar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Aquí iría la lógica para registrar al usuario
                // Por simplicidad, simplemente cerramos la ventana de registro
                dispose();
            }
        });

        // Agregar panel de registro a la ventana de registro
        add(panelRegistro);
    }
}