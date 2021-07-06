
mis_datos = ['carlos', 'andres', 'luis']

# en python3
# objecto map que se puede iterar

# en Python2 -> el resultado del map es una lista

#list(map(len, mis_datos)) es redundante
for valor in map(len, mis_datos):
    print(valor)
pass

# map(len, mis_datos)
[len(dato) for dato in mis_datos]

