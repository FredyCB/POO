import json


def cargar_lista() -> list:
    with open("datos.txt") as f:
        data = json.loads(f.read())
        return data


def guardar_lista(lista: list):
    with open("datos.txt", "w") as f:
        f.write(json.dumps(lista))


# Ejecucion principal
a = cargar_lista()
try:
    posicion = int(input("Escriba la posicion: "))
    valor = input("Coloque el nuevo valor: ")
    a[posicion] = valor

    print(a)
    guardar_lista(a)

except IndexError:
    print(f"La posicion debe estar entre 0 y {len(a)}")
except ValueError:
    print(f"La posicion debe ser un numero entero 0 y {len(a)}")
