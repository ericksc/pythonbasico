# crear una tupla
a = ('azul', 'amarillo', 'rojo', None, 1, True)

b = (3, 4, 1, 'a', 'b', 'c')
sorted(b, key=lambda x : str(x))
pass

# concatenar tuplas
(6,5,4,3) + (9,6,1)

# any, all

# any
#para detectar al menos uno True
any((False, False, False, False))

#all
#para detectar todas True
all((c[0] == 0 , c[-1]> 100, c[0] > c[-1]))

# ejercicio usando tuplas
# se tienen los siguientes precios de productos
# 900, 400, 200, 100, 500

# detectar si las condiciones fueron validas
# el precio del ultima compra es mayor que la segunda y que la suma de las compras fueron mayores que 2000

# si el precio de la primera compra es menor a 500 o que la segunda compra es mayor que la primera
