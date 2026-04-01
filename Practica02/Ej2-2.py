from Ej2 import AlgebraVectorial

v1 = AlgebraVectorial(1,2,3)
v2 = AlgebraVectorial(4,5,6)
print("Producto escalar =", v1.producto_escalar(v2))
print("Magnitud v1 =", v1.magnitud())
print("¿Perpendiculares?", v1.perpendicular(v2))
print("¿Paralelos?", v1.paralela(v2))
print("Proyección =", v1.proyeccion(v2))
print("Componente =", v1.componente(v2))