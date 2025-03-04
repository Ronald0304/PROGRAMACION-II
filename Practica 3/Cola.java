public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int elementos;

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.elementos = 0;
    }

    public void insert(long e) {
        if (!isFull()) {
            fin = (fin + 1) % n;
            arreglo[fin] = e;
            elementos++;
        } else {
            System.out.println("La cola está llena");
        }
    }

    public long remove() {
        if (!isEmpty()) {
            long valor = arreglo[inicio];
            inicio = (inicio + 1) % n;
            elementos--;
            return valor;
        } else {
            System.out.println("La cola está vacía");
            return -1;
        }
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[inicio];
        } else {
            System.out.println("La cola está vacía");
            return -1;
        }
    }

    public boolean isEmpty() {
        return elementos == 0;
    }

    public boolean isFull() {
        return elementos == n;
    }

    public int size() {
        return elementos;
    }
}
