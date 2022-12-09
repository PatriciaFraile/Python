class Persona():
    nombre = ""
    def __init__(self,nombre):
        self.nombre = nombre
        print("Persona creada", self.nombre)
class Cuenta():
    persona=[]
    cantidad = 0
    def __init__(self,cantidad,persona=[]):
        self.persona = persona
        self.cantidad = cantidad
    def mostrarDatos(self):
        for p in self.persona:
            print("Hola "+str(p)+" tienes "+cantidad) #No sale

nombre = input("Escribe tu nombre")
cantidad = int(input("Escribe el dinero que tienes en tu cuenta"))
persona = Persona(nombre)
cuenta = Cuenta(str(cantidad),[persona])
cuenta.mostrarDatos()


