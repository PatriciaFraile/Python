#Escribe un numero entero y positivo.
#Muestre la cuenta atrás
numero = int(input("Escribe un numero positivo"))
for i in range(numero,-1,-1):
    print(i , end=" ")