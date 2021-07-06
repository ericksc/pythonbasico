def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parametrized
def multiply(f, n):
    def aux(*xs, **kws):
        return n * f(*xs, **kws)
    return aux

@multiply(2)
def function(a):
    return 10 + a

print(function(3))    # Prints 26

@multiply(3)
def function_again(a):
    return 10 + a

print(function(3))          # Keeps printing 26
print(function_again(3))   # Prints 39, namely 3 * (10 + 3)

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