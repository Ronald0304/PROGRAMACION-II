import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea({self.p1}, {self.p2})"

    def dibujaLinea(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], 'bo-')
        plt.xlim(min(self.p1.x, self.p2.x) - 1, max(self.p1.x, self.p2.x) + 1)
        plt.ylim(min(self.p1.y, self.p2.y) - 1, max(self.p1.y, self.p2.y) + 1)
        plt.grid()
        plt.show()

# Ejemplo de uso
p1 = Punto(1, 2)
p2 = Punto(4, 6)
linea = Linea(p1, p2)

print(linea)
linea.dibujaLinea()
