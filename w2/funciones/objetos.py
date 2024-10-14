def duplicar(a):
    return a * 2


# Asignar duplicar a un objeto
f = duplicar

print(f(3))


def aumentar(inicial, aumento):
    return inicial + aumento


def componer(f1, f2, entrada1, entrada2):
    return f1(f2(entrada1, entrada2))


resultado = componer(duplicar, aumentar, 40, 6)
print(resultado)
