# valores por default a los parametros

casa = 'patito'

def total(precio, descuento=10, impuesto=13, *args, **kwargs):
    precio_parcial = precio * (1 + impuesto/100)
    return precio_parcial * (1 - descuento/100)

mis_parametros = (1,2,3,4,5,6,7)
parametros_keyword = {'a':1, 'b':2, 'c':3}

#resultado = total(1000, 10, 13, 100, 200, 400, 600, 700, casa, telefono = 8949782, detalle='datos', direccion='san jose')

resultado = total(*mis_parametros, **parametros_keyword)