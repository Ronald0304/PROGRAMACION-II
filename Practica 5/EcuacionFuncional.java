import java.util.Scanner;

public class EcuacionFuncional {
    public static double getDiscriminante(double a, double b, double c) {
        return b * b - 4 * a * c;
    }

    public static double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    public static double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }

    public static void resolverEcuacion(double a, double b, double c) {
        double discriminante = getDiscriminante(a, b, c);

        if (discriminante > 0) {
            double r1 = getRaiz1(a, b, discriminante);
            double r2 = getRaiz2(a, b, discriminante);
            System.out.printf("La ecuación tiene dos raíces %.5f y %.5f%n", r1, r2);
        } else if (discriminante == 0) {
            double r = -b / (2 * a);
            System.out.printf("La ecuación tiene una raíz %.5f%n", r);
        } else {
            System.out.println("La ecuación no tiene raíces reales");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.print("Ingrese a, b, c (o escriba 'salir' para terminar): ");
            String entrada = scanner.nextLine();
            
            if (entrada.equalsIgnoreCase("salir")) {
                System.out.println("Programa terminado.");
                break;
            }
            
            try {
                String[] valores = entrada.split(" ");
                double a = Double.parseDouble(valores[0]);
                double b = Double.parseDouble(valores[1]);
                double c = Double.parseDouble(valores[2]);
                resolverEcuacion(a, b, c);
            } catch (Exception e) {
                System.out.println("Entrada inválida. Asegúrese de ingresar tres números separados por espacios.");
            }
        }

        scanner.close();
    }
}
