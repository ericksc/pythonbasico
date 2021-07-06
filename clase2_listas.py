# crear listas
#          0          1       2
frutas = ['naranja', 'pera', 'uvas']


# acceder a los elementos
frutas[0]


# slicing
frutas[0:2]
#      limite izquierdo   limite derecho    step
frutas[                 :                 :      ]


# crear una lista de 10 articulos personas
#             0         1         2          3            4
articulos = ['zapatos', 'reloj', 'cartera', 'billetera', 'camisa',
#             5           6          7        8            9
             'laptop',  'pantalon', 'lapiz', 'cuaderno', 'medias']

# cuales son los articulos de indice impar?
articulos[1::2]
# cual es el ultimo articulo?
articulos[-1]
# cuales son los articulos que no sean ni el primero ni el ultimo?
pass


#como se pueden agregar elementos a la lista
# append

articulos.append('pantalla')

# extend

articulos.extend(['lampara', 'foco'])
# insert

articulos.insert(2, 'tennis')

# index
articulos.index('lapiz')

# sort()
articulos.sort()

a= [1, 53, 87, 99, 8, 10, 42, 52, 78]
a.sort(key=lambda x: (x % 2) == 0 )
# lambda es para crear una funcion anonima (sin nombre).
# definiendo el parametro 'patito'

#max
max(articulos, key=lambda x : x[3]  )

#min
min(articulos, key=lambda x : x[3]  )

b = ['auv', 'axy', 'erc', 'zwr']

# sum

c = [3,4,1,6,2]
sum(c)