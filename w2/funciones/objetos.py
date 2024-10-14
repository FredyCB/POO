# Es posible que las funciones se comporten como objetos, es decir,
# que puedan ser asignadas a variables.
def saludar(persona):
    print("Hola", persona)


f = saludar
f("Jose")


# En Python, las funciones son objetos de primera clase, lo que significa
# que pueden ser asignadas a variables, pasadas como argumentos a otras
# funciones y devueltas como valores de otras funciones.
# Ejemplo de funcion como argumento
def sumar(a, b):
    return a + b


def duplicar(numero):
    return numero * 2


# Funcion que permite usar dos funciones como argumentos
def componer(f, g, arg1, arg2):
    return f(g(arg1, arg2))


print(componer(duplicar, sumar, 10, 20))
# Salida: 60
