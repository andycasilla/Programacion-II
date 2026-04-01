# Ejercicio 3
# Clase Vector3D
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return Vector3D(
        self.x + v.x,
        self.y + v.y,
        self.z + v.z
    )
    
    def escalar(self, r):
        return Vector3D(
        r*self.x,
        r*self.y,
        r*self.z
    )
    
    def longitud(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def normal(self):
        m = self.longitud()
        return Vector3D(
        self.x/m,
        self.y/m,
        self.z/m
    )
    
    def producto_escalar(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z
    
    def producto_vectorial(self, v):
        i = self.y*v.z - self.z*v.y
        j = self.z*v.x - self.x*v.z
        k = self.x*v.y - self.y*v.x
        return Vector3D(i, j, k)
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"