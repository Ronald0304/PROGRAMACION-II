import random

class Juego:

    def __init__(self, numero_de_vidas):
        self.numeroDeVidas = numero_de_vidas
        self.record = 0
        self.puntaje_actual = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3  # Se puede modificar según necesidad
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

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10.")

        while self.numeroDeVidas > 0:
            try:
                intento = int(input("Introduce tu número: "))
                if intento == self.numeroAAdivinar:
                    print("¡Acertaste!")
                    self.actualizaRecord()
                    self.numeroAAdivinar = random.randint(0, 10)  # Genera un nuevo número
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

# Clase Aplicacion
if __name__ == "__main__":
    juego = JuegoAdivinaNumero(3)  # Número de vidas inicial
    juego.juega()
