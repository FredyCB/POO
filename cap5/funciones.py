# func. esteril (no return: None)
def saludar(persona):
    print("Hola", persona)


# func. fructifera (return)
def duplicar(numero):
    return numero * 2


# estrategia para doc funciones (no hay validacion)
def sumar(a: int, b: int) -> int:
    return a + b


x = saludar("Jose")
print(x)

y = duplicar(20)
print(y)

z = duplicar("12")
print(z)

s = sumar("1", "2")
print(s)
