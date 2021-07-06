andres = ['andres', 100]
carlos = ['carlos', 150]
luis = ['luis', 50]

compras = [andres, carlos, luis]

# usando filter, cual es el amigo que gasto mas de 100

# def mi_funcion(x):
#     return x

resultado = list(filter(lambda x: x[-1]> 100, compras))
print([nombre for nombre, _ in resultado])
