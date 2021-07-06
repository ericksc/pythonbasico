# primer decorador

# decorador
def a_new_decorator(f):

    def wrapTheFunction():
        print("Antes!")
        f()
        print("Despues!")

    return wrapTheFunction

# decorado
@a_new_decorator
def mi_funcion():
    print("logica principal")

@a_new_decorator
def otra_funcion():
    print('otra logica principal')

# ejecucion de la funcion decorada

print('1')
mi_funcion()
print('2')
otra_funcion()
