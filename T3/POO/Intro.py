#Función Type
numero = 10
print(type(numero))
#Definicion de clases
class Numeros():
    pass
#Ejercicio para repasar 
class Galleta():
    chocolate = False
galleta = Galleta()
if galleta.chocolate:
    print("Tiene chocoalate")
else:
    print("No tiene chocolate")
#Podemos cambiar el valor de chocolate = False haciendolo:
galleta.chocolate = True 
#Entonces:
if galleta.chocolate:
    print("Tiene chocolate")
else:
    print("No tiene chocolate")
#Podemos meter métodos en las clases:
class Galleta():
    chocolate = True
    def saludar():
        print("Hola , tengo chocolate")
galleta= Galleta()
Galleta.saludar()
#Se puede hacer de otra manera, haciendolo :
class Galleta():
    chocolate = True
    def saludar(soy_el_propio_objeto):#También se puede utilizar la convención self
        print("Buenas")
galleta = Galleta()
galleta.saludar()
#Creación de constructores dentro de la clase
class Galleta():
    #Iniciar el contructor sin llamarlo
    def __init__(self,sabor,color):
        self.sabor=sabor
        self.color = color
        print(f"Tu galleta {self.color} y {self.sabor}.")
galleta_uno = Galleta("Marron","Chocolate")
galleta_dos = Galleta("BLanco","Blanco")
#También existe un constructor que hace eliminar el objeto, haciendolo así:
class Galleta():
    def __del__(self):
        print("Galleta eliminada")
galleta = Galleta()
del(galleta)
#Constructor str , devuelve la representación del objeto
class Galleta():
    def __init__(self,color):
        self.color = color
    def __str__(self):
        return f"El color de la galleta es:{self.color}"
galleta = Galleta("Marron")
print(galleta.__str__())
#El metodo len , devuelve la longitud , es lo mismp que el str
