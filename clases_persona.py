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