num1 = int(input("Escribe un numero"))
num2 = int(input("Escribe un numero2"))

def suma(num1,num2):
    suma = num1+num2
    print("Suma",suma)

def resta(num1,num2):
    resta = num1-num2
    print("Resta",resta)

def dividir(num1,num2):
    dividir = num1/num2
    print("Dividir" ,dividir)

def multiplicar(num1,num2):
    multiplicar = num1*num2
    print("Multiplicar",multiplicar)


def modulo(num1,num2):
     modulo = num1%num2
     print("Modulo",modulo)

def potencia(num1,num2):
    potencia = pow(num1,num2)
    print("Potencia",potencia)

print(suma(num1,num2))
print(resta(num1,num2))
print(dividir(num1,num2))
print(modulo(num1,num2))
print(potencia(num1,num2))



