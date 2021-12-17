#Crear un triangulo con *
num = int(input("Escribe un numero"))
for i in range(num):
    for j in range (i+1):
        print("*", end=" ")
    print("")