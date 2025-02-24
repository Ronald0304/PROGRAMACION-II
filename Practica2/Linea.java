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

class Linea {
    Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    @Override
    public String toString() {
        return "Linea(" + p1 + ", " + p2 + ")";
    }

    public void dibujaLinea() {
        JFrame frame = new JFrame("Plano Cartesiano con Línea");
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

                // Dibujar línea
                g2d.setColor(Color.BLUE);
                int x1 = centerX + (int) (p1.x * 50);
                int y1 = centerY - (int) (p1.y * 50); // Invertimos Y
                int x2 = centerX + (int) (p2.x * 50);
                int y2 = centerY - (int) (p2.y * 50); // Invertimos Y
                g2d.drawLine(x1, y1, x2, y2);
            }
        });
        frame.setVisible(true);
    }
}

public class MainLinea {
    public static void main(String[] args) {
        Punto p1 = new Punto(0, 0);
        Punto p2 = new Punto(5, 5);
        Linea linea = new Linea(p1, p2);

        System.out.println(linea);
        linea.dibujaLinea();
    }
}

