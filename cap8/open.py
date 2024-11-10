'''
Modos:
r - read (este el modo predeterminado)
w - escritura (reemplazo)
a - escritura (agregado)
'''

# Ejecutar python open.py 
manejador = open('w3/archivos/the_thirteenth_tale.txt')

contador = 0
contador_parrafos = 0
for linea in manejador:
    contador += 1
    print(contador, ">", linea)

    if len(linea.strip()) > 0:
        contador_parrafos += 1

print(f"** Hay {contador_parrafos} parrafos...")