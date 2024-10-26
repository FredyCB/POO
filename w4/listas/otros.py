ls = [10, 20, 30, 40, 50, 60, 70, 5, 10]

print("Apariciones del 10 en la lista:", ls.count(10))
par = [2, 4, 6, 8]
impar = [1, 3, 5, 7]

# Concatenar (crear un nuevo objeto)
print("Concatenacion:", par + impar)
print("Par:", par)
print("Impar:", impar)

# # Append
# par.append(impar)
# print("Par:", par)

# Extender
par.extend(impar)
print("Par:", par)
print("Impar:", impar)

#par.append("Hola")
ls_ordenada = sorted(par)

print(ls_ordenada)

b = [10, 20, 30]
print(b[-1])

print("Hola"[-1])
