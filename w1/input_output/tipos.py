a = False  # a es bool
print(type(a))
a = 10  # a es int (64 bits)
print(type(a))
a = 2.34  # a es un float (64 bits)
print(type(a))
a = "hola mundo"  # a es una str (string)
print(type(a))


a = 2.3
b = int(a)  # quiero que b sea int
print(b)

# conversiones de un bool
print(-1, bool(-1))
print(0, bool(0))
print(1, bool(1))
print("", bool(""))
print("hola", bool("hola"))
print("False", bool("False"))

print(23, str(23))
print(True, str(True))

s1 = "'hola'"
s2 = '"hola"'
print(s1, s2)
