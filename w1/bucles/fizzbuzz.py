"""
Escriba numeros del 1 al 100 donde sigan los siguientes criterios:
    - Fizz: si el numero es divisible por 3
    - Buzz: si el numero es divisible por 5
    - Fizzbuzz: si el numero es divisible por 3 y por 5
    - Escriba el numero si no es divisible ni por 3 ni por 5

Ejemplo:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizzbuzz

"""

for numero in range(1, 101):
    if numero % 15 == 0:
        print("Fizzbuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
