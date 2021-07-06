#Dada las listas
lista_num = [10,30,21,40,61,50,81,70,101,90]
lista_alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# pregunta 1
# Escribir el codigo que ordene de mayor a menor
# la lista_num

lista_num.sort(reverse=True)
print(f'La lista de mayor a menor {lista_num}')

# pregunta 2
# Escribir el codigo que muestre la suma de los valores intercalados de la lista
# lista_num

lista_num = [10,30,21,40,61,50,81,70,101,90]
# tomando como criterio: intercalado como solo los pares
valores_intercalados = lista_num[::2]

# suma de los valores intercalados
suma = sum(valores_intercalados)
print(f'La suma de los valores intercalados {suma}')

# Ejercicio 3
# Escribir el codigo que muestre las letras que
# ocupa las posiciones impares en la lista
# lista_alfabeto

solo_impares = lista_alfabeto[1::2]
print(f'Solo impares {solo_impares}')

# Ejercicio 4
# Escribir el codigo que sume el maximo y el minimo de la lista_num
suma = max(lista_num) + min(lista_num)
print(f'La suma es {suma}')

# Ejercicio 5
#Escribir el codigo que agregue la ñ.
# Pero almacenando el resultado en la lista_alfabeto_ext

lista_alfabeto_ext = lista_alfabeto.copy()
posicion_n = lista_alfabeto_ext.index('n')
lista_alfabeto_ext.insert(posicion_n + 1, 'ñ' )
print(lista_alfabeto_ext)

# Ejercicio 6.
# Escribir el codigo  que cree una lista
# multidimensional basado en las 2 listas: lista_alfabeto y lista_num

# Tomando como criterio multidimensional como una estructura de 2 o mas dimensiones
lista_multidimensional = []
lista_multidimensional.append(lista_alfabeto)
lista_multidimensional.append(lista_num)

print(lista_multidimensional)

# Ejercicio 8

prueba_dic = {'Mango':800, 'Papaya':600, 'Sandia':550, 'Anona':750}

fruta_ingresada = input (" Favor ingrese el nombre de una estas 4 frutas : \ nMango \ nPapaya \ nSandia \ nAnona \
nFavor ingresar nombre : ")
kg_requeridos = float ( input (" Ingrese la cantidad de kilogramos deseados de la fruta : "))

precio_final = kg_requeridos * prueba_dic[fruta_ingresada]

print ("El precio final es:", precio_final )
