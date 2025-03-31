import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    # Suma de dos vectores
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    # Multiplicación por un escalar
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
        raise TypeError("El escalar debe ser un número real.")
    
    # Longitud del vector
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    # Normalización del vector
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("No se puede normalizar un vector de magnitud cero.")
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)
    
    # Producto escalar
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    # Producto vectorial
    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
# Ejemplo de uso
if __name__ == "__main__":
    a = Vector3D(3, 4, 5)
    b = Vector3D(1, 2, 3)
    
    print("Vector a:", a)
    print("Vector b:", b)
    print("Suma a + b:", a + b)
    print("Multiplicación de a por 2:", a * 2)
    print("Magnitud de a:", a.magnitude())
    print("Vector a normalizado:", a.normalize())
    print("Producto escalar a · b:", a.dot(b))
    print("Producto vectorial a × b:", a.cross(b))
  
