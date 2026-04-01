# Ejercicio 1
# Andy Casilla
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distancia(self, o):
        dx = self.__x - o.__x
        dy = self.__y - o.__y
        return (dx**2 + dy**2) ** 0.5
    
    def distanciaXY(self, x, y):
        dx = self.__x - x
        dy = self.__y - y
        return (dx**2 + dy**2) ** 0.5