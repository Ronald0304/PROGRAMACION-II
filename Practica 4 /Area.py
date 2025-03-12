import math

class Figura:
    def area(self):
        pass  # Método abstracto

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

class Pentagono(Figura):
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def area(self):
        return (5 * self.lado * self.apotema) / 2

# Creación de objetos y pruebas
figuras = [
    Circulo(5),
    Rectangulo(10, 4),
    Trapecio(8, 5, 3),
    Pentagono(6, 4)
]

for figura in figuras:
    print(f"Área de {figura.__class__.__name__}: {figura.area()}")
