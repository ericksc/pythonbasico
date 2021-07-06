
def en_mayuscula(palabra):
    return palabra.upper()

def en_minuscula(palabra):
    return palabra.lower()

def la_longitud(palabra):
    return len(palabra)

def capitalizando(palabra):
    return palabra.capitalize()

mis_funciones = [en_mayuscula, en_minuscula, la_longitud, capitalizando]

mis_palabras = ['BueNOs Dias', 'bUenas nOches']

for palabra in mis_palabras:
    valor = list(map(lambda x: x(palabra), mis_funciones))
    print(valor)

# vamos a probar la funcion 'en_mayuscula'
resultado = en_mayuscula('hola')
resultado = en_minuscula('hola')

