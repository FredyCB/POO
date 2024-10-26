ls = [10, 20, 30, 40, 50, 60, 70]

# Remover por posicion
print(ls.pop())  # remueve el ultimo
print(ls)

print(ls.pop(1))  # remueve la posicion 1
print(ls)

del ls[2]  # Remover la segunda posicion
print(ls)

# Remover por valor
ls.remove(50)  # Remueve el valor 50
print(ls)

ls.clear()  # Limpia la lista
print(ls)