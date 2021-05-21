# suponga que se tiene un precio de articulo
# descuento
# impuesto

# crear una funcion que me calcule el precio final de un articulo

def total(precio, descuento, impuesto, **kwargs):
    precio_parcial = precio * (1 + impuesto/100)
    return precio_parcial * (1 - descuento/100)

#camisa = total(precio=10000, descuento=5, impuesto=13)

juancito = {
    'precio': 5000,
    'descuento': 10,
    'impuesto': 13,
    'detalle': 'nuevo',
    'telefono': 7471231
}

#total(precio=juancito['precio'], descuento=juancito['descuento'], impuesto=juancito['impuesto'])

compra_juancito = total(**juancito)
print(compra_juancito)
