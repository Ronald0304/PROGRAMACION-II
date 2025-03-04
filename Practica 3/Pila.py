class Pila:
    def __init__(self, n: int):
        self.n = n
        self.arreglo = [0] * n
        self.top = -1

    def push(self, e: int):
        if not self.isFull():
            self.top += 1
            self.arreglo[self.top] = e
        else:
            print("La pila está llena")

    def pop(self) -> int:
        if not self.isEmpty():
            valor = self.arreglo[self.top]
            self.top -= 1
            return valor
        else:
            print("La pila está vacía")
            return -1

    def peek(self) -> int:
        if not self.isEmpty():
            return self.arreglo[self.top]
        else:
            print("La pila está vacía")
            return -1

    def isEmpty(self) -> bool:
        return self.top == -1

    def isFull(self) -> bool:
        return self.top == self.n - 1
