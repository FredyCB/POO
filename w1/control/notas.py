"""
Solicitar una nota (entero) y establecer si el alumno tiene las siguientes
calificaciones:
A = [90, 100]
B = [80, 89]
C = [70, 79]
D = [60, 69]
F = [0, 59]

Ademas indicar si aprobo o no (en caso que sea una F).
"""
nombre = input("Escriba el nombre del alumno: ")
nota = int(input("Escriba la nota del alumno: "))

if nota >= 90 and nota <= 100:
    calificacion = "A"
elif nota >= 80 and nota <= 89:
    calificacion = "B"
elif 70 <= nota <= 79:
    calificacion = "C"
elif 60 <= nota <= 69:
    calificacion = "D"
elif 0 <= nota <= 59:
    calificacion = "F"
else:
    calificacion = "Error"

print("La calificacion de", nombre, "es", calificacion)
