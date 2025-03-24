import java.util.Scanner;

abstract class EcuacionCuadratica {
    double a, b, c, discriminante;

    EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.discriminante = b * b - 4 * a * c;
    }

    abstract String calcular();
}

class DosRaices extends EcuacionCuadratica {
    DosRaices(double a, double b, double c) {
        super(a, b, c);
    }

    @Override
    String calcular() {
        double r1 = (-b + Math.sqrt(discriminante)) / (2 * a);
        double r2 = (-b - Math.sqrt(discriminante)) / (2 * a);
        return String.format("La ecuación tiene dos raíces %.5f y %.5f", r1, r2);
    }
}

class UnaRaiz extends EcuacionCuadratica {
    UnaRaiz(double a, double b, double c) {
        super(a, b, c);
    }

    @Override
    String calcular() {
        double r = -b / (2 * a);
        return String.format("La ecuación tiene una raíz %.5f", r);
    }
}

class SinRaices extends EcuacionCuadratica {
    SinRaices(double a, double b, double c) {
        super(a, b, c);
    }

    @Override
    String calcular() {
        return "La ecuación no tiene raíces reales";
    }
}

public class EcuacionPOO {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Ingrese a, b, c (o escriba 'salir' para terminar): ");
            String entrada = scanner.nextLine();

            if (entrada.equalsIgnoreCase("salir")) break;

            try {
                String[] valores = entrada.split(" ");
                double a = Double.parseDouble(valores[0]);
                double b = Double.parseDouble(valores[1]);
                double c = Double.parseDouble(valores[2]);

                EcuacionCuadratica ecuacion = (a == 0) ? new SinRaices(a, b, c) :
                        (b * b - 4 * a * c > 0) ? new DosRaices(a, b, c) :
                        (b * b - 4 * a * c == 0) ? new UnaRaiz(a, b, c) : new SinRaices(a, b, c);

                System.out.println(ecuacion.calcular());
            } catch (Exception e) {
                System.out.println("Entrada inválida.");
            }
        }

        scanner.close();
    }
}
