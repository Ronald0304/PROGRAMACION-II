import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminante = self.getDiscriminante()

    def getDiscriminante(self):
        return self.b**2 - 4 * self.a * self.c

    def resolver(self):
        if self.discriminante > 0:
            return DosRaices(self.a, self.b, self.discriminante).calcular()
        elif self.discriminante == 0:
            return UnaRaiz(self.a, self.b).calcular()
        else:
            return SinRaices().calcular()

class DosRaices(EcuacionCuadratica):
    def calcular(self):
        r1 = (-self.b + math.sqrt(self.discriminante)) / (2 * self.a)
        r2 = (-self.b - math.sqrt(self.discriminante)) / (2 * self.a)
        return f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}"

class UnaRaiz(EcuacionCuadratica):
    def calcular(self):
        r = -self.b / (2 * self.a)
        return f"La ecuación tiene una raíz {r:.5f}"

class SinRaices(EcuacionCuadratica):
    def calcular(self):
        return "La ecuación no tiene raíces reales"

while True:
    entrada = input("Ingrese a, b, c (o escriba 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
    try:
        a, b, c = map(float, entrada.split())
        ecuacion = EcuacionCuadratica(a, b, c)
        print(ecuacion.resolver())
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar tres números separados por espacios.")
