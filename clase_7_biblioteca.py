# La biblioteca
# Utilizando clases
# crear un sistema que permita registrar libros nuevos
# id, titulo, autor, editorial, anno

# inventario de prestamos
# usuario, id, fecha de prestamos , fecha de devolucion

# un objeto -> inventario de libros
# objetos -> libro
# objetos -> usuario

class libro:
    def __str__(self):
        return f"""id:{self.id}. titulo:{self.titulo}.
               autor: {self.autor}. editorial:{self.editorial}.
               anno:{self.anno}"""

    def __repr__(self):
        return f"""id:{self.id}. titulo:{self.titulo}.
               autor: {self.autor}. editorial:{self.editorial}.
               anno:{self.anno}"""

    def __init__(self, id, titulo, autor, editorial, anno):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anno= anno

class inventario:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, id, titulo, autor, editorial, anno):
        mi_libro = libro(id=id, titulo=titulo, autor=autor, editorial=editorial, anno=anno)
        self.libros.append(mi_libro)

    def prestar_libro(self, usuario, id, fecha_prestamo, fecha_devolucion):
        libro_prestado = [libro for libro in self.libros if libro.id == id][0]
        libro_prestado.usuario = usuario
        libro_prestado.fecha_prestamo = fecha_prestamo
        libro_prestado.fecha_devolucion = fecha_devolucion

mi_biblioteca = inventario()

mi_biblioteca.registrar_libro(id=1, titulo='el quijote',
                              autor='Cervantes', editorial='Oceano', anno=1640)

mi_biblioteca.prestar_libro(usuario='juanito', id=1,
                            fecha_prestamo='2021-07-12', fecha_devolucion='2021-08-01')
pass