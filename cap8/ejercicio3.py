'''
Crear un programa que permite registrar los siguientes datos:
- Cuenta
- Nombre
- Parcial 1
- Parcial 2
- Parcial 3
- Calcular promedio

Esto debe guardarse en un archivo CSV (Comma separated values)

'''

while True:
    print("[1] Ingresar datos")
    print("[2] Finalizar proceso")
    opcion = input("Elija una opcion: ")

    if opcion == 1:
        cuenta = input("Cuenta: ")
        nombre = input("Nombre: ")
        parcial1 = float(input("Nota del Parcial 1: "))
        parcial2 = float(input("Nota del Parcial 2: "))
        parcial3 = float(input("Nota del Parcial 3: "))
        promedio = round((parcial1 + parcial2 + parcial3), 0)


    elif opcion == 2:
        break