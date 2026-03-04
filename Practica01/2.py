# LaPaz 04/03/26
# Andy Casilla


class EcuacionLineal:

    def __init__(self, a, b, c, d, e, f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def tiene_solucion(self):
        return (self._a * self._d - self._b * self._c) != 0

    def get_x(self):
        return (self._e * self._d - self._b * self._f) / (self._a * self._d - self._b * self._c)

    def get_y(self):
        return (self._a * self._f - self._e * self._c) / (self._a * self._d - self._b * self._c)


#Prueba
a, b, c, d, e, f = map(float, input(
    "Ingrese a, b, c, d, e, f: ").split())

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tiene_solucion():
    print("x =", ecuacion.get_x(),
          ", y =", ecuacion.get_y())
else:
    print("La ecuacion no tiene solucion")