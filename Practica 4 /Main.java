// Clase abstracta Figura
abstract class Figura {
    abstract double area();
}

// Clase Círculo
class Circulo extends Figura {
    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }

    @Override
    double area() {
        return Math.PI * radio * radio;
    }
}

// Clase Rectángulo
class Rectangulo extends Figura {
    private double base, altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    double area() {
        return base * altura;
    }
}

// Clase Trapecio
class Trapecio extends Figura {
    private double baseMayor, baseMenor, altura;

    public Trapecio(double baseMayor, double baseMenor, double altura) {
        this.baseMayor = baseMayor;
        this.baseMenor = baseMenor;
        this.altura = altura;
    }

    @Override
    double area() {
        return ((baseMayor + baseMenor) * altura) / 2;
    }
}

// Clase Pentágono
class Pentagono extends Figura {
    private double lado, apotema;

    public Pentagono(double lado, double apotema) {
        this.lado = lado;
        this.apotema = apotema;
    }

    @Override
    double area() {
        return (5 * lado * apotema) / 2;
    }
}

// Clase principal para probar las figuras
public class Main {
    public static void main(String[] args) {
        Figura[] figuras = {
            new Circulo(5),
            new Rectangulo(10, 4),
            new Trapecio(8, 5, 3),
            new Pentagono(6, 4)
        };

        for (Figura figura : figuras) {
            System.out.println("Área de " + figura.getClass().getSimpleName() + ": " + figura.area());
        }
    }
}
