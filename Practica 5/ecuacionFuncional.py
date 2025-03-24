import math

def getDiscriminante(a, b, c):
    return b**2 - 4*a*c

def getRaiz1(a, b, discriminante):
    return (-b + math.sqrt(discriminante)) / (2 * a)

def getRaiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def resolver_ecuacion(a, b, c):
    discriminante = getDiscriminante(a, b, c)

    if discriminante > 0:
        r1 = getRaiz1(a, b, discriminante)
        r2 = getRaiz2(a, b, discriminante)
        print(f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}")
    elif discriminante == 0:
        r = -b / (2 * a)
        print(f"La ecuación tiene una raíz {r:.5f}")
    else:
        print("La ecuación no tiene raíces reales")

while True:
    entrada = input("Ingrese a, b, c (o escriba 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Programa terminado.")
        break
    try:
        a, b, c = map(float, entrada.split())
        resolver_ecuacion(a, b, c)
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar tres números separados por espacios.")
