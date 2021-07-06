
nombre = ['juan', 'carlos', 'luis', 'andres']

precio = [450, 600, 120, None]

datos = list(zip(nombre, precio))

mis_amigos, costos = list(zip(*datos))
pass