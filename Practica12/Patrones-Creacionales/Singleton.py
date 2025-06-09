class CajeroAutomatico:
    _unico_cajero = None
    
    def __new__(cls):
        if not cls._unico_cajero:
            cls._unico_cajero = super().__new__(cls)
            cls._unico_cajero.saldo = 100000  # Saldo inicial
        return cls._unico_cajero
    
    def retirar_dinero(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f" Retirados Bs {monto}. Saldo restante: Bs {self.saldo}")
        else:
            print(" Fondos insuficientes")
    
    def consultar_saldo(self):
        print(f" Saldo disponible: Bs {self.saldo}")

# Simulación de clientes
cliente1 = CajeroAutomatico()
cliente2 = CajeroAutomatico()

print("¿Mismo cajero?", cliente1 is cliente2)  # True

cliente1.retirar_dinero(13000)
cliente2.consultar_saldo()  # Muestra saldo actualizado
cliente2.retirar_dinero(9000)
cliente1.consultar_saldo()
