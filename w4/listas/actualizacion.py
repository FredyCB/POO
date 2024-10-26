def cargar_lista() -> list:
    with open("datos.txt") as f:
        s = f.read()
        return s[1 : len(s) - 1].split(", ")


a = cargar_lista()
try:
    posicion = int(input("Escriba la posicion: "))
    valor = input("Coloque el nuevo valor: ")
    a[posicion] = valor
    print(a)

    with open("datos.txt", "w") as archivo:
        archivo.write(str(a))

except IndexError:
    print(f"La posicion debe estar entre 0 y {len(a)}")
except ValueError:
    print(f"La posicion debe ser un numero entero 0 y {len(a)}")
    


