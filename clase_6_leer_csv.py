from copy import deepcopy

def leer_archivo(nombre_archivo):
  # para leer archivo txt
  with open(nombre_archivo) as file:
      datos = file.readlines()

  # procesar , limpiar los datos
  datos = [reglon.replace('\n', '') for reglon in datos]

  # por conveccion. datos como lista de listas
  datos = [reglon.split(',') for reglon in datos]

  # convertir la lista de listas a lista de diccionarios
  # 0 -> nombre
  # 1 -> apellido
  # 2 -> edad
  # 3 -> enfermedades
  # 4 -> medicamentos
  datos =[{'nombre': reglon[0],
    'apellido': reglon[1],
    'edad': reglon[2],
    'enfermedades': reglon[3],
    'medicamentos': reglon[4]
    } for reglon in datos]

  # procesando enfermedades
  [paciente.update({'enfermedades':  paciente['enfermedades'].split('|')}) for paciente in datos]
  # procesando medicamentos
  [paciente.update({'medicamentos':  paciente['medicamentos'].split('|')}) for paciente in datos]
  return datos


def escribir_archivo(nombre_archivo, mis_datos):
  """

  :param nombre_archivo: es el archivo a guardar
  :param mis_datos: es una lista de diccionarios
  :return:
  """
  # escribir en archivo
  # enfermedades -> diabetes|cancer|hambre
  # medicamentos -> pastalla|crema|agua
  # nombre,apellido,edad,enfermedades,medicamentos

  # aislar las estructuras

  datos = deepcopy(mis_datos)

  # convertir la lista de medicamentos hacia string de medicamentos separados por |
  [paciente.update({'medicamentos':  '|'.join(paciente['medicamentos'])}) for paciente in datos]

  # convertir la lista de enfermedades hacia string de enfermedades separados por |
  [paciente.update({'enfermedades':  '|'.join(paciente['enfermedades'])}) for paciente in datos]

  # convertir de lista de diccionarios a lista de listas
  datos = [list(paciente.values()) for paciente in datos]

  # de lista de listas a lista de string
  datos = [','.join(paciente) for paciente in datos]

  datos = [f'{paciente}\n' for paciente in datos]

  with open(nombre_archivo, mode='w') as file:
    file.writelines(datos)


if __name__ == '__main__':
  print('Estoy probando leer archivo')
  mis_datos = leer_archivo('mi_familia.txt')
  print(mis_datos)