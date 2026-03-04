# LaPaz 04/03/26
# Andy Casilla

import math

#MODULAR

def promedio(datos):
    return sum(datos) / len(datos)

def desviacion(datos):
    prom = promedio(datos)
    suma = sum((x - prom)**2 for x in datos)
    return math.sqrt(suma / (len(datos) - 1))


#POO
class Estadistica:

    def __init__(self, datos):
        self._datos = datos

    def promedio(self):
        return sum(self._datos) / len(self._datos)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom)**2 for x in self._datos)
        return math.sqrt(suma / (len(self._datos) - 1))

#Prueba
datos = list(map(float, input().split()))

print("\n--- VERSION MODULAR ---")
print("Promedio: {:.2f}".format(promedio(datos)))
print("Desviacion: {:.5f}".format(desviacion(datos)))

print("\n--- VERSION POO ---")
est = Estadistica(datos)
print("Promedio: {:.2f}".format(est.promedio()))
print("Desviacion: {:.5f}".format(est.desviacion()))