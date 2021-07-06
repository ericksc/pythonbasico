from collections import Counter

colores = ['blanco', 'azul', 'blanco']
sabores = ['amargo', 'dulce', 'salado', 'amargo']
textura = ['suave', 'duro', 'suave']

cosas = [
    colores, sabores, textura
]


# list comprehesion
[elemento for elemento in cosas]

sumario = Counter(colores)

print(sumario)