import random
from urllib.request import urlopen

recurso = urlopen('http://data.pr4e.org/romeo.txt')
for linea in recurso:
    print(linea.decode().strip())


imagen = urlopen("http://data.pr4e.org/cover3.jpg")
# create a random filename
filename = f"archivo_{random.randint(1, 1000)}.jpg"
with open(filename, "wb") as archivo:
    archivo.write(imagen.read())
