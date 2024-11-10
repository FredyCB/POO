ls = [10, 20, 10, 40, 10, 60, 10, 5, 10]
posicion = -1
valor = 10
while True:
    try:
        posicion = ls.index(valor, posicion + 1)
        print(f"Aparece el valor {valor} en {posicion}")
    except ValueError:
        break