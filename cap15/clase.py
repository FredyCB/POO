class Cosa:
    pass


cosa = Cosa()
cosa.valor = 10
print(cosa.__dict__)

otra_cosa = Cosa()
print(otra_cosa.__dict__)
