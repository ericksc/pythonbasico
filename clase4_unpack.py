# p = 4, 5
#
# x = p[0]  # :(
# y = p[1]  # :(
#
# x, y = p    # :D :)
#
# data = ['data', 50 , 91.1 ,  (2011,11,21) ]

juanito = ['juan', 'perez', 30, 7371881, 'juan@juan.com', (1991,10,30)]

print(juanito)
#*_ , email = juanito
_, apellido, *_, (anno, *_) = juanito

print(apellido)
print(anno)
pass
