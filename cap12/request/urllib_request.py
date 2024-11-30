import random
from urllib.request import urlopen

# Extracción y visualización de contenido de un archivo de texto
recurso = urlopen('http://data.pr4e.org/romeo.txt')
for linea in recurso:
    print(linea.decode().strip())

# Extracción y guardado de un archivo de imagen
imagen = urlopen("http://data.pr4e.org/cover3.jpg")
filename = f"archivo_{random.randint(1, 1000)}.jpg"
with open(filename, "wb") as archivo:
    archivo.write(imagen.read())
