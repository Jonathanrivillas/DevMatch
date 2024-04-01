import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;

public class SeleccionDeUsuarios extends JFrame {
    public SeleccionDeUsuarios() {
        setTitle("Selección de Usuarios");
        setExtendedState(JFrame.MAXIMIZED_BOTH); // Establece la ventana para que se maximice en la pantalla
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null); // Centrar la ventana en la pantalla
        
        // Crear un panel de fondo con la imagen deseada
        BackgroundPanel backgroundPanel = new BackgroundPanel("C:/Users/Jonat/Downloads/estadio-futbol-noche-generativo-ai.jpg");
        backgroundPanel.setLayout(new GridBagLayout()); // Usamos GridBagLayout para centrar los botones
        add(backgroundPanel);

        // Crear botones personalizados circulares
        CircularButton futbolista = new CircularButton("C:/Users/Jonat/Downloads/BotonFutbolista.png");
        CircularButton entrenador = new CircularButton("C:/Users/Jonat/Downloads/BotonEntrenador.png");

        // Establecer un tamaño fijo para los botones
        int buttonSize = 200;
        futbolista.setPreferredSize(new Dimension(buttonSize, buttonSize));
        entrenador.setPreferredSize(new Dimension(buttonSize, buttonSize));

        // Agregar ActionListener a los botones
        futbolista.addActionListener(e -> {
            // Agregar la lógica que deseas ejecutar cuando se haga clic en el botón futbolista
            System.out.println("futbolista clickeado");
            
        });

        entrenador.addActionListener(e -> {
            // Agregar la lógica que deseas ejecutar cuando se haga clic en el botón entrenador
            System.out.println("entrenador clickeado");
            VentanaEntrenador ventanaEntrenador = new VentanaEntrenador(SeleccionDeUsuarios.this);
            ventanaEntrenador.setVisible(true);
        });

        // Crear JLabels debajo de los botones
        JLabel label1 = new JLabel("Futbolista");
        JLabel label2 = new JLabel("Entrenador(Organizador)");

        // Configurar el tamaño de la fuente y el color del texto de los JLabel
        Font font = new Font("Arial", Font.BOLD, 16); // Fuente en negrita de tamaño 16
        Color color = Color.BLACK; // Color blanco para el texto

        label1.setFont(font);
        label1.setForeground(color);

        label2.setFont(font);
        label2.setForeground(color);

        // Configurar GridBagConstraints para centrar los botones vertical y horizontalmente
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 20, 5, 20); // Espacio alrededor de los botones (aumentado el espacio horizontal)
        backgroundPanel.add(futbolista, gbc);
        gbc.gridy++;
        backgroundPanel.add(label1, gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        backgroundPanel.add(entrenador, gbc);
        gbc.gridy++;
        backgroundPanel.add(label2, gbc);
    }

    class BackgroundPanel extends JPanel {
        private BufferedImage backgroundImage;

        public BackgroundPanel(String imagePath) {
            try {
                backgroundImage = ImageIO.read(new File(imagePath));
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            if (backgroundImage != null) {
                g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
            }
        }
    }

    class CircularButton extends JButton {
        private BufferedImage image;

        public CircularButton(String imagePath) {
            try {
                image = ImageIO.read(new File(imagePath));
                setOpaque(false); // Hace que el fondo del botón sea transparente
                setContentAreaFilled(false); // No rellena el área del botón con color
                setBorderPainted(false); // No muestra el borde del botón
                setFocusPainted(false); // No muestra el foco del botón

                addMouseListener(new MouseAdapter() {
                    @Override
                    public void mouseEntered(MouseEvent e) {
                        setBorderPainted(true); // Mostrar el borde del botón cuando el mouse está sobre él
                    }

                    @Override
                    public void mouseExited(MouseEvent e) {
                        setBorderPainted(false); // Ocultar el borde del botón cuando el mouse sale de él
                    }
                });
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            if (image != null) {
                // Dibuja la imagen centrada en el botón
                int x = (getWidth() - image.getWidth()) / 2;
                int y = (getHeight() - image.getHeight()) / 2;
                g.drawImage(image, x, y, this);
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new SeleccionDeUsuarios().setVisible(true);
            }
        });
    }
}

