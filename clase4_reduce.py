from functools import reduce

a = [1,2,3,4]

def multiplicar(x,y):
    z = x * y
    

resultado = reduce(multiplicar, a)
print(resultado)