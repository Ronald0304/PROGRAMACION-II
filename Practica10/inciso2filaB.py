class Ministerio:
    def __init__(self, nombre, direccion,):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = 0
        self.empleados = []  
        self.edades = []
        self.sueldos = []
        

    def agregarEmpleado(self, nombreCompleto, edad, sueldo):
        self.empleados.append(nombreCompleto)
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1
        
    def __str__(self):
        salida = f"\n--- DATOS DEL MINISTERIO ---\n"
        salida += f"Nombre       : {self.nombre}\n"
        salida += f"Dirección    : {self.direccion}\n"
        salida += f"NroEmpleados : {self.nroEmpleados}\n"
        salida += "\n--- LISTA DE EMPLEADOS ---\n"
        for i in range(self.nroEmpleados):
            salida += f"{i+1}. {self.empleados[i]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]} Bs\n"
        return salida

    def eliminarEmpleadosPorEdad(self, edad):
        nuevosEmpleados = []
        nuevasEdades = []
        nuevosSueldos = []

        for i in range(self.nroEmpleados):
            if self.edades[i] != edad:
                nuevosEmpleados.append(self.empleados[i])
                nuevasEdades.append(self.edades[i])
                nuevosSueldos.append(self.sueldos[i])

        self.empleados = nuevosEmpleados
        self.edades = nuevasEdades
        self.sueldos = nuevosSueldos
        self.nroEmpleados = len(self.empleados)

    def __lshift__(self, otro):
        origen, indice = otro
        if 0 <= indice < origen.nroEmpleados:
            self.agregarEmpleado(
                origen.empleados[indice],
                origen.edades[indice],
                origen.sueldos[indice]
            )
            del origen.empleados[indice]
            del origen.edades[indice]
            del origen.sueldos[indice]
            origen.nroEmpleados -= 1

    def mostrarEmpleadosMenorEdad(self):
        if not self.edades:
            print("No hay empleados.")
            return
        menor = min(self.edades)
        print(f"\nEmpleados con menor edad ({menor} años):")
        for i in range(self.nroEmpleados):
            if self.edades[i] == menor:
                print(f"{self.empleados[i]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

    def mostrarEmpleadosMenorSueldo(self):
        if not self.sueldos:
            print("No hay empleados.")
            return
        menor = min(self.sueldos)
        print(f"\nEmpleados con menor sueldo ({menor} Bs):")
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == menor:
                print(f"{self.empleados[i]} - Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")


# (a) Instanciar 2 objetos Ministerio de diferente forma
m1 = Ministerio("Ministerio de Educación", "Av. Camacho #100")
m2 = Ministerio("Ministerio de Salud", "Plaza del Estudiante")

m1.agregarEmpleado("Pedro Rojas Luna", 35, 2500)
m1.agregarEmpleado("Lucy Sosa Rios", 43, 3250)
m1.agregarEmpleado("Carlos Vega Duran", 30, 2800)
m1.agregarEmpleado("María López Quiroga", 26, 3100)

m2.agregarEmpleado("Ana Perez Rojas", 26, 2700)
m2.agregarEmpleado("Saul Arce Calle", 29, 2500)
m2.agregarEmpleado("Luis Mendoza Soliz", 45, 4000)
m2.agregarEmpleado("Elena Vargas Soto", 27, 2600)

print(m1)
print(m2)

# (b) Eliminar empleados con edad x en m2
print("\n>> Eliminando empleados con edad 29 en Ministerio 2")
m2.eliminarEmpleadosPorEdad(29)
print("\nMinisterio 2 actualizado:")
print (m2)

# (c) Transferir al empleado 2 de m2 al m1
print("\n>> Transfiriendo el empleado 2 del Ministerio 2 al Ministerio 1")
m1 << (m2, 2)

print("\nMinisterio 1 y 2 actualizados:")
print(m1)
print(m2)

# (d) Mostrar empleados con menor edad y menor sueldo
print("\n>> Empleados con menor edad en Ministerio 1:")
m1.mostrarEmpleadosMenorEdad()
print("\n>> Empleados con menor edad en Ministerio 2:")
m2.mostrarEmpleadosMenorEdad()

print("\n>> Empleados con menor sueldo en Ministerio 1:")
m1.mostrarEmpleadosMenorSueldo()
print("\n>> Empleados con menor sueldo en Ministerio 2:")
m2.mostrarEmpleadosMenorSueldo()
