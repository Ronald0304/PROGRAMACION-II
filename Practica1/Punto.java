import java.text.DecimalFormat;

public class Punto {
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double[] coord_cartesianas() {
        return new double[]{x, y};
    }

    public double[] coord_polares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.toDegrees(Math.atan2(y, x)); // Convertimos el ángulo a grados
        return new double[]{r, theta};
    }

    @Override
    public String toString() {
        DecimalFormat df = new DecimalFormat("#.##");
        return "Punto(x=" + df.format(x) + ", y=" + df.format(y) + ")";
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println(p); // Salida: Punto(x=3.0, y=4.0)
        
        double[] cartesianas = p.coord_cartesianas();
        System.out.println("Coordenadas Cartesianas: (" + cartesianas[0] + ", " + cartesianas[1] + ")");
        
        double[] polares = p.coord_polares();
        System.out.println("Coordenadas Polares: (r=" + polares[0] + ", θ=" + polares[1] + "°)");
    }
}
