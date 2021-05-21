#formulas de areas de figuras geometricas

#triangulo
print("Calcule el Area de un Triangulo")
baseT = int(input("ingrese la base = "))
altura = int(input("ingrese la altura = "))
areaTriangulo = float((baseT * altura) / 2)

print("el area del triangulo es = " + str(areaTriangulo))

#circulo
print("\n\nCalcule el Area de un circulo")
PI = 3.1421
radio = int(input("ingrese el radio = "))
areaCirculo = (PI * (radio ** 2))

print("el area del circulo es = " + str(areaCirculo))

#cuadrado
print("\n\nCalcule el Area del Cuadrado")
lado = int(input("ingrese el lado = "))
areaCuadrado = lado ** 2

print("el area del cuadrado es = " + str(areaCuadrado))