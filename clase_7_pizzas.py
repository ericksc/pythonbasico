class pizza:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'Pizza({self.ingredientes})'

    @classmethod
    def margarita(cls):
        return (['mozzarella', 'tomate'])

    @classmethod
    def suprema(cls):
        return (['mozzarella', 'tomate', 'jamon'])

pizza.margarita()

pizza.suprema()
pass
