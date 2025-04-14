class A {
    public int x;
    public int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        x++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

class B {
    public int y;
    public int z;

    public B(int y, int z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }
}

public class D {
    public int x, y, z;

    public D(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // Métodos equivalentes a los de A y B
    public void incrementaXZ() {
        x++;
        z++;
    }

    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }

    public void incrementaXYZ() {
        x++;
        y++;
        z++;
    }

    public void mostrar(String mensaje) {
        System.out.println(mensaje + ": x=" + x + ", y=" + y + ", z=" + z);
    }

    public static void main(String[] args) {
        D obj = new D(1, 2, 3);
        obj.mostrar("Antes");

        obj.incrementaXYZ();
        obj.mostrar("Después de incrementaXYZ");

        obj.incrementaXZ();
        obj.mostrar("Después de incrementaXZ");

        obj.incrementaYZ();
        obj.mostrar("Después de incrementaYZ");

        obj.incrementaZ();
        obj.mostrar("Después de incrementaZ");
    }
}
