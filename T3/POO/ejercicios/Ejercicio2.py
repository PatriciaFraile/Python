class Persona():
    nombre = ""
    def __init__(self,nombre):
        self.nombre = nombre
        print("Persona creada", self.nombre)
    
    def __str__(self):
        return '{}'.format(self.nombre)
class Cuenta():
    persona=[]


    def __init__(self,cantidad ,persona=[]):
        self.persona = persona
        self.cantidad = cantidad

    def mostrarDatos(self):
        for p in self.persona:
           print(p) 
           print("Tienes " + str(self.cantidad)+"euros")

nombre = input("Escribe tu nombre")
cantidad = int(input("Escribe el dinero que tienes en tu cuenta"))
persona = Persona(nombre)
cuenta = Cuenta(cantidad,[persona])
cuenta.mostrarDatos()


