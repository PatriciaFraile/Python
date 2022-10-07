#Haz un programa que te pregunte por tu nombre y el numero de veces que quieres imprimir
nombre = input("Como te llamas")
numero =  int (input("Cuantas veces quieres que se repita"))
for i in range(numero):
    print(nombre,"\n")

