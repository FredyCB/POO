#  Concatenar cadenas
parte1 = "Hola"
parte2 = "Mundo"
saludo = parte1 + " " + parte2
print("Concatenación:", saludo)
# Salida: Concatenación: Hola Mundo

# Repetir una cadena
texto = "Hola"
repetido = texto * 3
print("Repetición:", repetido)
# Salida: Repetición: HolaHolaHola

# Convertir a mayúsculas
texto = "hola mundo"
mayusculas = texto.upper()
print("Mayúsculas:", mayusculas)
# Salida: Mayúsculas: HOLA MUNDO

# Convertir a minúsculas
texto = "HOLA MUNDO"
minusculas = texto.lower()
print("Minúsculas:", minusculas)
# Salida: Minúsculas: hola mundo

# Capitalizar (primera letra en mayúsculas)
texto = "hola mundo"
capitalizado = texto.capitalize()
print("Capitalizado:", capitalizado)
# Salida: Capitalizado: Hola mundo

#  Cambiar el formato de palabras (Title Case)
texto = "aprendiendo python es divertido"
titulo = texto.title()
print("Title Case:", titulo)
# Salida: Title Case: Aprendiendo Python Es Divertido

# Centrar un texto
texto = "Python"
centrado = texto.center(20)
print("Centrado: '", centrado, "'")
# Salida: Centrado: '        Python        '

# Dividir un string en una lista
texto = "manzana, banana, cereza"
frutas = texto.split(", ")
print("Frutas:", frutas)
# Salida: Frutas: ['manzana', 'banana', 'cereza']

# Unir una lista en un string
frutas = ["manzana", "banana", "cereza"]
texto = ", ".join(frutas)
print("Texto unificado:", texto)
# Salida: Texto unificado: manzana, banana, cereza

# Reemplazar un valor dentro del string
texto = "Tengo un coche azul"
nuevo_texto = texto.replace("azul", "rojo")
print("Texto modificado:", nuevo_texto)
# Salida: Texto modificado: Tengo un coche rojo

# Quitar espacios en blanco al inicio y al final
texto = "   hola mundo   "
sin_espacios = texto.strip()
print("Sin espacios:", sin_espacios)
# Salida: Sin espacios: hola mundo

#  Verificar si una cadena es numérica
texto = "12345"
es_numerico = texto.isdigit()
print("Es numérico:", es_numerico)
# Salida: Es numérico: True

# Contar ocurrencias de una subcadena
texto = "abracadabra"
contador = texto.count("a")
print("Número de 'a':", contador)
# Salida: Número de 'a': 5

# Verificar si una cadena empieza o termina con algo específico
texto = "Python es genial"
empieza_con = texto.startswith("Python")
termina_con = texto.endswith("genial")
print("Empieza con 'Python':", empieza_con)
print("Termina con 'genial':", termina_con)
# Salida: Empieza con 'Python': True
# Salida: Termina con 'genial': True

# Encontrar la posición de una subcadena
texto = "Me gusta programar en Python"
posicion = texto.find("Python")
print("Posición de 'Python':", posicion)
# Salida: Posición de 'Python': 22

# Tambien se puede buscar con index
texto = "Me gusta programar en Python"
posicion = texto.index("Python")
print("Posición de 'Python':", posicion)
# Salida: Posición de 'Python': 22

# La diferencia entre find e index es que find retorna -1 si no encuentra la subcadena,
# mientras que index lanza una excepción ValueError
texto = "Me gusta programar en Python"
posicion = texto.find("Java")
print("Posición de 'Java':", posicion)
# Salida: Posición de 'Java': -1

# texto = "Me gusta programar en Python"
posicion = texto.index("Java")
# print("Posición de 'Java':", posicion)
# Salida: ValueError: substring not found