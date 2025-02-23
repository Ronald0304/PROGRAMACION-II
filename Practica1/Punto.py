import math

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)  # Ángulo en radianes
        return r, math.degrees(theta)  # Convertimos el ángulo a grados

    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"

# Ejemplo de uso
p = Punto(3, 4)
print(p)  # Salida: Punto(x=3, y=4)
print("Coordenadas Cartesianas:", p.coord_cartesianas())
print("Coordenadas Polares:", p.coord_polares())
