# Test ejercicio 1
from Ej1 import MiPunto

p1 = MiPunto()
p2 = MiPunto(10,30.5)
print("Punto 1:", p1.getX(), p1.getY())
print("Punto 2:", p2.getX(), p2.getY())
print("Distancia =", p1.distancia(p2))