temperaturas = [19, 24, 19, 30, 31, 31, 29]
dias = ("Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado")

dic = dict(zip(dias, temperaturas))

val_min = min(dic.values())
val_max = max(dic.values())

print("Estos son los dias mas bajos:")
for clave, valor in dic.items():
    if valor == val_min:
        print(clave)

print("Estos son los dias mas altos:")
for clave, valor in dic.items():
    if valor == val_max:
        print(clave)

temp_avg = sum(dic.values()) / len(dic)
print("Promedio:", temp_avg)
dias_mayor_avg = [clave for clave, valor in dic.items() if valor > temp_avg]
print("Dias mayores al promedio de temp:", dias_mayor_avg)