# Como crear un punto(x , y)

from collections import namedtuple

punto = namedtuple('Punto', ['x', 'y'])

mi_punto = punto(1, 2)  #(1, 2)

otro_punto = punto(x=10, y=20)

print(f'Mi punto esta ubicado en {mi_punto.x} , {mi_punto.y}')


import math
distancia = math.sqrt((mi_punto.x - otro_punto.x) ** 2 + (mi_punto.y - otro_punto.y) ** 2)
print(distancia)

mis_puntos = [mi_punto, otro_punto]

#iteracion -> for loop -> bucles
x = 0
y = 0
for punto in mis_puntos:
    x = abs(punto.x - x)
    y = abs(punto.y - y)

distancia = math.sqrt(x**2 + y**2)
print(distancia)