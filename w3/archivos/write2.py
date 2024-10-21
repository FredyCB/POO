with open("w3/archivos/numeros.txt", mode="w") as archivo:
    for numero in range(1, 101):
        archivo.write(str(numero))
        archivo.write("\n")
