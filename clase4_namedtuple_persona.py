# Como crear una persona usando namedtuple

from collections import namedtuple

Persona = namedtuple('Persona', ['fecha_nacimiento', 'edad', 'cedula', 'nombre', 'apellido', 'direccion'])

juanito = Persona(fecha_nacimiento='2000-01-5',
                  edad=20, cedula='313312165', nombre='Juan',
                  apellido='Perez', direccion='Del estadio 100m Norte')

print(f'Hola don {juanito.nombre}')