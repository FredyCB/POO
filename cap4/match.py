"""
Dado un numero entre 0 y 6 determinar el dia de la semana.

Se utilizará la estructura match para simplificar el codigo. Es parecido a un
switch en otros lenguajes.
"""

numero_dia = int(input("Ingrese un numero (0-6): "))

match numero_dia:
    case 0:
        dia = "Domingo"
    case 1:
        dia = "Lunes"
    case 2:
        dia = "Martes"
    case 3:
        dia = "Miercoles"
    case 4:
        dia = "Jueves"
    case 5:
        dia = "Viernes"
    case 6:
        dia = "Sabado"
    case _:
        dia = "Error"


print("El dia es:", dia)
