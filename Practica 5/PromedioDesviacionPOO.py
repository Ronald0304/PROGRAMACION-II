import math
class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros
    def promedio(self):
        return sum(self.numeros) / len(self.numeros)
    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for x in self.numeros:
            suma += (x - prom) ** 2
        return math.sqrt(suma / (len(self.numeros) - 1))

# Programa principal
numeros = []
print("Ingresa 10 números:")

for i in range(10):
    n = float(input(f"Número {i+1}: "))
    numeros.append(n)

estadistica = Estadistica(numeros)
print(f"\nEl promedio es {round(estadistica.promedio(), 2)}")
print(f"La desviación estándar es {round(estadistica.desviacion(), 4)}")
