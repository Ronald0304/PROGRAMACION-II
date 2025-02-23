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
        JFrame frame = new JFrame("Dibujar Línea");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.BLUE);
                g.drawLine((int) p1.x * 50, (int) p1.y * 50, (int) p2.x * 50, (int) p2.y * 50);
            }
        });
        frame.setVisible(true);
    }
}

public class MainLinea {
    public static void main(String[] args) {
        Punto p1 = new Punto(1, 2);
        Punto p2 = new Punto(4, 6);
        Linea linea = new Linea(p1, p2);

        System.out.println(linea);
        linea.dibujaLinea();
    }
}
