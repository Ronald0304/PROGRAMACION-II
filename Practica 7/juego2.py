import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numeroDeVidas = numero_de_vidas
        self.record = 0
        self.puntaje_actual = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3  # Se puede modificar 
        self.puntaje_actual = 0
        print("Juego reiniciado. Tienes", self.numeroDeVidas, "vidas.")

    def actualizaRecord(self):
        self.puntaje_actual += 1
        if self.puntaje_actual > self.record:
            self.record = self.puntaje_actual
            print("¡Nuevo record actualizado! Record actual:", self.record)
        else:
            print("Puntaje actual:", self.puntaje_actual, "| Record actual:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te queda(n)", self.numeroDeVidas, "vida(s).")
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)
        self.numeroAAdivinar = None

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def generaNumeroAAdivinar(self):
        return random.randint(0, 10)

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = self.generaNumeroAAdivinar()
        print("Adivina un número entre 0 y 10.")

        while self.numeroDeVidas > 0:
            try:
                intento = int(input("Introduce tu número: "))
                if not self.validaNumero(intento):
                    print("Número fuera de rango. Debe estar entre 0 y 10.")
                    continue

                if intento == self.numeroAAdivinar:
                    print("¡Acertaste!")
                    self.actualizaRecord()
                    self.numeroAAdivinar = self.generaNumeroAAdivinar()
                    print("Nuevo número generado. Sigue jugando!")
                else:
                    if not self.quitaVida():
                        print("No te quedan más vidas. El número era", self.numeroAAdivinar)
                        break
                    else:
                        if intento < self.numeroAAdivinar:
                            print("El número es mayor. Intenta de nuevo.")
                        else:
                            print("El número es menor. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Introduce un número entero.")

        print("Juego terminado. Tu record final fue:", self.record)
        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if jugar_de_nuevo == 's':
            self.juega()
        else:
            print("Gracias por jugar. ¡Hasta la próxima!")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 == 0:
                return True
            else:
                print("Error: el número no es par.")
                return False
        print("Número fuera de rango. Debe ser par y estar entre 0 y 10.")
        return False

    def generaNumeroAAdivinar(self):
        return random.choice([x for x in range(0, 11) if x % 2 == 0])

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 == 1:
                return True
            else:
                print("Error: el número no es impar.")
                return False
        print("Número fuera de rango. Debe ser impar y estar entre 0 y 10.")
        return False

    def generaNumeroAAdivinar(self):
        return random.choice([x for x in range(0, 11) if x % 2 == 1])

# Clase Aplicacion
if __name__ == "__main__":
    print("Selecciona el tipo de juego:")
    print("1. Adivina cualquier número")
    print("2. Adivina solo pares")
    print("3. Adivina solo impares")
    opcion = input("Ingresa el número de opción: ").strip()

    if opcion == '1':
        juego = JuegoAdivinaNumero(3)
    elif opcion == '2':
        juego = JuegoAdivinaPar(3)
    elif opcion == '3':
        juego = JuegoAdivinaImpar(3)
    else:
        print("Opción no válida. Se usará el juego estándar.")
        juego = JuegoAdivinaNumero(3)

    juego.juega()
