t = (10, 20, 30)
print(t[0])

#t[0] = 1000  # Es un TypeError

t2 = 10, 20, 30,
t3 = (10)  # Esto no tupla, es el entero 10
print(type(t3))
t4 = (10,)  # Si es tupla
print(type(t4))
t5 = 10,  # Si es tupla
print(type(t5))

# list -> tuple
ls = [10, 20, 30]
t6 = tuple(ls)

# tuple -> list
otra_ls = list(t6)

t7 = (10, 20, 30, [40])
t7[3].clear()
print(t7)