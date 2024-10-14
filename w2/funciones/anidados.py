# Ejemplo de funciones anidadas
def operacion(a, b):
    def suma():
        return a + b

    def resta():
        return a - b

    def multiplicacion():
        return a * b

    def division():
        return a / b

    return suma(), resta(), multiplicacion(), division()


# Ejecutar la función
print(operacion(10, 5))
# (15, 5, 50, 2.0)
