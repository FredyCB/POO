"""
Bucles
    - while
    - for

Objetivo: escribir numeros pares del 0 al 100

Java:
    for (int i = 0; i <= 100; i += 2) {
        System.out.println(i);
    }

    int j = 0;
    while (j <= 100) {
        System.out.println(j);
        j += 2;
    }
"""

for i in range(0, 101, 2):
    print(i)

j = 0
while j <= 100:
    print(j)
    j += 2
