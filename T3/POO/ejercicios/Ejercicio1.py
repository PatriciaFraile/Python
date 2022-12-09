class Persona():
    nombre = ""
    edad = 0
    dni = ""
    def __init__ (self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def mostrarDatos(self):
        print(f"{self.nombre} , {self.edad}, tu dni es {self.dni}")
    def esMayorEdad(self):
        if(self.edad>18):
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
nombre = input("Escribe tu nombre")
edad = int(input("Cuantos años tienes"))
dni = input("Tu dni es:")
personaUno = Persona(nombre,edad,dni)
personaUno.mostrarDatos()
personaUno.esMayorEdad()