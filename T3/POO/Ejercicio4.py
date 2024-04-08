class Cuenta():
    titular = ""
    cantidad = 0
    def __init__ (self,titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular
    def mostrarDatos(self):
        print(self.titular)
        print(self.__cantidad)
    def ingresar(self,numero):
        if int(numero)> int(0):
            self.__cantidad+=int(numero)
        else:
            print("No debe ser negativo")
    def retirar(self,num):
        if int(num)<int(self.__cantidad):
            self.__cantidad=int(self.__cantidad)-int(num)
            print("guardado")
        else:
            print("Tiene que ser menor ")

nombre = input("Escribe tu nombre")
cantidad = input("Cuanto dinero quieres ")
cuenta = Cuenta(nombre)
cuenta.ingresar(cantidad)
cantidad2 = input("Cuanto quieres sacar")
cuenta.retirar(cantidad2)





