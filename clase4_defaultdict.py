# diccionario vacio
# mi_diccionario = {}
# mi_diccionario['palabra'].upper()

# defaultdict
from collections import defaultdict
#
# colores = (
#     ('juan', 'Yellow'),  # primera
#     ('carlos', 'Blue'),  # segunda
#     ('andres', 'Green'),  # tercera
#     ('juan', 'Black'),
#     ('juan', 'Purple'),
#     ('andres', 'Red'),
#     ('luis', 'Silver'),
#     ('juan', 'Orange'),
# )
#
# colores_favoritos = defaultdict(list)
#
# for nombre, color in colores:
#     colores_favoritos[nombre].append(color)
#
# print(colores_favoritos)

# ejercicio
# juan      heredia, saprissa, liga, cartago
# carlos    heredia,  liga,  cartago
# andres    saprissa, liga, limon
# luis      saprissa, limon, cartago
# paso 1 crear un diccionario donde las llaves son los nombres de los amigos y los valores las preferencias de los equipos
# paso 2. resumen: cuantos aficionados hay por equipo

amigos = [
    ('juan' , ('heredia', 'saprissa', 'liga', 'cartago')),
    ('carlos'   , ('heredia',  'liga',  'cartago')),
    ('andres'   , ('saprissa', 'liga', 'limon')),
    ('luis'     , ('saprissa', 'limon', 'cartago')),
]

equipos_favoritos = defaultdict(list)

for nombre, equipos in amigos:
    equipos_favoritos[nombre].extend(equipos)

print(equipos_favoritos)


lista_equipos = list(equipos_favoritos.values())

lista_final_equipos = []

for equipos_de_un_amigo in lista_equipos:
    lista_final_equipos.extend(equipos_de_un_amigo)

cuenta_equipos = {}
for equipo in lista_final_equipos:
    if equipo in cuenta_equipos:
        cuenta_equipos[equipo] += 1
    else:
        cuenta_equipos[equipo] = 1

from collections import Counter
print(lista_final_equipos)
print(cuenta_equipos)
print(Counter(lista_final_equipos))
# output
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })

# some_dict = {}
# some_dict['colours']['favourite'] = "yellow"
# # Raises KeyError: 'colours'

# from collections import defaultdict
# tree = lambda: defaultdict(tree)
# some_dict = tree()
# some_dict['colours']['favourite'] = "yellow"
# # Funciona!
# pass