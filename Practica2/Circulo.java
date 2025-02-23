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
        JFrame frame = new JFrame("Dibujar Círculo");
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.setColor(Color.RED);
                int r = (int) (radio * 50);
                g.drawOval((int) (centro.x * 50 - r), (int) (centro.y * 50 - r), r * 2, r * 2);
            }
        });
        frame.setVisible(true);
    }
}

public class MainCirculo {
    public static void main(String[] args) {
        Circulo circulo = new Circulo(new Punto(3, 3), 2);

        System.out.println(circulo);
        circulo.dibujaCirculo();
    }
}
