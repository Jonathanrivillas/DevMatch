import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class VentanaEntrenador extends JFrame {
    private JFrame ventanaAnterior; // Referencia a la ventana anterior

    public VentanaEntrenador(JFrame ventanaAnterior) {
        this.ventanaAnterior = ventanaAnterior;
        setTitle("Ventana del Entrenador");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);

        BackgroundPanel backgroundPanel = new BackgroundPanel("C:/Users/Jonat/Downloads/estadio-futbol-noche-generativo-ai.jpg");
        setContentPane(backgroundPanel);

        // Configurar el layout de la ventana principal
        setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 1; // Cada botón ocupará una columna
        gbc.anchor = GridBagConstraints.CENTER; // Los componentes se centrarán horizontalmente
        gbc.insets = new Insets(10, 10, 10, 10); // Espacio entre los componentes

        // Agregar los botones uno por uno
        addButton("C:/Users/Jonat/Downloads/1137 (1).jpg", "Crear partido único", gbc);
        addButton("C:/Users/Jonat/Downloads/7800778 (1).jpg", "Crear torneo", gbc);

        gbc.gridy++; // Saltar a la siguiente fila
        addButton("C:/Users/Jonat/Downloads/7619895 (1).jpg", "Ver posiciones", gbc);
        addButton("C:/Users/Jonat/Downloads/still-life-colombian-national-soccer-team (1).jpg", "Ver resultados", gbc);

        // Botón Volver
        gbc.gridx = 0;
        gbc.gridy++;
        gbc.gridwidth = 2; // Ocupa dos columnas
        gbc.anchor = GridBagConstraints.CENTER; // Centrar el botón
        JButton volverButton = new JButton("Volver");
        volverButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                volver();
            }
        });
        add(volverButton, gbc);
    }

    private void addButton(String imagePath, String labelText, GridBagConstraints gbc) {
        // Crear el botón
        ImageIcon icon = new ImageIcon(imagePath);
        JButton button = new JButton(icon);
        button.setContentAreaFilled(false);
        button.setBorderPainted(false);
        button.setFocusPainted(false);
        button.setOpaque(false);

        // Agregar el efecto de opresión al colocar el mouse sobre el botón
        button.getModel().addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                ButtonModel model = (ButtonModel) e.getSource();
                if (model.isRollover()) {
                    button.setBorderPainted(true);
                } else {
                    button.setBorderPainted(false);
                }
            }
        });

        // Agregar ActionListener al botón
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Acción al hacer clic en el botón
                JOptionPane.showMessageDialog(VentanaEntrenador.this, "¡Haz clic en " + labelText + "!");
            }
        });

        // Agregar el botón al contenedor principal
        add(button, gbc);

        // Configurar GridBagConstraints para el JLabel
        gbc.gridx++;
        gbc.anchor = GridBagConstraints.CENTER;

        // Crear el JLabel
        JLabel label = new JLabel(labelText);
        label.setForeground(Color.WHITE); // Color del texto del JLabel

        // Agregar el JLabel al contenedor principal
        add(label, gbc);
    }

    private void volver() {
        ventanaAnterior.setVisible(true); // Hacer visible la ventana anterior
        dispose(); // Cerrar esta ventana
    }

    class BackgroundPanel extends JPanel {
        private Image backgroundImage;

        public BackgroundPanel(String imagePath) {
            try {
                backgroundImage = new ImageIcon(imagePath).getImage();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            if (backgroundImage != null) {
                g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
            }
        }

        @Override
        public Component add(Component comp) {
            return super.add(comp);
        }
    }

    public static void main(String[] args) {
        JFrame ventanaAnterior = new SeleccionDeUsuarios(); // Crear la ventana anterior como SeleccionDeUsuarios
        ventanaAnterior.setVisible(true); // Hacer la ventana anterior visible
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                VentanaEntrenador ventanaEntrenador = new VentanaEntrenador(ventanaAnterior);
                ventanaEntrenador.setVisible(true);
            }
        });
    }
}
