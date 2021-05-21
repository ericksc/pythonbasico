# necesito crear una funcion que me calcule la suma de precios de articulos.
# No se sabe cuantos articulos

def suma_articulos(*precios):
    # total = 0
    # for precio in precios:
    #     total += precio

    return sum(precios)

print(suma_articulos())

print(suma_articulos(1000))

print(suma_articulos(2000, 3000))

print(suma_articulos(8000, 9000, 10000))

print(suma_articulos(1,2,3,4,5,6,7,8,9))


suma_articulos(suma_articulos(), suma_articulos(1000))