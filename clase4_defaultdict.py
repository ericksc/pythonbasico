# defaultdict
from collections import defaultdict

colores = (
    ('juan', 'Yellow'),
    ('carlos', 'Blue'),
    ('andres', 'Green'),
    ('juan', 'Black'),
    ('juan', 'Purple'),
    ('andres', 'Red'),
    ('luis', 'Silver'),
    ('juan', 'Orange'),
)

colores_favoritos = defaultdict(list)

for nombre, color in colores:
    colores_favoritos[nombre].append(color)

print(colores_favoritos)

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

from collections import defaultdict
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
# Funciona!