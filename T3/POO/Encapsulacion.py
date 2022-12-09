'''class Numeros():
    __atributo_privado = "Soy un atributo grande"
numero = Numeros()
print(numero.__atributo_privado)#Saldra error'''
#Lo podemos hacer de otra manera para que no salga error y es:
class Numeros():
    __atributo_privado = "Soy un atributo grande"
    def atributo_publico(self):
        return self.__atributo_privado
numero = Numeros()
print(numero.atributo_publico())