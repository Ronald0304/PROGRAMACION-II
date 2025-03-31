import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, list) and len(x) == 3:  # Permite inicializar con una lista
            self.x, self.y, self.z = x
        else:
            self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return AlgebraVectorial(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return AlgebraVectorial(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def dot(self, other):
        """Producto punto entre dos vectores."""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        """Producto cruz entre dos vectores."""
        return AlgebraVectorial(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitude(self):
        """Calcula la magnitud del vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def perpendicular_a_b(self, other):
        """Determina si dos vectores son perpendiculares."""
        return self.dot(other) == 0
    
    def paralela_a_b(self, other):
        """Determina si dos vectores son paralelos."""
        return self.cross(other).magnitude() == 0
    
    def proyeccion_de_a_sobre_b(self, other):
        """Calcula la proyección ortogonal de a sobre b."""
        factor = self.dot(other) / (other.magnitude() ** 2)
        return AlgebraVectorial(factor * other.x, factor * other.y, factor * other.z)
    
    def componente_de_a_en_b(self, other):
        """Calcula el componente de a en la dirección de b."""
        return self.dot(other) / other.magnitude()

# Ejemplo de uso:
vector_a = AlgebraVectorial(3, 4, 0)
vector_b = AlgebraVectorial(6, 8, 0)

print("Perpendicular:", vector_a.perpendicular_a_b(vector_b))
print("Paralela:", vector_a.paralela_a_b(vector_b))
print("Proyección de A sobre B:", vector_a.proyeccion_de_a_sobre_b(vector_b))
print("Componente de A en dirección de B:", vector_a.componente_de_a_en_b(vector_b))
