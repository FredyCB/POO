texto = "Ingredientes: 1 y 1/2 tazas de harina, 1 taza de azúcar, 3/4 taza de cacao en polvo, 1 y 1/2 cucharadita de bicarbonato de sodio, 1/2 cucharadita de sal, 2 huevos, 1 taza de leche, 1/2 taza de aceite vegetal, 2 cucharaditas de extracto de vainilla, 1 taza de agua caliente" 
# Busqueda
palabra = input("Buscar palabra: ")
posicion = texto.find(palabra)
if posicion == -1:    print("Palabra no encontrada")
else:    print("Palabra encontrada en la posicion:", posicion)# 
#Extraccion 
inicio = int(input("Elemento inicial: "))
final = int(input("Elemento final: "))
print("Subcadena v1:", texto[inicio : final + 1])
# Analisis
texto_limpio = texto.replace(",", "").replace(":", "")
palabras = texto_limpio.split(" ")
print("Cantidad de palabras:", len(palabras))
for p in palabras:    
    if len(p) > 5:        
      print(p) 