#Escribe un programa que almacene en una lista los números de 1 al 10 y 
#los muestre por pantalla ordenados en orden inverso

numero = [1,2,3,4,5,6,7,8,9,10]

for i in range (1,11):
    print(numero[-i], end=",")