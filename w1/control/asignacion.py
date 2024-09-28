"""
En este ejemplo se muestra como se puede asignar un valor a una variable de
forma condicional.
"""

num = int(input("Escriba un numero para saber si es par o impar: "))

# asignacion condicional (pythonic)
etiqueta = "par" if num % 2 == 0 else "impar"
print("Es", etiqueta)

print("Fin del programa")
