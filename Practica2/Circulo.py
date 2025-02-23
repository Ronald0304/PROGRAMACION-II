import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"

class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Circulo(centro={self.centro}, radio={self.radio})"

    def dibujaCirculo(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.add_patch(plt.Circle((self.centro.x, self.centro.y), self.radio, color='r', fill=False))
        plt.xlim(self.centro.x - self.radio - 1, self.centro.x + self.radio + 1)
        plt.ylim(self.centro.y - self.radio - 1, self.centro.y + self.radio + 1)
        plt.grid()
        plt.show()

# Ejemplo de uso
circulo = Circulo(Punto(3, 3), 2)

print(circulo)
circulo.dibujaCirculo()
