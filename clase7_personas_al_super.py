import clases_persona as cl

listaPersonas = [('andres','323111'),('maria','784378'),('susana','913273'),('paco','14326')]
personas = []

for nombre, cedula in listaPersonas:
    personas.append(cl.Persona(nombre=nombre,cedula=cedula))

for persona in personas:
    persona.ponerse_mascarilla()

for persona in personas:
    if persona.mascarilla_colocada:
        print('pase adelante')
    else:
        print('Alto no puedes entrar')