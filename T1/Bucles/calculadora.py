numero = int(input("Escribe un numero"))
numero2 = int(input("Escribe un numero"))

while True:
    texto = int(input("""Que quieres hacer:
    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    5.Modulo
    6.Potencia """))
    if texto == 1:
        print("--Sumar--")
        suma = numero+numero2
        print("La suma es:",suma)
    elif texto==2:
        print("--Resta--")
        resta = numero+numero2
        print("La resta es:",resta)
    elif texto==3:
        print("--Multiplicar--")
        multiplicar = numero*numero2
        print("La multiplicacion es:", multiplicar)
    elif texto==4:
        print("--Dividir--")
        divide = numero/numero2
        print("La division es:",divide)
    elif texto==5:
        print("--Modulo--")
        modulo = numero%numero2
        print("Modulo",modulo)
    elif texto==6:
        print("--Potencia--")
        potencia = pow(numero,numero2)
        print("La potencia es:",potencia)
    else:
        break
    