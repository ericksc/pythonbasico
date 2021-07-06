
def datos_paciente (Identificacion, Nombre, Apellido, Telefono, Direccion, Enfermedades, Medicamentos):
    return [Identificacion, Nombre,Apellido,Telefono,Direccion,Enfermedades,Medicamentos]

Jose = datos_paciente(1,'Jose','Arguedas',88000001,'Heredia',['hipertension','diabetes'],['a','b','c'])
Alfredo = datos_paciente(2,'Alfredo','Leal',88000002,'Tibas',['sinusitis'],['d'])
Alfonso = datos_paciente(3,'Alfonso','Lacayo',[88000003],['Desamparados'],['hipertension','colesterol'],['a','b','e'])

lista_pacientes = []
lista_pacientes.append(Jose)
lista_pacientes.append(Alfredo)
lista_pacientes.append(Alfonso)

Identificacion, Nombre, Apellido, Telefono, Direccion, Enfermedades, Medicamentos = list(zip(*lista_pacientes))

while True:
    print("Lista de gestiones:")
    print("1. Gestion de pacientes")
    print("2. Reportes")

    operacion = input("Seleccione la gestion que desea realizar: ")

    if operacion == '1':
        id = int(input("Ingrese identificacion del paciente: "))
        if id in (Identificacion):
            editar_enfermedad = input("Editar lista de enfermedades (Si/No): ")
            if editar_enfermedad == 'Si':
                nueva_enfermedad = input("Enfermedad por la que consulta: ")
                Enfermedades[Identificacion.index(id)].append(nueva_enfermedad)
            editar_medicamento = input("Editar lista de medicamentos (Si/No): ")
            if editar_medicamento == 'Si':
                nuevo_medicamento = input("Medicamento prescrito: ")
                Medicamentos[Identificacion.index(id)].append(nuevo_medicamento)
            eliminar_paciente = input("Eliminar paciente (Si/No): ")
            if eliminar_paciente == 'Si':
                lista_pacientes.pop(Identificacion.index(id))
        else:
            print("Ingrese datos de paciente nuevo")
            nuevo_paciente = datos_paciente(id,input("Nombre: "),input("Apellido: "),input("Telefono: "),input("Direccion: "),
                                            list(input("Enfermedad(es) por la que consulta: ").split()),
                                            list(input("Medicamento(s) prescrito: ").split()))
            lista_pacientes.append(nuevo_paciente)
            Identificacion, Nombre, Apellido, Telefono, Direccion, Enfermedades, Medicamentos = list(zip(*lista_pacientes))

    elif operacion == '2':
        reporte_enfermedades = input("Reporte de enfermedades (Si/No): ")
        if reporte_enfermedades == 'Si':
            enfermedades_totales = []
            enfermedades_tratadas = []
            print("Enfermedades tratadas en la clinica:")

            for i in Enfermedades:
                if i not in enfermedades_totales:
                    enfermedades_totales.extend(i)
            for i in enfermedades_totales:
                if i not in enfermedades_tratadas:
                    enfermedades_tratadas.append(i)
                    print(i)

        reporte_medicamentos = input("Reporte de medicamentos (Si/No): ")
        if reporte_medicamentos == 'Si':
            medicamentos_totales = []
            medicamentos_entregados = []
            print("Medicamentos entregados en la clinica:")

            for i in Medicamentos:
                if i not in medicamentos_totales:
                    medicamentos_totales.extend(i)
            for i in medicamentos_totales:
                if i not in medicamentos_entregados:
                    medicamentos_entregados.append(i)
                    print(i)

        reporte_comparacion = input("Comparación de pacientes (Si/No): ")
        if reporte_comparacion == 'Si':
            id1 = int(input("Ingrese identificacion del paciente 1: "))
            id2 = int(input("Ingrese identificacion del paciente 2: "))

            enfermedades_comun = []
            for i in Enfermedades[Identificacion.index(id1)]:
                if i in Enfermedades[Identificacion.index(id2)]:
                    enfermedades_comun.append(i)
            print(f'Los pacientes con numeros de identificacion {id1} y {id2} tienen en comun: {enfermedades_comun}')

            enfermedades_diferentes1 = []
            for i in Enfermedades[Identificacion.index(id1)]:
                if i not in Enfermedades[Identificacion.index(id2)]:
                    enfermedades_diferentes1.append(i)
            enfermedades_diferentes2 = []
            for i in Enfermedades[Identificacion.index(id2)]:
                if i not in Enfermedades[Identificacion.index(id1)]:
                    enfermedades_diferentes2.append(i)
            print(f'El paciente con identificacion {id1} tiene {enfermedades_diferentes1}, mientras que el paciente '
                  f'con identificacion {id2} tiene {enfermedades_diferentes2}')

            medicamentos_comun = []
            for i in Medicamentos[Identificacion.index(id1)]:
                if i in Medicamentos[Identificacion.index(id2)]:
                    medicamentos_comun.append(i)
            print(f'Los pacientes con numeros de identificacion {id1} y {id2} toman: {medicamentos_comun}')

            medicamentos_diferentes1 = []
            for i in Medicamentos[Identificacion.index(id1)]:
                if i not in Medicamentos[Identificacion.index(id2)]:
                    medicamentos_diferentes1.append(i)
            medicamentos_diferentes2 = []
            for i in Medicamentos[Identificacion.index(id2)]:
                if i not in Medicamentos[Identificacion.index(id1)]:
                    medicamentos_diferentes2.append(i)
            print(f'El paciente con identificacion {id1} toma {medicamentos_diferentes1}, mientras que el paciente '
                  f'con identificacion {id2} toma {medicamentos_diferentes2}')

    otra_operacion = input("Desea realizar otra gestion (Si/No): ")

    if otra_operacion == 'No':
        break
