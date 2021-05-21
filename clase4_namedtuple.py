# Como crear un punto(x , y)

from collections import namedtuple

punto = namedtuple('Punto', ['x', 'y'])

mi_punto = punto(1, 2)  #(1, 2)

print(f'Mi punto esta ubicado en {mi_punto.x} , {mi_punto.y}')

