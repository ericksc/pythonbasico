class Pato:
    def __init__(self, nombre): # constructor
        print(f'Me llamo {nombre}')

    def hable(self):
        print('Quaaack!')

    def camine(self):
        print('Walks like a duck.')

luis = Pato('Luiscito')
luis.hable()