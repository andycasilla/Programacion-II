# LaPaz 04/03/26
# Andy Casilla

import time
import random

class Cronometro:

    def __init__(self):
        self.inicia = time.time() * 1000
        self.finaliza = 0

    def iniciar(self):
        self.inicia = time.time() * 1000

    def detener(self):
        self.finaliza = time.time() * 1000

    def lapsoDeTiempo(self):
        return self.finaliza - self.inicia


def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j

        temp = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temp


#Prueba
lista = []
for i in range(10000):
    lista.append(random.randint(1, 100000))

c = Cronometro()
c.iniciar()
ordenamiento_seleccion(lista)
c.detener()

print("Tiempo en milisegundos:", c.lapsoDeTiempo())