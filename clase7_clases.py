# creacion de personas!

class Persona:
    def __str__(self):
        return f'Mi nombre es {self.mi_nombre} y mi cedula es {self.mi_cedula}'

    def __repr__(self):
        return f'Mi nombre es {self.mi_nombre} y mi cedula es {self.mi_cedula}'

    def __init__(self, nombre, cedula):
        # atributo mi_nombre
        self.mi_nombre = nombre
        # atributo mi_cedula
        self.mi_cedula = cedula
        # atributo de mascarilla
        self.mascarilla_colocada = False

    def ponerse_mascarilla(self, color='celeste'):
        print(f'{self.mi_nombre} saca la mascarilla de color {color} de la bolsa')
        print(f'{self.mi_nombre} pongase la mascarilla')
        self.mascarilla_colocada = True

juanito = Persona(nombre='Juan', cedula='123456789')


if juanito.mascarilla_colocada:
    print('Pase al super')
else:
    print('No entre')

juanito.ponerse_mascarilla(color='verde')

# Ejercicio

# # 1 suponga que la informacion de las personas este en una lista de tuplas
#  [
# ('andres', '323111'),
# ('maria', '784378'),
# ('susana', '913273'),
# ('paco', '14326'),
# ]

# 2 Usando una lista que contienen objetos Persona. Agregar a andres, maria, susana, paco

# 3 ejecutar el metodo ponerse_mascarilla a todos los objeto

# 4 consultar a todas las personas si tienen la mascarilla puesta