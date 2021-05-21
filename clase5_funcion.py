# mi primera funcion

# base = 20
# altura = 5
#
# area_rectangulo = base * altura

def mi_area_rectangulo(base, altura):
    return base * altura

base = 10
altura = 5

mi_area = mi_area_rectangulo(base, altura)

print(mi_area)

# otro rectangulo, base = 20 , altura = 10
otra_area = mi_area_rectangulo(10, 20)

otra_base = 500

area_nuevo_rectangulo = mi_area_rectangulo(altura=10, base=otra_base)


# ejercicio
# suponga que Juan va a comprar. zapato -> 2000, descuento -> 10% . camisa -> 5000 . descuento ->20%
# crear una funcion que calcule el precio a pagar por Juan

