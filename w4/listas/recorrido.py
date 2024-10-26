# inicializacion vacia
cosas = []
cosas = list()

cosas = [10, 3.4, False, "hola", [1, 2, 3]]
print(len(cosas))

print("Forma convencional")
for elemento in cosas:
    print(elemento)

print("Forma antigua")
for indice in range(len(cosas)):
    print(cosas[indice])

print("Usando enumerate")
# si deseo conocer tanto posicion como valor del elemento
for posicion, valor in enumerate(cosas):
    print(posicion, ">>", valor)

print("Con while")
pos = 0
while pos < len(cosas):
    print(cosas[pos])
    pos += 1