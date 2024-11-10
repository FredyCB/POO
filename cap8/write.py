indentacion = " " * 4
nombre = input("Escriba el nombre a saludar: ").title()

with open("saludos.py", mode="a") as archivo:
    archivo.write("def saludar():\n")
    archivo.write(indentacion + f"print('Hola {nombre}')\n")
    archivo.write("\n\nsaludar()\n")
