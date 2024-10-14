def pares(limite: int) -> int:
    valor = 0
    lista = []
    while valor <= limite:
        valor += 2
        lista.append(valor)
    return lista


def generador_pares(limite: int) -> int:
    valor = 0
    while valor <= limite:
        yield valor
        valor += 2


for x in generador_pares(20_000_000):
    print(x)


# lista_pares = list(generador_pares(24))
# print(lista_pares)
