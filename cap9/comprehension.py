# crear una lista de pares del 1 al 20
lista = []
for num in range(2, 21, 2):
    val = num ** 2
    if val >= 100:
        lista.append(val)
print(lista)

# comprehension [valor for valor in iterable if filtro]
print("Por comprehension")
pares = [numero**2 for numero in range(2, 21, 2) if numero**2 >= 100]
print(pares)

