public class Main {
    public static void main(String[] args) {
        D obj = new D(1, 2, 3);
        System.out.println("Antes: x=" + obj.getX() + ", y=" + obj.getY() + ", z=" + obj.getZ());
        
        obj.incrementaXYZ();
        
        System.out.println("Después de incrementaXYZ: x=" + obj.getX() + ", y=" + obj.getY() + ", z=" + obj.getZ());
    }
}

class Z {
    public int valor;

    public Z(int valor) {
        this.valor = valor;
    }
}

class A {
    private int x;
    private Z z;

    public A(int x, Z z) {
        this.x = x;
        this.z = z;
    }

    public void incrementaXZ() {
        x++;
        z.valor++;
    }

    public void incrementaZ() {
        z.valor++;
    }

    public int getX() {
        return x;
    }

    public Z getZ() {
        return z;
    }

    public void setX(int x) {
        this.x = x;
    }
}

class B {
    private int y;
    private Z z;

    public B(int y, Z z) {
        this.y = y;
        this.z = z;
    }

    public void incrementaYZ() {
        y++;
        z.valor++;
    }

    public void incrementaZ() {
        z.valor++;
    }

    public int getY() {
        return y;
    }

    public Z getZ() {
        return z;
    }

    public void setY(int y) {
        this.y = y;
    }
}

class D {
    private A a;
    private B b;
    private Z z;

    public D(int x, int y, int zValor) {
        this.z = new Z(zValor);
        this.a = new A(x, z);
        this.b = new B(y, z);
    }

    public void incrementaXYZ() {
        a.setX(a.getX() + 1);
        b.setY(b.getY() + 1);
        z.valor++;
    }

    public int getX() {
        return a.getX();
    }

    public int getY() {
        return b.getY();
    }

    public int getZ() {
        return z.valor;
    }
}
