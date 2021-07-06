# diccionario

#creacion de diccionarios!!!
agenda = {
    'carlitos':7461252,
    'luis': 85215125,
    'andres': 43215231
}

# leer informacion
agenda['carlitos']


# como obtenga la coleccion de todas las llaves?
agenda.keys()

# como obtengo los numeros de telefonos de todos mis amigos
agenda.values()

# como obtengo todos los datos?
agenda.items()

# como actualizar los datos?
agenda['maria'] = 8327131

agenda.update( {'carlitos': 532535} ) # actualizar llaves presentes
agenda.update( {'juan': 321238} ) # agregar
pass

# compras al super!
# juancto va al super
# pan 400, queso 500, salsa 1000, jamon 700
# paso 1. crear un diccionario con las compras de juan. las llaves seran los nombres de los productos.
# valores seran el precio de cada producto

juan = {
    'pan': 400,
    'queso': 500,
    'salsa': 1000,
    'jamon': 700
}

# paso 2: el precio del queso tiene un 15% de descuento. actualizar el dato del precio del queso
descuento = 0.15
#juan.update({'queso': juan['queso'] * (1-descuento) })

#opcion 2
#juan['queso'] = juan['queso'] * (1-descuento)

#opcion 3

#juan['queso'] *= 1 - descuento


# paso 3. se acabo del jamon. juan no puede comprar jamon
# opcion 1
#del juan['jamon']

#opcion 2

info_jamon = juan.pop('jamon')

juan['jamon'] = info_jamon

pass