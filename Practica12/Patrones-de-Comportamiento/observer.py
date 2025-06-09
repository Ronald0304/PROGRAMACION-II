class EstacionMeteorologica:
    def __init__(self):
        self.suscriptores = []
        self.clima = "soleado"
    
    def agregar_suscriptor(self, suscriptor):
        self.suscriptores.append(suscriptor)
        print(f" {type(suscriptor).__name__} suscrito")
    
    def eliminar_suscriptor(self, suscriptor):
        self.suscriptores.remove(suscriptor)
    
    def cambiar_clima(self, nuevo_clima):
        print(f"\n Cambio de clima: {self.clima} → {nuevo_clima}")
        self.clima = nuevo_clima
        self.notificar_cambio()
    
    def notificar_cambio(self):
        for sus in self.suscriptores:
            sus.actualizar(self.clima)

class Agricultor:
    def actualizar(self, clima):
        if clima == "lluvia":
            print(" Agricultor: ¡Bueno para mis cultivos!")
        else:
            print(" Agricultor: Necesito regar manualmente")

class Turista:
    def actualizar(self, clima):
        if clima == "soleado":
            print(" Turista: ¡Día perfecto para la playa!")
        else:
            print(" Turista: Visitaré museos hoy")

estacion = EstacionMeteorologica()
a1 = Agricultor()
t1 = Turista()

estacion.agregar_suscriptor(a1)
estacion.agregar_suscriptor(t1)

estacion.cambiar_clima("lluvia")
estacion.cambiar_clima("soleado")
