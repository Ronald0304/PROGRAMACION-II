class Cola:
    def __init__(self, n: int):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.elementos = 0

    def insert(self, e: int):
        if not self.isFull():
            self.fin = (self.fin + 1) % self.n
            self.arreglo[self.fin] = e
            self.elementos += 1
        else:
            print("La cola está llena")

    def remove(self) -> int:
        if not self.isEmpty():
            valor = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n
            self.elementos -= 1
            return valor
        else:
            print("La cola está vacía")
            return -1

    def peek(self) -> int:
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        else:
            print("La cola está vacía")
            return -1

    def isEmpty(self) -> bool:
        return self.elementos == 0

    def isFull(self) -> bool:
        return self.elementos == self.n

    def size(self) -> int:
        return self.elementos
