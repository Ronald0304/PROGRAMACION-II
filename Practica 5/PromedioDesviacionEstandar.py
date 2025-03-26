import math
# Función para calcular promedio
def promedio(lista):
    return sum(lista) / len(lista)
# Función para calcular desviación estándar
def desviacion(lista):
    prom = promedio(lista)
    suma = 0
    for x in lista:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (len(lista) - 1))

# Programa principal
numeros = []
print("Ingresa 10 números:")

for i in range(10):
    n = float(input(f"Número {i+1}: "))
    numeros.append(n)

prom = promedio(numeros)
desv = desviacion(numeros)

print(f"\nEl promedio es {round(prom, 2)}")
print(f"La desviación estándar es {round(desv, 4)}")
