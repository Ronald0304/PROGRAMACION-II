import javax.swing.*;
import java.awt.*;

class Punto {
    double x, y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Punto(x=" + x + ", y=" + y + ")";
    }
}

class Circulo {
    Punto centro;
    double radio;

    public Circulo(Punto centro, double radio) {
        this.centro = centro;
        this.radio = radio;
    }

    @Override
    public String toString() {
        return "Circulo(centro=" + centro + ", radio=" + radio + ")";
    }

    public void dibujaCirculo() {
        JFrame frame = new JFrame("Plano Cartesiano con Círculo");
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2d = (Graphics2D) g;
                g2d.setColor(Color.BLACK);

                // Tamaño del panel
                int width = getWidth();
                int height = getHeight();

                // Centro del plano cartesiano
                int centerX = width / 2;
                int centerY = height / 2;

                // Dibujar ejes X e Y
                g2d.drawLine(0, centerY, width, centerY); // Eje X
                g2d.drawLine(centerX, 0, centerX, height); // Eje Y

                // Dibujar círculo
                g2d.setColor(Color.RED);
                int r = (int) (radio * 50);
                int x = centerX + (int) (centro.x * 50) - r;
                int y = centerY - (int) (centro.y * 50) - r; // Invertimos Y
                g2d.drawOval(x, y, r * 2, r * 2);
            }
        });
        frame.setVisible(true);
    }
}

public class MainCirculo {
    public static void main(String[] args) {
        Circulo circulo = new Circulo(new Punto(0, 0), 2);
        System.out.println(circulo);
        circulo.dibujaCirculo();
    }
}
