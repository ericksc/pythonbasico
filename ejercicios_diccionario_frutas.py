# ##################################################
# ################## Tarea 3 ejercicio 8 ###########
prueba_dic = {'Mango':800, 'Papaya':600, 'Sandia':550, 'Anona':750}

fruta_ingresada = input (" Favor ingrese el nombre de una estas 4 frutas : \ nMango \ nPapaya \ nSandia \ nAnona \
nFavor ingresar nombre : ")
kg_requeridos = float ( input (" Ingrese la cantidad de kilogramos deseados de la fruta : "))

precio_final = kg_requeridos * prueba_dic[fruta_ingresada]

print ("El precio final es:", precio_final )
