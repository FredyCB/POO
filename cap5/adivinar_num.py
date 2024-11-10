from random import randint

MAXIMO_INTENTOS = 7


def adivinar():
    # generar la incognito
    incognita = randint(1, 100)  # Es el numero secreto
    # print("Este es el secreto:", incognita)
    intentos = 0  # Registra la cantidad de intentos
    ganador = False  # Indica si hay un ganador

    while intentos < MAXIMO_INTENTOS:
        intentos += 1
        # jugar
        candidato = int(input(f"Este es el intento {intentos}, digite un numero:"))

        if candidato == incognita:
            ganador = True
            break
        elif candidato < incognita:
            print("Debe probar con un numero MAYOR!!")
        else:
            print("Debe probar con un numero MENOR!!")

    # resultado final
    if ganador:
        print("Has acertado")
    else:
        print("Has perdido, suerte a la proxima")


adivinar()
