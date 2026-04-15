import random

class Juego:
    def __init__(self, vidas):
        self.vidasIniciales = vidas
        self.numeroDeVidas = vidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
        print("Partida reiniciada. Vidas:", self.numeroDeVidas)

    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, num):
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un numero entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un numero: "))
            except:
                print("Numero invalido")
                continue

            if not self.validaNumero(num):
                print("Numero fuera de rango (0-10)")
                continue

            if num == self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    print("Te quedaste sin vidas")
                    print("El numero era:", self.numeroAAdivinar)
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            print("Error: numero fuera de rango (0-10)")
            return False
        if num % 2 != 0:
            print("Error: debe ser un numero PAR")
            return False
        return True
    
    def juega2(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([0,2,4,6,8,10])

        print("Adivina un numero PAR entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un numero: "))
            except:
                print("Numero invalido")
                continue

            if not self.validaNumero(num):
                print("Numero fuera de rango (0-10)")
                continue

            if num == self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    print("Te quedaste sin vidas")
                    print("El numero era:", self.numeroAAdivinar)
                    break

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num):
        if not (0 <= num <= 10):
            print("Error: numero fuera de rango (0-10)")
            return False
        if num % 2 == 0:
            print("Error: debe ser un numero IMPAR")
            return False
        return True

    def juega3(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([1,3,5,7,9])

        print("Adivina un numero entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un numero: "))
            except:
                print("Numero invalido")
                continue

            if not self.validaNumero(num):
                print("Numero fuera de rango (0-10)")
                continue

            if num == self.numeroAAdivinar:
                print("Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    print("Te quedaste sin vidas")
                    print("El numero era:", self.numeroAAdivinar)
                    break

class Aplicacion:
    @staticmethod
    def main():
        print("\n=== JUEGO NORMAL ===")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()

        print("\n=== JUEGO PAR ===")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega2()

        print("\n=== JUEGO IMPAR ===")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega3()


if __name__ == "__main__":
    Aplicacion.main()