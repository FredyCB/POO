'''
Leer el archivo the_thirteenth_tale.txt, identificar la palabra
mas extensa
'''

# from modulo (archivo) import (funcion)
from utils import eliminar_signos

archivo = open('w3/archivos/the_thirteenth_tale.txt')
palabra_extensa = ''
for linea in archivo:
    palabras = linea.split()  # una lista de posibles palabras
    for palabra in palabras:
        palabra_limpia = eliminar_signos(palabra)
        if len(palabra_limpia) > len(palabra_extensa):
            palabra_extensa = palabra_limpia
print("La palabra mas extensa del fichero es: ", palabra_extensa) 