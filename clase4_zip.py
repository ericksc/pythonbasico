# nombres = ['carlos', 'luis', 'andres', 'maria']
#
# frutas = ['coco', 'limon', 'melon']
#
# resultado = list(zip(nombres[1:], frutas))

personas = [
    ('juan', 321321),
    ('jose', 654211),
    ('pepe', 732131),
]

# el unzip
print(personas)
client, telefono = zip(*personas)
print(client)
print(telefono)


mi_dict = {'a':1, 'b':2}
las_llaves = mi_dict.keys()
los_valores = mi_dict.values()