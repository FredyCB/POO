
class Persona:
    secuencia = 10  # Pertenece a la clase

    def __init__(self, nombre, apellido, identidad):
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        Persona.secuencia += 1
        self.secuencia = Persona.secuencia  # Pertenece al objeto (self)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.secuencia}"


if __name__ == '__main__':
    # Crear objetos
    persona0 = Persona("", "", 0)

    persona1 = Persona("Jose", "Avila", 23454)

    print("Generado en persona.py:", persona1)

    print(persona1.__dict__)
