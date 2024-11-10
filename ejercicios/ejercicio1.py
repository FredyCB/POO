temperaturas = [19, 24, 24, 30, 31, 30, 29]
dias = ("Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado")

temperatura_min = min(temperaturas)
print(temperatura_min)

temperatura_max = max(temperaturas)
print(temperatura_max)

pos_min = temperaturas.index(temperatura_min)
pos_max = temperaturas.index(temperatura_max)

print("El primer dia con la temp mas baja fue: ", dias[pos_min])
print("El primer dia con la temp mas alta fue: ", dias[pos_max])

temperatura_avg = sum(temperaturas) / len(temperaturas)
temperatura_arriba_avg = []
# Aqui estan los valores por encima del promedio
for temp in temperaturas:
    if temp > temperatura_avg:
        temperatura_arriba_avg.append(temp)

# Los dias por encima del promedio
dias_arriba_avg = []
for pos, temp in enumerate(temperaturas):
    if temp > temperatura_avg:
        dias_arriba_avg.append(dias[pos])

print("Promedio: ", temperatura_avg)
print("Todas las temperaturas arriba del promedio son: ", temperatura_arriba_avg)
print("Y los dias serian:", dias_arriba_avg)