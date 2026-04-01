# Ejercicio 2
# Clase AlgebraVectorial
class AlgebraVectorial:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def producto_escalar(self, v):
        return self.a1*v.a1 + self.a2*v.a2 + self.a3*v.a3
    def magnitud(self):
        return (self.a1**2 + self.a2**2 + self.a3**2) ** 0.5
    def perpendicular(self, v):
        return self.producto_escalar(v) == 0
    def paralela(self, v):
        r1 = self.a1 / v.a1
        r2 = self.a2 / v.a2
        r3 = self.a3 / v.a3
        return r1 == r2 and r2 == r3
    def proyeccion(self, v):
        return self.producto_escalar(v) / (v.magnitud()**2)
    def componente(self, v):
        return self.producto_escalar(v) / v.magnitud()