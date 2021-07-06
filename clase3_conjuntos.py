# ejemplos con conjuntos

carlitos = {'manzana', 'uva', 'pera'}

andres = {'mora', 'uva', 'coco'}

# cual fruta tienen en comun
# interseccion!

carlitos.intersection(andres)

carlitos & andres

# cuales son las frutas que tenemos si carlitos
# y andres las comparten
carlitos | andres

# cuales frutas tiene carlitos o andres pero no ambos
carlitos ^ andres

# cuales son las frutas de carlitos
# que no estan en comun con andres
carlitos - andres


# cuales son las frutas de andres que no
# tiene carlos
andres - carlitos

# pertenencia
# si andres le gusta el coco
'coco' in andres

# duplicados
# luis fue al supermercado y compro lo siguiente
#luis -> pera, limon, cas, tomate, pera, limon, naranja
#limon, tomate, cas
# luis, cuales frutas compraste?

# crear un conjunto
lista_fruta = ['pera', 'limon', 'cas', 'tomate',
               'pera', 'limon', 'naranja',
               'limon', 'tomate', 'cas']

las_frutas = set(lista_fruta)

{'cereza', 'durazno', 'kiwi', 'caimito'}

pass


# ejercicio

a = set('abracadabra')
b = set('alacazam')

#1 cuales letras tienen un comun?
# intersection
print('pregunta1', a, b, a & b)
a & b
#2. cuales letras tiene 'abracadabra' que no tiene 'alacazam'

# diferencia
a-b
print('pregunta2', a, b, a - b)
#3 cuales son las letras que tiene 'abracadabra' o 'alacazam'
# union
a | b
print('pregunta3',a, b, a | b)

{1,2,3,4,5,6,7}
{321,643,987,12,654,723}
pass