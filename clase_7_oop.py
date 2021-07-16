class controlando_conversion_a_str:
    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


class Plumas:
    def __str__(self):
        return f'color:{self.color}'

    def __repr__(self):
        return f'color:{self.color}'

    def __init__(self, color):
        self.color = color

class Pico:
    def __str__(self):
        return f'tamano:{self.tamano} forma:{self.forma} abierto:{self.abierto}'

    def __repr__(self):
        return f'tamano:{self.tamano} forma:{self.forma} abierto:{self.abierto}'

    def __init__(self, tamano, forma):
        self.tamano = tamano
        self.forma = forma
        self.abierto = False

    def abrir(self):
        self.abierto = True

    def cerrar(self):
        self.abierto = False

class Pata:
    def __str__(self):
        return f'tamano:{self.tamano} adelante:{self.adelante}'

    def __repr__(self):
        return f'tamano:{self.tamano} adelante:{self.adelante}'

    def __init__(self, tamano):
        self.tamano = tamano
        self.adelante = True

    def mover(self):
        self.adelante = not self.adelante

class ave(controlando_conversion_a_str):
    def __init__(self, color, tamano, forma):
        self.plumaje = [Plumas(color) for _ in range(1000)]
        self.pico = Pico(tamano=tamano, forma=forma)
        self.patas = [Pata(tamano=tamano) for _ in range(2)]

    def nadar(self):
        print('Moviendo las patas')

    def volar(self):
        print('Moviendo las alas')

    def comer(self):
        print('Usando el pico')

    def hablar(self):
        print(f'Las aves no hablan')


class Gallina(ave):
    def __init__(self, nombre, color, tamano, forma):
        super().__init__(color=color, tamano=tamano, forma=forma)
        self.el_nombre = nombre

    def volar(self):
        print('Las Gallinas no vuelan')

class Pato(ave):
    def __init__(self, nombre, color, tamano, forma):
        super().__init__(color=color, tamano=tamano, forma=forma)
        self.el_nombre = nombre

    def quack(self):
        print(f'Me llamo {self.el_nombre} y digo quack')


class Perico(ave):
    def __init__(self, nombre, color, tamano, forma):
        super().__init__(color=color, tamano=tamano, forma=forma)
        self.el_nombre = nombre


donald = Pato('donald', 'blanco', 'grande', 'ancho')
loretto = Perico('loretto', 'verde', 'pequeno', 'angosto')
rosita = Gallina('rosita', 'cafe', 'mediana', 'estrecho')

mis_mascotas = [donald, loretto, rosita]

for mascota in mis_mascotas:
    mascota.hablar()