import random
import requests

# Fetching and printing text file content
recurso_url = 'http://data.pr4e.org/romeo.txt'
response = requests.get(recurso_url)
if response.status_code == 200:
    for linea in response.text.splitlines():
        print(linea.strip())
else:
    print(f"Error fetching the resource: {response.status_code}")

# Fetching and saving an image file
imagen_url = "http://data.pr4e.org/cover3.jpg"
response = requests.get(imagen_url)
if response.status_code == 200:
    # create a random filename
    filename = f"archivo_{random.randint(1, 1000)}.jpg"
    with open(filename, "wb") as archivo:
        archivo.write(response.content)
    print(f"Image saved as {filename}")
else:
    print(f"Error fetching the image: {response.status_code}")
