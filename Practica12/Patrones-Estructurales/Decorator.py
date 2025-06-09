from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def obtener_descripcion(self):
        pass

    @abstractmethod
    def obtener_costo(self):
        pass

class CafeBase(Bebida):
    def obtener_descripcion(self):
        return "Café simple"

    def obtener_costo(self):
        return 2.00

class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida

class ConLeche(DecoradorBebida):
    def obtener_descripcion(self):
        return self._bebida.obtener_descripcion() + ", leche"

    def obtener_costo(self):
        return self._bebida.obtener_costo() + 0.50

class ConChocolate(DecoradorBebida):
    def obtener_descripcion(self):
        return self._bebida.obtener_descripcion() + ", chocolate"

    def obtener_costo(self):
        return self._bebida.obtener_costo() + 0.75

class ConCanela(DecoradorBebida):
    def obtener_descripcion(self):
        return self._bebida.obtener_descripcion() + ", canela"

    def obtener_costo(self):
        return self._bebida.obtener_costo() + 0.30

def main():
    bebida = CafeBase()
    bebida = ConLeche(bebida)
    bebida = ConChocolate(bebida)

    print("Descripción:", bebida.obtener_descripcion())
    print("Costo total: $", round(bebida.obtener_costo(), 2))

    bebida2 = CafeBase()
    bebida2 = ConLeche(bebida2)
    bebida2 = ConChocolate(bebida2)
    bebida2 = ConCanela(bebida2)

    print("\nDescripción:", bebida2.obtener_descripcion())
    print("Costo total: $", round(bebida2.obtener_costo(), 2))

if __name__ == "__main__":
    main()
