
class Persona:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.estomago = []
        self.horas_trabajas = 0
        self.conocimiento = {}

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

    def comer(self, alimento):
        self.estomago.append(alimento)

    def trabajar(self):
        self.horas_trabajas += 1

    def estudiar(self, materia, tiempo):
        if materia in self.conocimiento:
            self.conocimiento[materia] += tiempo
        else:
            self.conocimiento[materia] = tiempo


class Papa(Persona):
    def __init__(self, nombre, cedula, edad):
        Persona.__init__(self, nombre=nombre, cedula=cedula, edad=edad)

class Hijo(Persona):
    def __init__(self, nombre, cedula, edad):
        Persona.__init__(self, nombre=nombre, cedula=cedula, edad=edad)
        self.juguetes = []

    def jugar(self, juguete):
        self.juguetes.append(juguete)

    def trabajar(self):
        print(f'{self.nombre} no trabaja!')

hugito = Papa(nombre='Hugo', cedula='2314412', edad=40)
hugito.trabajar()
hugito.comer('sopa')
hugito.estudiar('gerencia', 4)
hugito.jugar(juguete='carros')

paquito = Hijo(nombre='Paco', cedula='1231321', edad=4)
paquito.comer('cereal')
paquito.comer('galleta')
paquito.trabajar()
paquito.estudiar(materia='papelitos', tiempo=2)

pass

#
# juanito = Persona(nombre='juan', cedula='11231', edad=20)
# juanito.comer('taco')
# juanito.trabajar()
# juanito.estudiar(materia='python', tiempo=2)
pass