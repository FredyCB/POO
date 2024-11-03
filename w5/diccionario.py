# [10, 20, 30]
#  0   1   2

from pprint import pprint

'''
{
    clave1: valor1,  <-- elemento
    clave2: valor2,  <-- elemento
}

claves son unicas, son inmutables
valor no tienen restricciones
'''

paises = {}
paises = dict()

paises = {
    "HN": {
        "nombre": "Honduras",
        "capital": "Tegucigalpa",
        "extension": "112777",
        "idioma": "es",
    },
    "ES": {
        "idioma": "es",
        "capital": "San Salvador",
        "nombre": "El Salvador",
    }
}

#eliminado = paises.pop("HN")
#pprint(eliminado)
#del paises["ES"]

# Agregar un elemento al diccionario
paises["MX"] = {
    "nombre": "Mexico",
    "capital": "Ciudad de Mexico",
    "idioma": "es",
}

codigo = input("Codigo del pais: ")
buscar = paises.get(codigo, "No esta el pais indicado")
print(buscar)
# if codigo not in paises:
#     print("*** No esta: ", codigo)
# else:
#     print(paises[codigo])
# pprint(paises)