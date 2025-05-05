class LineaTeleferico:
    def __init__(self, color, tramo, numeroCabinas):
        self.color = color
        self.tramo = tramo
        self.numeroCabinas = numeroCabinas
        self.numeroEmpleados = 0
        self.empleados = [] 
        self.edades = []
        self.sueldos = []

    def agregarEmpleado(self, nombre, apellido1, apellido2, edad, sueldo):
        self.empleados.append([nombre, apellido1, apellido2])
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.numeroEmpleados += 1

    def eliminarPorApellido(self, apellido):
        nuevosEmpleados = []
        nuevasEdades = []
        nuevosSueldos = []
        for i in range(self.numeroEmpleados):
            if apellido not in self.empleados[i]:
                nuevosEmpleados.append(self.empleados[i])
                nuevasEdades.append(self.edades[i])
                nuevosSueldos.append(self.sueldos[i])
        self.empleados = nuevosEmpleados
        self.edades = nuevasEdades
        self.sueldos = nuevosSueldos
        self.numeroEmpleados = len(self.empleados)

    def __add__(self, otro):
        def transferirEmpleado(origen, destino, posicion):
            if 0 <= posicion < origen.numeroEmpleados:
                destino.agregarEmpleado(
                    *origen.empleados[posicion],
                    origen.edades[posicion],
                    origen.sueldos[posicion]
                )
                del origen.empleados[posicion]
                del origen.edades[posicion]
                del origen.sueldos[posicion]
                origen.numeroEmpleados -= 1
        return transferirEmpleado

    def mostrarMayorEdad(self):
        if not self.edades:
            print("Sin empleados.")
            return
        mayor = max(self.edades)
        print("Empleado con mayor edad:")
        for i in range(self.numeroEmpleados):
            if self.edades[i] == mayor:
                print(self.empleados[i], "-", self.edades[i], "años")

    def mostrarMayorSueldo(self):
        if not self.sueldos:
            print("Sin empleados.")
            return
        mayor = max(self.sueldos)
        print("Empleado con mayor sueldo:")
        for i in range(self.numeroEmpleados):
            if self.sueldos[i] == mayor:
                print(self.empleados[i], "-", self.sueldos[i], "Bs")

    def __str__(self):
        resultado = f"--- Linea Teleferico ---\n"
        resultado += f"Color: {self.color}\nTramo: {self.tramo}\nCabinas: {self.numeroCabinas}\n"
        resultado += f"Numero de Empleados: {self.numeroEmpleados}\n"
        resultado += f"{'Nombre Completo':30} {'Edad':5} {'Sueldo'}\n"
        resultado += "-" * 50 + "\n"
        for i in range(self.numeroEmpleados):
            nombreCompleto = " ".join(self.empleados[i])
            resultado += f"{nombreCompleto:30} {self.edades[i]:5} {self.sueldos[i]}\n"
        return resultado
linea1 = LineaTeleferico("Rojo", "Estacion Central - Cementerio - 16 de Julio", 20)
linea2 = LineaTeleferico("Verde", "Obrajes - Alto Obrajes", 15)

linea1.agregarEmpleado("Pedro", "Rojas", "Luna", 35, 2500)
linea1.agregarEmpleado("Lucy", "Sosa", "Rios", 43, 3250)
linea1.agregarEmpleado("Ana", "Perez", "Rojas", 26, 2700)
linea1.agregarEmpleado("Saul", "Arce", "Calle", 29, 2500)

linea2.agregarEmpleado("Mario", "Torres", "Vera", 45, 3000)
linea2.agregarEmpleado("Laura", "Quispe", "Mamani", 28, 2800)
linea2.agregarEmpleado("Luis", "Gomez", "Perez", 33, 2500)

print(linea1)
print(linea2)

linea1.eliminarPorApellido("Rojas")
print("\nDespues de eliminar apellido 'Rojas':")
print(linea1)

transferir = linea2 + linea1
transferir(linea2, linea1, 1)  
print("\nDespues de transferir empleado de linea2 a linea1:")
print(linea1)

print("\n[Mayor Edad]")
linea1.mostrarMayorEdad()

print("\n[Mayor Sueldo]")
linea1.mostrarMayorSueldo()
