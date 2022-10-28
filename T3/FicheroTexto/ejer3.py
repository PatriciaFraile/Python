#Escribe un programa que pregunte al usuario los números de los ganadores que hay de una loteria 
#primitiva  , los guarde en la lista y los muestre por pantalla ordenados de menor a mayor
lista = []
for i in range (4):
    lista.append(int(input("Cuantos ganadores hay:")))
lista.sort()
print("Los numeros de los ganadores son "+str(lista))