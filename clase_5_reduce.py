nombres = ['sue', 'john', 'tom']

from functools import reduce

resultado = reduce( lambda x, y: f'{x} {y}', nombres )
print(resultado)
