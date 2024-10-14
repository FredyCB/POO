# Esta funcion retorna TODOS los numeros pares hasta el limite dado. Es necesario
# almacenar todos los valores en memoria, lo cual puede ser ineficiente si el limite
# es muy grande.
def pares(limite: int) -> int:
    valor = 0
    lista = []
    while valor <= limite:
        valor += 2
        lista.append(valor)
    return lista


# Este es un generador que retorna los numeros pares hasta el limite dado.
# La diferencia entre un generador y una funcion normal es que el generador
# no almacena todos los valores en memoria, sino que los va generando uno a uno.
def generador_pares(limite: int):
    valor = 0
    while valor <= limite:
        yield valor
        valor += 2


# El generador retorna un nuevo par en cada iteracion
for x in generador_pares(200_000):
    print(x)
