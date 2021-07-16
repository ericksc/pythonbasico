from clase_6_leer_csv import leer_archivo

class carlitos:
    def __str__(self):
        return f'{self.mi_nombre}'

    def __repr__(self):
        return f'{self.mi_nombre}'

    # metodo : constructor
    def __init__(self, nombre, color):
        self.mi_nombre = nombre
        self.color = color
        print(f'Hola soy {self.mi_nombre}')

    def brincar(self):
        print('Estoy brincando')

    def lea(self, archivo):
        dato = leer_archivo(archivo)
        print(dato)

    def hable(self):
        print(f'hola soy {self} y soy de color {self.color}')



eddy = carlitos('eddy', 'rojo')
juan = carlitos('juan', 'azul')
eva = carlitos('eva', 'morado')

eva.lea('mi_familia.txt')

mis_juguetes = [eddy, juan, eva]
pass