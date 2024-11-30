VIDA_LIMITE = 1000


class Jugador:
    secuencia = 10

    def __init__(self, nombre, defensa, ataque):
        Jugador.secuencia += 1
        self.secuencia = Jugador.secuencia
        self.nombre = nombre
        self.tipo = "prueba"
        self.defensa = defensa
        self.ataque = ataque
        self.vida = VIDA_LIMITE

    def __str__(self):
        return f"{self.nombre} ({self.vida}) DEF: {self.defensa} ATK: {self.ataque}"

    def mostrar_vida(self):
        return self.vida

    def atacar(self, atacante):
        if atacante.ataque > self.defensa:
            self.nivel_vida -= atacante.ataque - self.defensa
        elif atacante.ataque < self.defensa:
            atacante.nivel_vida -= self.defensa - atacante.ataque

    @property
    def esta_vivo(self):
        return self.vida > 0

    @property
    def nivel_vida(self):
        if self.vida < 0:
            return 0

        return self.vida

    @nivel_vida.setter
    def nivel_vida(self, value):
        if value < 0:
            raise ValueError("No se puede modificar con valores negativos")

        if value > VIDA_LIMITE:
            raise ValueError(
                f"No se puede modificar con valores mayores a {VIDA_LIMITE}"
            )

        self.vida = value


player1 = Jugador("Arturo", 1500, 2000)
player2 = Jugador("Gustav", 1750, 1750)
player3 = Jugador(nombre="Ana", ataque=2000, defensa=1000)
print(player1)
print(player2)
print(player3)
print(player1.mostrar_vida())

print(player3.esta_vivo)

player1.atacar(player2)
assert player1.vida == 750
assert player2.vida == 1000

player2.atacar(player1)
assert player1.vida == 750
assert player2.vida == 750


player3.nivel_vida = 400
