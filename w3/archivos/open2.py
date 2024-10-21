manejador = open('w3/archivos/the_thirteenth_tale.txt')

# precaucion: esta funcion lee todo el contenido y lo
# dispone en la RAM
#contenido = manejador.read() 
#print(len(contenido), type(contenido))
# print(contenido)

lineas = manejador.readlines()
print(len(lineas), type(lineas))
print(lineas[0])