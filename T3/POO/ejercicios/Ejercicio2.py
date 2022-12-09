class Persona():
    nombre = ""
    def __init__(self,nombre):
        self.nombre = nombre
        print("Persona creada", self.nombre)
class Cuenta():
    persona=[]
    cantidad = 0
    def __init__(self,cantidad,persona=[]):
        self.cantidad = cantidad
        self.persona = persona
        print(f"Hola {self.persona} , tu cantidad de dinero en tu cuenta es: {self.cantidad}")
nombre = input("Escribe tu nombre")
persona = Persona(nombre)
cuenta = Cuenta([persona])


