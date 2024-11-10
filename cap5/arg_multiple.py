def sumar(*valores):
    return sum(valores)


def saludar(tratamiento, persona="Desconocido", extra="Hola"):
    print(tratamiento, persona)
    print(extra)
    print("-"*10)


saludar(extra="Bienvenidos a la clase", tratamiento="", persona="Alumnos de is-410")
