edad = 50
tome_alcohol = False
restriccion = True
no_tengo_licencia = True

if tome_alcohol:
    print('No puedo manejar')

else:
    if (18 > edad) and not restriccion:
        print('Soy menor de edad no puedo manejar')
    elif (18 <= edad) and (edad < 90) and (not restriccion):
        print('Soy adulto y puedo manejar')
    elif (90 <= edad) and not restriccion:
        print('Soy de la tercera edad y no puedo manejar')
    elif no_tengo_licencia:
        print(':(')
    else:
        print('no puedo manejar!!!!')


