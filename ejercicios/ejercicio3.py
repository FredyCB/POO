from pprint import pprint

texto = """
España dominó las Islas Filipinas por más de Tres siglos y medio durante los cuales abusos de la frailocracia y de la Administración acabaron con la paciencia de los naturales obligándoles en los días 26 al 31 de Agosto de 1896 á sacudir tan pesado yugo iniciando la revolución las provincias de Manila y Cavite

En tan gloriosos días levantáronse Balintawak Santa Mesa Kalookan Kawit Noveleta y San Francisco de Malabon proclamando la independencia de Filipinas seguidos á los cinco días por todos los demás pueblos de la provincia de Cavite sin que para ello existiera concierto prévio para ejecutar el movimiento atraídos sin duda alguna por el noble ejemplo de aquellos

Por lo que toca á la provincia de Cavite si bien se circularon órdenes de llamamiento por escrito firmadas por D Agustin Rieta D Cándido Tirona y por mí Tenientes de las tropas revolucionarias sin embargo no había seguridad de que fueran atendidas ni recibidas siquiera como en efecto una de estas órdenes cayó en manos del español D Fernando Parga Gobernador Político Militar de la provincia que dió cuenta al Capitán General Don Ramón Blanco y Erenas quién ordenó á seguida combatir y atacar á los revolucionarios

La Providencia que había señalado sin duda la hora de la emancipación filipina protegió á los revolucionarios pues solo así se explica que hombres armados de palos y gulok sin disciplina ni organización vencieran á fuerzas españolas de Ejército regular en los rudos combates de Bakoor Imus y Noveleta hasta el extremo de arrebatarles numerosos fusiles lo que obligó al General Blanco á suspender las operaciones y tratar de sofocar la revolución por la política de atracción pretextando que no le gustaba «hacer carnicería en los filipinos»

El Gobierno de Madrid no aprobando esta clase de política del General Blanco envió al Teniente General don Camilo Polavieja para relevarle del cargo mandando al propio tiempo tropas regulares de españoles peninsulares

Polavieja con 16 mil hombres armados de Maüser y una batería de cañones atacó á los revolucionarios con energía apenas reconquistó la mitad de la provincia de Cavite y habiéndose enfermado dimitió el cargo en Abril de 1897

Relevado D Camilo Polavieja por el Capitán General D Fernando Primo de Rivera éste anciano guerrero persiguió en persona á los revolucionarios con tanta firmeza como humanidad logrando reconquistar toda la provincia de Cavite y arrojando á los rebeldes á las montañas

Entónces senté mis reales en la abrupta y desconocida sierra de Biak-na-bató donde establecí el Gobierno Republicano de Filipinas á fines de Mayo de 1897
"""

palabras = sorted(texto.lower().split())
palabras_unicas = set(palabras)
print("Palabras en total:", len(palabras))
print("Palabras unicas:", len(palabras_unicas))

palabras_usadas = {}
for palabra in palabras:
    # if palabra in palabras_usadas:
    #     # La palabra ya existe, necesito actualizar el valor
    #     palabras_usadas[palabra] += 1
    # else:
    #     palabras_usadas[palabra] = 1
    palabras_usadas[palabra] = palabras_usadas.get(palabra, 0) + 1


# with open("salida.csv", "w") as file:
#     file.write("palabra,conteo\n")
#     for k, v in palabras_usadas.items():
#         file.write(f"{k},{v}\n")

palabras_grandes = {
    palabra: apariciones
    for palabra, apariciones in palabras_usadas.items()
    if len(palabra) >= 15
}

max_val = max(palabras_grandes.values())
max_pos = list(palabras_grandes.values()).index(max_val)
claves = list(palabras_grandes.keys())
print(claves[max_pos])
