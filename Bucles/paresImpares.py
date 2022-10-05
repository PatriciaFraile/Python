#Escriba un programa que pida dos números enteros y
#  escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

def numeros():
    numero1= int(input("Escribe un numero"))
    numero2= int(input(f"Escribe un numero mayor o igual de {numero1}"))

    if(numero2<numero1):
        print(f"Tiene que ser mayor o igual que {numero1}")
    else:
        for i in range(numero1 , numero2 + 1):
            if i%2==0:
                print(f"Es par el {i}")
            else:
                print(f"Es impar el{i}")



