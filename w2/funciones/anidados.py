def saludar(nombre, apellido):
    def generar_nombre(nombre, apellido):
        return f"{nombre} {apellido}"

    print("Hola:", generar_nombre(nombre, apellido))


saludar("Jose", "Aguilar")
