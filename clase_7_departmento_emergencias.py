from random import randint

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.casos_resueltos = 0

    def generar_llamada(self):
        return randint(1, 10)

    def tipo_emergencia(self, llamadas):
        pass

    def trabajar(self):
        llamadas = self.generar_llamada()
        self.casos_resueltos += self.tipo_emergencia(llamadas)

    def empleado_del_mes(self):
        return self.casos_resueltos >= 10

class Bombero(Empleado):
    def __init__(self, nombre):
        Empleado.__init__(self, nombre=nombre)

    def tipo_emergencia(self, llamadas):
        return llamadas // 2


class Policia(Empleado):
    def __init__(self, nombre):
        Empleado.__init__(self, nombre=nombre)

    def tipo_emergencia(self, llamadas):
        return llamadas // 4

lista_empleados = []
lista_empleados.append(Bombero('Bob'))
lista_empleados.append(Policia('Joe'))

ciclo = False

while not ciclo:
    temp = []
    for mi_empleado in lista_empleados:
        mi_empleado.trabajar()
        temp.append(mi_empleado.empleado_del_mes())
        ciclo = any(temp)

for mi_empleado in lista_empleados:
    print(mi_empleado.nombre, mi_empleado.casos_resueltos)