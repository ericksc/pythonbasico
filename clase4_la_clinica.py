
la_clinica = {}

"""
{
    '1113213': {
           'id': '1113213',
           'nombre': 'juanito',
           'apellido': 'mora',
           'enfermedades' : [],
           'medicamentos' : [],
           },
    '433212': {
            'id': '433212'
            ......
    }
}
"""

def agregar_paciente(clinica, paciente):
    # todo clinica es un diccionario
    id = paciente['id']
    clinica[id] = paciente

def crear_paciente(id, nombre, apellido, telefono, direccion):
    paciente = {
        'id': id,
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'direccion': direccion,
        'enfermedades': [],
        'medicamentos': []
    }
    return paciente

def preguntar_datos_personales():
    id = input('Favor ingrese el id')
    nombre = input('Favor ingrese el nombre')
    apellido = input('Favor ingrese el apellido')
    telefono = input('Favor ingrese el telefono')
    direccion = input('Favor ingrese el direccion')
    mi_paciente = crear_paciente(id=id, nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion)
    return mi_paciente

def borrar_paciente(clinica, paciente):
    id = paciente['id']
    del clinica[id]


# estoy probando
#juanito = {
#     'id': '1234',
#     'nombre': 'Juan',
#     'apellido': 'Mora',
#     'enfermedades': [],
#     'medicamentos': [],
# }

# carlitos = {
#     'id': '5412',
#     'nombre': 'Carlos',
#     'apellido': 'Lopez',
#     'enfermedades': [],
#     'medicamentos': [],
# }

#agregar_paciente(clinica=la_clinica, paciente=juanito)
#agregar_paciente(clinica=la_clinica, paciente=carlitos)



while True:
    mi_paciente = preguntar_datos_personales()
    id = mi_paciente['id']
    if id not in la_clinica:
        agregar_paciente(clinica=la_clinica, paciente=mi_paciente)
    print(la_clinica)
    borrar_paciente(clinica=la_clinica, paciente=mi_paciente)

    print(la_clinica)



