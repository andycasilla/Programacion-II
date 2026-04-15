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
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        return self.numeroDeVidas > 0
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()

        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un numero entre 0 y 10")

        while True:
            try:
                num = int(input("Ingresa un número: "))
            except:
                print("Error: ingresa un número valido")
                continue

            if num == self.numeroAAdivinar:
                print("Felicidades, Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")
                else:
                    print("Suerte la proxima vez, PERDISTE")
                    print("El numero era:", self.numeroAAdivinar)
                    break

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()