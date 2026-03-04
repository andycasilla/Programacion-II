# LaPaz 04/03/26
# Andy Casilla


import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def get_discriminante(self):
        return self._b**2 - 4 * self._a * self._c

    def get_raiz1(self):
        if self.get_discriminante() >= 0:
            return (-self._b + math.sqrt(self.get_discriminante())) / (2 * self._a)
        else:
            return 0

    def get_raiz2(self):
        if self.get_discriminante() >= 0:
            return (-self._b - math.sqrt(self.get_discriminante())) / (2 * self._a)
        else:
            return 0


#Prueba
a, b, c = map(float, input(
    "Ingrese a, b, c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)

d = ecuacion.get_discriminante()

if d > 0:
    print("La ecuacion tiene dos raices {:.6f} y {:.5f}".format(ecuacion.get_raiz1(), ecuacion.get_raiz2()))
elif d == 0:
    print("La ecuacion tiene una raiz", ecuacion.get_raiz1())
else:
    print("La ecuacion no tiene raices reales")