

def leer_archivo(archivo='pacientes_clinica.txt'):
    with open(archivo) as file:
        datos = file.readlines()
    return datos

datos = leer_archivo()
pass