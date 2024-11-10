'''
Leer el archivo the_thirteenth_tale.txt y buscar las apariciones
de una palabra en particular
'''

from utils import eliminar_signos


buscar = input("Buscar la siguiente palabra: ").lower()

archivo = open('w3/archivos/the_thirteenth_tale.txt')

contenido = archivo.read()  # precaucion: lee todo el archivo
apariciones = 0
for palabra in contenido.split():
    _palabra = eliminar_signos(palabra).lower()
    if buscar == _palabra:
        apariciones += 1

print(f"Aparece {apariciones} veces...")
