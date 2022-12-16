'''Objetos dentro de Objetos'''
class Serie:
    def __init__(self, titulo, captitulos, lanzamiento):
        self.titulo = titulo
        self.capitulos = captitulos
        self.lanzamiento = lanzamiento
        print('Se ha creado la serie:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    serie = []  

    def __init__(self, serie=[]):
        self.serie = serie

    def agregar(self, p):  
        self.serie.append(p)

    def mostrar(self):
        for p in self.serie:
            print(p)  


p = Serie("La que se avecina", 200, 2022)
c = Catalogo([p])  
c.mostrar()
#c.agregar(Serie("La que se avecina", 200, 2022))  
#c.mostrar()