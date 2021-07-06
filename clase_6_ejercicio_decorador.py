def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parametrized
def descuento_iva(f, descuento, iva):
    def aux(*xs, **kws):
        neto = f(*xs, **kws) # va juanito en otro momento carlos
        # accion despues de ejecutar la funcion f
        con_descuento = neto * (1 - descuento/100)
        con_impuesto = con_descuento * (1 + iva/100)
        return con_impuesto
    return aux


@descuento_iva(descuento=10, iva=1)
def juanito(*args, **kwargs):
    return sum(args)

@descuento_iva(descuento=20, iva=1)
def carlos(*args, **kwargs):
    return sum(args)

@descuento_iva(descuento=5, iva=1)
def sue(*args, **kwargs):
    return sum(args)

print(juanito(300, 200))
print(carlos(300, 200))
print(sue(1000))


# Ejercicio 1:

# 1- Crear una funcion que salude. ejemplo: Buenos dias
# decorar la funcion anterior para que diga la despedida. ejemplo: hasta luego
# poner en funcionamiento
# 10 mins

# Ejercicio 2
# Suponga que Juanito va de compras
# compro. naranja -> 100, melon-> 200
# en la caja se le hacen descuestos y tambien le calcula el IVA
# para tener un precio final
naranaja = 100
melon = 200
# 1 - crear funcion que tome los precios de los productos por comprar
# 2- Crear decorador que calcule el descuento y el IVA parametrizado
# 3- obtenga el precio final si el descuento es del 10% y el IVA 1%