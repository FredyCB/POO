def f_por_referencia(ls: list):
    ls[0] = "Modifica"


def f_por_copia(ls: list):
    lsc = ls.copy()
    lsc[0] = "Modificado"


a = [10, 20, 30]
f_por_copia(a)
print("Paso por copia: ", a)
f_por_referencia(a)
print("Paso por referencia:", a)


