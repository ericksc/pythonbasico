
with open('mi_famila.txt') as f:
    mi_familia = f.readlines()

#papa, mama, hijo = mi_familia
#papa = papa.split(',')
#nombre_papa, *_ = papa

# cuanto dinero tiene en total mi  familia

total = 0

# un ciclo, #bucle , # for-loop
for miembro in mi_familia:
    miembro = miembro.rstrip('\n')
    miembro = miembro.split(',')
    *_, saldo = miembro

    total += int(saldo)


print(f'El dinero en total de mi familia es: {total}')
pass