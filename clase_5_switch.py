

# diccionario de funciones!
# switch

# la calculadora
# suma
# resta
# multiplica
# divide

def sumar(x, y):
    return x+y

def restar(x,y):
    return x-y

def multiplicar(x, y):
    return x * y

def dividir(x,y):
    return x / y

def mi_default(x, y):
    return f'Operacion no valida'

x = 10
y = 5
operacion = 'suma'


calculadora = {
    'suma': sumar,
    'resta': restar,
    'multiplica': multiplicar,
    'dividir': dividir
}

calculadora.get(operacion, mi_default)(x,y)
pass